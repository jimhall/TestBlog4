---
layout: post
title: "VirtualBox Remote Desktop Crazy Combo With Cut and Paste"
date: 2020-09-01
categories: [computing]
tags: [virtualbox, solaris, windows10, macos]
image: "https://www.virtualbox.org/graphics/vbox_logo2_gradient.png"
excerpt_separator: <!--more-->
---

I wanted to scribble down some notes on remote desktop and VirtualBox
using Microsoft Remote Desktop. When I got started I realized I had
a really complex combination of Operating Systems, but it all worked
seemlessly. Here is how I got it work, including a step needed to get
cut-n-paste to work.

<!--more-->

At a high level I wanted to connect to the console of a
[VirtualBox](https://www.virtualbox.org) guest from my development machine and
investigate if "cut and paste" was possible between the development machine
and the guest console. Here is a simple diagram of the environment I wound up
with:


<pre>
┌──────────────────────────────────────┐                  ┌──────────────────────────────────────┐
│                                      │                  │                                      │
│   ┌────────────────────┐             │                  │   ┌────────────────────┐             │
│   │                    │             │                  │   │                    │             │
│   │   Solaris          │             │                  │   │   Microsoft        │             │
│   │   Vbox Guest       │             │                  │   │   Remote Desktop   │             │
│   │   (Bridged Mode)   │             │                  │   │                    │             │
│   │   IP: 10.0.0.72    │             │◀────WiFi Net────▶│   │                    │             │
│   │   Name: jimwin8    │             │                  │   │                    │             │
│   │                    │             │                  │   │                    │             │
│   └────────────────────┘             │                  │   └────────────────────┘             │
│                                      │                  │                                      │
│                                      │                  │                                      │
│       Win10 Host IP: 10.0.0.182      │                  │       MacOS (machine I type on)      │
└──────────────────────────────────────┘                  └──────────────────────────────────────┘
</pre>

The reason why I have titled this "Crazy Combo" is that I wound up with the
following combination of products to meet my needs:

- Windows 10 host running VirtualBox
- Solaris 11.3 VirtualBox guest
- My development machine running MacOS Catalina

Rationale for this combination is as follows:

- I prefer MacOS so I work day to day on that platform
- I needed to run other operating systems (like Solaris), but did not want to
  consume my laptop memory to guest OS consumption.
- So I started "scavenging" on ebay for a older gaming laptop with a
  reasonable amount of memory to run guests
- The gaming laptop runs Windows 10 and I did not want to invest time on
  getting Linux or Solaris to work on it.

So with that, I got the environment working, and overtime I found it getting
frustrating that when I needed console access I had to trundle over to the
gaming laptop. Not being a regular Win 10 user compounded things. So I started
investigating remote desktop clients for the Mac. Initially I went to
[VirtualBox](https://www.virtualbox.org/manual/UserManual.html#rdp-viewers)
site but it does not list a client that can specifically work on a Mac. Doing
some googling I stumbled upon the [Microsoft Remote
Desktop Client](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac).
Microsoft does not specifically talk about how to use it with VirtualBox but
seems to position it as a generic RDP client. So I tried it and everything
worked.

