---
layout: post
title: "Configure Django 3.2 on Solaris"
date: 2022-07-06
categories: [computing]
tags: [solaris, django, python]
image: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Aktualne_logo_Oracle_Solaris_OS_OSos.png/250px-Aktualne_logo_Oracle_Solaris_OS_OSos.png"
excerpt_separator: <!--more-->
---

Trying to leverage what is bundled in Solaris 11.4, so I tried to configure
the latest version of Django. Simultaneously picked up some tricks on how to
manage packages on Solaris.

<!--more-->

## The Short Version (TL;DR: Configure the latest version of Django)

*Assuming* you have a full install of Solaris 11.4 (at this writing SRU43), it
seems to boil down to the following (Assumes you have the "System
Administrator" profile assigned):

```bash
$ getent user_attr jhall
jhall::::profiles=System Administrator;roles=root;audit_flags=cusa\:no
$ pfexec pkg install python-39
$ pfexec pkg set-mediator -v -V 3.9 --backup-be-name 11.4.43.113.3-switch-python3.9 python
$ mkdir try-django
$ cd try-django/
$ python -m venv --system-site-packages .
$ source bin/activate
$ python
Python 3.9.4 (default, Feb 10 2022, 06:27:49)
[GCC 11.2.0] on sunos5
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.VERSION
(3, 2, 11, 'final', 0)
```

And there you have it. Pretty darn easy/simple to get up and running and
manage your python environment with Solaris.

## The Long Version (Where I learn some things)

The "long version" has steps that led me to discover what I believe to be the
"short version" provided above. I would position this listing as "good faith
notes" and there may be more effective, optimized and/or accurate ways to
arrive at the desired destination.

### Manage packages on the system as a non-root user and install the latest Django

Solaris at this point is really full featured in being able to control what a
non-root user can do on the system. At install it asks for a non-root user
and adds the "System Administrator" profile to the account. Upon login you can
get information about the profile and note that is superset or grouping of more
granular profiles:

```bash
$ profiles -p "System Administrator" info
	name=System Administrator
	desc=profiles=Printer Management
	profiles=Fault Management,Install Service Management,Compliance Reporter,Unified Archive Administration,National Languages Support Management,Administrative Command History,Audit Review,Extended Accounting Flow Management,Extended Accounting Net Management,Extended Accounting Process Management,Extended Accounting Task Management,Cron Management,Device Management,File System Management,Log Management,Mail Management,Maintenance and Repair,Media Catalog,Name Service Management,Network Management,Project Management,RAD Management,Service Operator,Shadow Migration Monitor,Stat Store Management,Software Installation,System Configuration,User Management,ZFS Cloud Management,ZFS Storage Management
```

If the account being used was not added at install time, you
could simply add the "Software Installation" profile to do the work:

```bash
$ profiles -p "Software Installation" info
	name=Software Installation
	desc=Add application software to the system
	profiles=National Languages Support Management,ZFS File System Management
	cmd=/usr/sbin/beadm
	cmd=/usr/bin/ln
	cmd=/usr/bin/pkginfo
	cmd=/usr/bin/pkgmk
	cmd=/usr/bin/pkgparam
	cmd=/usr/bin/pkgproto
	cmd=/usr/bin/pkgtrans
	cmd=/usr/ccs/bin/make
	cmd=/usr/sbin/install
	cmd=/usr/sbin/pkgadd
	cmd=/usr/sbin/pkgask
	cmd=/usr/sbin/pkgchk
	cmd=/usr/sbin/pkgrm
	cmd=/usr/lib/rad/module/mod_ips.so.1
	cmd=/usr/lib/rad/module/mod_bemgr.so.1
	cmd=/usr/sbin/spliceadm
	cmd=/usr/bin/pkg
```
### Trying to figure out what is on the system currently

Running `pkg list | grep django` returned nothing, so it looked like my
install did not include the software. I performed the following steps to
arrive at the latest version provided by Oracle: 

- First I made a note of the current default python is:
```bash
$ /usr/bin/python -V
Python 3.7.12 (default, Mar 30 2022, 14:16:52)
```

- Decided to use the "dry run" option of `pkg` to see if simply running
  `pfexec pkg install -nv django` to see what would happen. I got the
  following output:

  ```bash
                 Packages to install:        11
           Estimated space available:  70.23 GB
      Estimated space to be consumed: 757.46 MB
             Create boot environment:        No
      Create backup boot environment:        No
                Rebuild boot archive:        No
    ```
- Removing the dry run option and going with `pfexec pkg install -v django`
  Solaris installs *two versions* of Django (3.2.11 and 2.2.26):

  ```bash
Changed packages:
solaris
  library/python/django
    None -> 3.2.11-11.4.43.0.1.113.1
  library/python/django-37
    None -> 2.2.26-11.4.43.0.1.113.1
  ```
- After install, running `pip freeze | grep Dj` shows the Django being imported by
  python is 2.2.26:
  ```bash
Django==2.2.26
   ```
- This is confirmed by running `pkg list -a *django*` (output truncated):
```bash
NAME (PUBLISHER)                                  VERSION                    IFO
library/python/django                             3.2.11-11.4.43.0.1.113.1   i--
library/python/django-37                          2.2.26-11.4.43.0.1.113.1   i--
library/python/django-39                          3.2.11-11.4.43.0.1.113.1   ---
```

- The combination of `pip freeze` and `pkg list` combined with `python -V`
  returning 3.7 revealed that the current active environment is a combination
  of python 3.7 and Django 2.2.26, which is package `library/python/django-37`.
  However, the "default" `library/python/django` is related to
  `library/python/django-39`, which according to the VERSION column would be
  Django 3.2.11, which according to the IFO column is not even *installed*.
  
- So it looks like in order to get Django 3.2.11, python 3.9 needs to be
  installed. Using `pkg list -a python-39` shows that python 3.9 is available
  in the repo, but is not installed:
```bash
NAME (PUBLISHER)                                  VERSION                    IFO
runtime/python-39                                 3.9.4-11.4.43.0.1.113.1    ---
```



Looking at the original script in the blog post, it is pretty slick. My
challenge is that I am behind the curve on REST programming in general! I
have a fairly basic grasp of python, but lack fundamentals on the requests
library. Here are some of my notes (a little random, but I think it is
illuminating as to how this stuff works):

- There is an `import requests` line at the top of the script, which I
  get (you need a package to make the http REST call). But why the `with
  requests.Session() as s` statment? Why bother with a _session_? (Line 17 in
  the script)  

  Answer: According to the
  [request docs](https://docs.python-requests.org/en/master/user/advanced/#session-objects)
  this allows cookies to persist between requests and re-uses the same TCP
  connection. The `with` keyword makes it a context manager and will make sure
  the session is closed as soon as the with block is exited, even if unhandled
  exceptions occurred.
  
- The zone is using a self-signed certificate for `https` connections. The
  client is a Mac. I could not get the blog post script to work initially.

  Answer: The blog post line of code:
  ```python
  r = s.post(login_url, json=config_json, verify='host.crt')
  ```

  Resulted in the following exception:

  ```python
  requests.exceptions.SSLError: 
  HTTPSConnectionPool(host='balder.norsestuff.com', port=6788): 
  Max retries exceeded with url: 
  /api/authentication/1.0/Session (Caused by
  SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED]
  certificate verify failed: unable to get local issuer certificate
  (_ssl.c:1108)')))
  ```

  After doing some research, I determined I needed to grab the zone's CA file:

  ```bash
  pwd
  /Users/jameshall/mysrc/python/solaris/rad/balder/CA
  scp backdoor@balder:/etc/certs/localhost/host-ca/hostca.crt .
  ```

  Then run the following `openssl` command in order to create the proper symlinks:

  ```bash
  ln -s hostca.pem `openssl x509 -hash -noout -in hostca.pem`.0
  ```

  Then I modified the script with a new post command using the path to the
  hostca file for the `verify` option:

  ```python
  r = s.post(login_url, json=config_json, verify='/Users/jameshall/mysrc/python/solaris/rad/balder/CA')
  ```

- How do you inspect the cookie that comes back? I was hoping that I could
  simply say `print(s.cookies.__dict__[blah])`, but not so much. Exploring the
  data structure got borked at the Cookie object.

  Answer: [https://docs.python-requests.org/en/master/api/#cookies](https://docs.python-requests.org/en/master/api/#cookies)

  ```python
  requests.utils.dict_from_cookiejar(s.cookies)
  ```
 
  and a little deeper into the structure:

  ```python
  requests.utils.dict_from_cookiejar(s.cookies)['_rad_instance']
  ```

  Sample API call and output:

  ```python
  requests.utils.dict_from_cookiejar(s.cookies)
  ```
  ```bash
  {'_rad_instance': '8960', '_rad_token': 'c2890180-7e70-42b0-a80f-b676161df99f'}
  ```

- How do you capture request status

  Answer: The [json](https://docs.python.org/3/library/json.html#module-json)
  package is needed. Add this line to the script:

  ```python
  >>> r.text
  '{\n        "status": "success",\n        "payload": "ONLINE"\n}'
  >>> bar = json.loads(r.text)
  >>> bar['status']
  'success'
  ```

- Tried to GET an SMF service that had a list of instances. Found
  `svc:/system/identity` had five instances:

  ```python
  query_url1 = "https://balder.norsestuff.com:6788/api/com.oracle.solaris.rad.smf/1.0/Service/system%2Fidentity/instances"
  ```
  This returns the following:

  ```bash
  The status code is: 200
  The return text is: {
          "status": "success",
          "payload": [
                  "cert",
                  "cert-expiry",
                  "domain",
                  "node",
                  "version"
          ]
  }
  ```

- An aside: Here is a code fragment  on exploring the session data structure
  which led to me determing that I needed to get further data about the
  session cookie via the `requests` API (see above).

  ```python
  >>> s.cookies.__dict__['_cookies']['balder.norsestuff.com']['/api']['_rad_instance']
  Cookie(version=0, name='_rad_instance', value='3840', port=None,
  port_specified=False, domain='balder.norsestuff.com',
  domain_specified=False, domain_initial_dot=False, path='/api',
  path_specified=True, secure=False, expires=1630617493, discard=False,
  comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
  ```

## Conclusion

It looks like I can run some slightly modified python code from a Mac client
and:

- Create a secure connection from the client by adding the hostca self-singed
  cert to the `verify` option.

- Manipulate the returned data structures to tell if the connection
  authenticated successfully.

- Inspect the cookies associated with the connection.

  Looks like there is a path to using this for Django authentication.

## Appendix: Modified blog post script

<script src="https://gist.github.com/jimhall/f8c08b94dbbe96cde0efc07ad712a69a.js"></script>
