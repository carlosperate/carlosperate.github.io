Title: Article Title
Author: carlosperate
Date: 2000-12-30
Modified: 2019-12-27
Category: Blog
Tags: github, documentation, web-tech, raspberry-pi, beaglebone, sbc, event, arduino, microbit
Slug: template
Summary: Summary in 50 words?
Lang: en
Status: draft
og_image: /images/something.jpg
related_posts: static-docs-from-github-wiki, static-docs-from-github-wiki, static-docs-from-github-wiki


This is a template. Ideally if I add extra tags I should add them here as well.

<!-- This is a comment -->

<!-- Note: I still need to test the `og_image` page attribute. -->

Contents:

[TOC]


## Adding Tweets

Here is a text tweet with link:

@carlosperate/status/802144214628921344

Here is a text tweet with media:

@carlosperate/status/333995782304825344

Link to a tweeter username: @carlosperate


## Adding Images

![Talk Schedule Saturday](/images/theme/background_tile.png)


### Additional Formatting with HTML

These two images fit side to side:

<img src="/images/theme/background_tile.png" alt="alt 1" width="49%">
<img src="/images/theme/background_tile.png" alt="alt 2" width="49%">

And for a full width image (only works with no sidebar):

<img src="/images/banners/quickhue_banner.png" alt="alt 3" class="full-width">

And this one is just slightly wider than the container (only works with no
sidebar):

<img src="/images/banners/quickhue_banner.png" alt="alt 3" class="wider-than-parent">


## Adding YouTube Videos

Here is a responsive embedded YouTube video, only first key mandatory, the
others are shown with their default value:

[[{
    "YouTube": "8dc4siImaz8",
    "allowfullscreen": True,
    "seamless": True
}]]

Here is a embedded YouTube video with a fix width and height.
This is not recommended as it not responsive and will break the layout in
lower resolutions:

[[{
    "YouTube": "8dc4siImaz8",
    "width": 640,
    "height": 480
}]]

Minimal:

[[{"YouTube": "8dc4siImaz8"}]]
