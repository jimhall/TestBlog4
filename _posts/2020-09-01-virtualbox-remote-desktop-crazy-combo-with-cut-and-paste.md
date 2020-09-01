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

Started investigating remote desktop clients on the
[VirtualBox](https://www.virtualbox.org/manual/UserManual.html#rdp-viewers)
site but it does not list a client that can specifically work on a Mac. Doing
some googling I stumbled upon the [Microsoft Remote
Desktop Client](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac).
Microsoft does not specifically talk about how to use it with VirtualBox but
seems to position it as a generic RDP client. So I tried it and everything
worked.

