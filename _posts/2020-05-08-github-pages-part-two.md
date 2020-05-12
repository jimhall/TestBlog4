---
layout: post
title: "GitHub Pages 2020: Foundational Directories and Files (Part II)"
date: 2020-05-08
categories: [blog, computing]
tags: [ghpages, jekyll]
image: "https://jimhall.github.io/assets/images/greenscreen.png"
excerpt_separator: <!--more-->
---

After creating a repo in GitHub and enabling GitHub Pages for the repository,
you have a to pick a "theme". A theme is basically display style for your
website. In my case I chose the theme "Hacker".

<!--more-->

I took a look at the directory to see what was created and it turned out to be
a ``` _config.yml``` file. The contents of the file had a single entry of ```theme:
jekyll-theme-hacker```. No other directories or files. This post addresses
what directories and files I created to make a sane blog (in my opinion).

Take a look at the [ghpages tag page](https://jimhall.github.io/tags/ghpages)
for all the posts in this series.

## Overall Task Map (checked items in this post)

- [ ] Review relevant GitHub Labs
- [ ] Read/skim the GitHub Pages docs
- [ ] Read/skim the Jekyll docs
- [ ] Get Familiarthe supported Jekyll theme versions and plug-ins
- [ ] Create the GitHub repo for your site (e.g [https://jimhall.github.io](https://jimhall.github.io))
- [ ] Plan out a development model to update your site
- [x] Theme choice: an aside
- [x] Create directory structure for blogging
- [x] Review _includes requirements
- [x] Review _layouts requirements
- [x] Review _sass requirements
- [x] Create an index.md

## Theme Choice: An Aside

As mentioned above, I picked one of the default Jekyll theme's for GitHub
Pages called `jekyll-theme-hacker`. The black background and green font
reminded me of my days starting out building and designing trading floors for
financial services companies. When I first started the transition form "green
screens" (stacks of small picture tube monitors using phosphorescence to
"light up" the screen). Think the movie Wall Street (see below):

![Green Screen Image](https://jimhall.github.io/assets/images/greenscreen.png)

While I was attracted to the aesthetics of the theme, in hindsite I probably
should have picked a more complete theme like
[jekyll-theme-minimal](https://rubygems.org/gems/jekyll-theme-minimal).
Ironically, `jekyll-theme-hacker` was more "minimal" then
`jekyll-theme-minimal` in terms of the information it would display that would
be helpful for blog site. On the bright side, the lack of display
functionality helped capture a lot steps below on how to create a blog site.

## Create Directory Structure for Blogging

Strictly speaking, most of the steps below are optional. As mentioned in
[Part
I](https://jimhall.github.io/blog/computing/2020/05/04/github-pages-part-one.html),
you _could_ create a blog entry in the _posts directory and have at it. But I
take things a little bit further to create a more full featured blog.

### Diagram of File and Directory Structure

Here is a simple layout to create a more full featured blog:

```
README.md
.gitignore
index.md
_config.yml
favicon.ico
about.md
_includes
      |_ head.html
      |_ footer.html
      |_ header.html
archive
      |_ index.md
_posts
      |_ <various posts reside here>
_layouts
      |_ post.html
      |_ tags.html
      |_ default.html
      |_ archive.html
      |_ categories.html
tags
      |_ index.md
scripts
      |_ tags-n-cats.py
_sass
      |_ jekyll-theme-hacker-local.scss
      |_ jekyll-theme-hacker.scss
assets
      |_ images
           |_ favicon
                 |_ <icons for site>
           |_ arrow-58-32.png
           |_ minima-social-icons.svg
categories
      |_ index.md
```

#### Table Describing Diagram

| File or Dir | Description                                                |
| ----------- | --------------                                             |
| [README.md](https://github.com/jimhall/jimhall.github.io/blob/master/README.md)     | Standard repo description of site. I use it as a changelog  |
| [.gitignore](https://github.com/jimhall/jimhall.github.io/blob/master/.gitignore)   | Since on a Macbook I skip all the .DS* files                |
| [_config.yml](https://github.com/jimhall/jimhall.github.io/blob/master/_config.yml) | Jekyll config file                                          |
| [index.md](https://github.com/jimhall/jimhall.github.io/blob/master/index.md)       | Jekyll compiles/changes into index.html                     |
| [favicon.ico](https://github.com/jimhall/jimhall.github.io/blob/master/favicon.ico) | Graphic for bookmarks and URL bar                           |
| [about.md](https://github.com/jimhall/jimhall.github.io/blob/master/about.md)       | Jekyll compiles/changes into about.html (who am i?)         |
| [_includes/head.html](https://github.com/jimhall/jimhall.github.io/blob/master/_includes/head.html) | Jekyll template for `<head>` html metadata |
| [_includes/footer.html](https://github.com/jimhall/jimhall.github.io/blob/master/_includes/footer.html) | Jekyll template for `<footer>` (shown at the bottom of every page on my site) |
| [_includes/header.html](https://github.com/jimhall/jimhall.github.io/blob/master/_includes/header.html) | Jekyll template for `<header>` (shown at the top of every page on my site) |
| [archive/index.md](https://github.com/jimhall/jimhall.github.io/blob/master/archive/index.md) | Jekyll template that generates a date sorted list of my blog posts |
| [_posts](https://github.com/jimhall/jimhall.github.io/blob/master/_posts) | Blog posts in markdown format that are then compiled into an html page |

