---
layout: post
title: "GitHub Pages 2020: Foundational Directories and Files (Part II)"
date: 2020-05-08
categories: [blog, computing, github]
tags: [ghpages, jekyll]
image: "https://jimhall.github.io/assets/images/greenscreen.png"
excerpt_separator: <!--more-->
---

After creating a repo in GitHub and enabling GitHub Pages for the repository,
you have a to pick a "theme". A theme is basically display style for your
website. In my case I chose the theme "Hacker".

<!--more-->

I took a look at the directory to see what was created and it turned out to be
a ` _config.yml` file. The contents of the file had a single entry of `theme:
jekyll-theme-hacker`. No other directories or files. This post addresses
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
- [x] Understanding How Pages Get Built
- [x] Review of _includes code considerations
- [x] Review _layouts code considerations
- [x] Review _sass code considerations
- [x] Create an index.md

## Theme Choice: An Aside

As mentioned above, I picked one of the default Jekyll theme's for GitHub
Pages called `jekyll-theme-hacker`. The black background and green font
reminded me of my days starting out building and designing trading floors for
financial services companies. When I first started the transition from "green
screens" (stacks of small picture tube monitors using phosphorescence to
"light up" the screen) to PCs and ethernet was kicking off. Think the movie Wall Street (see below):

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
[Part I](https://jimhall.github.io/blog/computing/2020/05/04/github-pages-part-one.html),
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
_sass
      |_ jekyll-theme-hacker-local.scss
      |_ jekyll-theme-hacker.scss
assets
      |_ images
categories
      |_ index.md
```

#### Table Describing Diagram

| File or Dir | Description                                                |
| ----------- | --------------                                             |
| [README.md](https://github.com/jimhall/jimhall.github.io/blob/master/README.md)     | Standard repo description of site. I use it as a changelog  |
| [.gitignore](https://github.com/jimhall/jimhall.github.io/blob/master/.gitignore)   | Since on a Macbook I skip all the .DS files                |
| [_config.yml](https://github.com/jimhall/jimhall.github.io/blob/master/_config.yml) | Jekyll config file                                          |
| [index.md](https://github.com/jimhall/jimhall.github.io/blob/master/index.md)       | Jekyll compiles/changes into index.html                     |
| [favicon.ico](https://github.com/jimhall/jimhall.github.io/blob/master/favicon.ico) | Graphic for bookmarks and URL bar                           |
| [about.md](https://github.com/jimhall/jimhall.github.io/blob/master/about.md)       | Jekyll compiles/changes into about.html (who am i?)         |
| [_includes/head.html](https://github.com/jimhall/jimhall.github.io/blob/master/_includes/head.html) | Jekyll template for `<head>` html metadata |
| [_includes/footer.html](https://github.com/jimhall/jimhall.github.io/blob/master/_includes/footer.html) | Jekyll template for `<footer>` (shown at the bottom of every page on my site) |
| [_includes/header.html](https://github.com/jimhall/jimhall.github.io/blob/master/_includes/header.html) | Jekyll template for `<header>` (shown at the top of every page on my site) |
| [ archive/index.md](https://github.com/jimhall/jimhall.github.io/blob/master/archive/index.md) | Jekyll template that generates a date sorted list of my blog posts |
| [_posts](https://github.com/jimhall/jimhall.github.io/blob/master/_posts) | Blog posts in markdown format that are then compiled into an html page |
| [_layouts/post.html](https://github.com/jimhall/jimhall.github.io/blob/master/_layouts/post.html) | HTML that renders blog post |
| [_layouts/tags.html](https://github.com/jimhall/jimhall.github.io/blob/master/_layouts/tags.html) | HTML that renders tag summary page post |
| [_layouts/default.html](https://github.com/jimhall/jimhall.github.io/blob/master/_layouts/default.html) | HTML that is default rendering for a web page for the blog |
| [_layouts/archive.html](https://github.com/jimhall/jimhall.github.io/blob/master/_layouts/archive.html) | HTML that renders the archive page |
| [_layouts/categories.html](https://github.com/jimhall/jimhall.github.io/blob/master/_layouts/categories.html) | HTML that renders a category web page for the blog |
| [tags/index.html](https://github.com/jimhall/jimhall.github.io/blob/master/tags/index.html) | HTML that renders a summary of tags web page for the blog |
| [_sass/jekyll-theme-hacker.scss](https://github.com/jimhall/jimhall.github.io/blob/master/_sass/jekyll-theme-hacker.scss) | CSS & SASS from the default `hacker` theme |
| [_sass/jekyll-theme-hacker-local.scss](https://github.com/jimhall/jimhall.github.io/blob/master/_sass/jekyll-theme-hacker-local.scss) | CSS & SASS from added by me |
| [assets/images/](https://github.com/jimhall/jimhall.github.io/blob/master/assets/images/) | HTML that renders a summary of tags web page for the blog | 
| [categories/index.md](https://github.com/jimhall/jimhall.github.io/blob/master/categories/index.md) | HTML that renders a summary of categories web page for the blog |

## Understanding How Pages Get Built

As I started to build some draft blog posts, I found it made sense to "break
up" the rendering to avoid repeating markdown and html for various pages. Let
me walk through my methods and thought process below.

- Blog Posts

1. Write the blog post in the `_posts` directory with Markdown. Add [Front
Matter](https://jekyllrb.com/docs/front-matter/) keyword `layout: post`.
This means it will refer to
[_layouts/post.html](https://github.com/jimhall/jimhall.github.io/blob/master/_layouts/post.html)
to begin the process of creating the blog post html. `post.html` also
has some html to set page date, title, and some [Jekyll
Liquid](https://jekyllrb.com/docs/liquid/) to display category and tags.
2. `_layouts/post.html` refers to
[_layouts/default.html](https://github.com/jimhall/jimhall.github.io/blob/master/_layouts/default.html).
`_layouts/default.html` with some simple html and [Jekyll Liquid include
tags](https://jekyllrb.com/docs/includes/) to build the `<head>`,
`<header>` and `<footer>` sections of the html doc. 
3.  [_includes/[head|header|footer].html](https://github.com/jimhall/jimhall.github.io/blob/master/_includes) contain the html that will
render the relevant section of the html document for the site.

- The Blog Archive Page

1.
[archive/index.md](https://github.com/jimhall/jimhall.github.io/blob/master/archive/index.md)
contains the [FrontMatter](https://jekyllrb.com/docs/front-matter/) keyword
`layout: archive`. This page is using some Jekyll Liquid for a loop that lists
all the posts put up on the site so far.
2. The front matter in `archive/index.md` will pull in
[_layouts/archive.html](https://github.com/jimhall/jimhall.github.io/blob/master/_layouts/archive.html)
which has similar [Jekyll Liquid include
tags](https://jekyllrb.com/docs/includes/) as `_layouts/default.html`,
just missing the `<div>` tag because are general content being developed
for the page.
3. Similar rendering as seen in step three for blog posts

- Tags and Category posts

1.  [tags/index.md](https://github.com/jimhall/jimhall.github.io/blob/master/tags) and
[categories/index.md](https://github.com/jimhall/jimhall.github.io/blob/master/categories)
have [Jekyll Liquid logic](https://jekyllrb.com/docs/liquid/) that lists out
all the tags or categories and the blog posts associated with them. It also
calls [Front Matter](https://jekyllrb.com/docs/front-matter/) keyword `layout:
default`. 
2. Similar rendering as seen in step three for blog posts for aspects of the
standard html doc for the site.

## Review `_includes` requirements

When building the site, it seemed to make most sense to have separate include
files for the `<head>`, `<header>` and `<footer>` sections of the
sites web pages and just keep it consistent. Leveraged the idea from the work
of @tocttou and their [hacker-blog
repo](https://github.com/tocttou/hacker-blog). Here are some notes:

### _includes/[head.html](https://github.com/jimhall/jimhall.github.io/blob/master/_includes/head.html)

- Created a lame logo for my site and used [Real Favicon
  Generator](https://realfavicongenerator.net) and dropped in the suggested
  meta tags [here](https://github.com/jimhall/jimhall.github.io/blob/cfc35d415f9b11cb3799a7a49a68926a4e1151c6/_includes/head.html#L9-L20)

- Added meta tags for social media referring to a [css-tricks
  article](https://css-tricks.com/essential-meta-tags-social-media/) and
  dropped the code
  [here](https://github.com/jimhall/jimhall.github.io/blob/cfc35d415f9b11cb3799a7a49a68926a4e1151c6/_includes/head.html#L21-L29).
  I created a liquid tag called `page.image` that gets added to the
  Jekyll Front Matter as `image:<image name>` in each blog post.

- I added `feed_meta` and `seo` liquid tags so that [jekyll-feed
  plug-in](https://www.rubydoc.info/gems/jekyll-feed/0.13.0) and search engine
  optimization is in place.

- [Added a Google Analytics fragment](https://desiredpersona.com/google-analytics-jekyll/) at [this
  location](https://github.com/jimhall/jimhall.github.io/blob/cfc35d415f9b11cb3799a7a49a68926a4e1151c6/_includes/head.html#L37-L48)

### _includes/[header.html](https://github.com/jimhall/jimhall.github.io/blob/master/_includes/header.html)

- Creates the standard top part `<header>` for the site with title of the
  blog, major site links and an RSS icon.

### _includes/[footer.html](https://github.com/jimhall/jimhall.github.io/blob/master/_includes/footer.html)

- Leveraged the
  [jekyll-theme-minimal](https://rubygems.org/gems/jekyll-theme-minimal) SVG
  file for [social media icons
  minima-social-icons.svg](https://github.com/jimhall/jimhall.github.io/tree/master/assets/images).
  Added only Twitter and GitHub icon at the base of the page. Additionally,
  added a [license and a copyright date using Liquid Tags `capture` tag](https://github.com/jimhall/jimhall.github.io/blob/cfc35d415f9b11cb3799a7a49a68926a4e1151c6/_includes/footer.html#L22-L26)).


