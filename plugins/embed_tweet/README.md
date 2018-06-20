__This a Pelican plugin from
https://github.com/professorsloth/pelican-embed-tweet , which is a fork of
https://github.com/lqez/pelican-embed-tweet , that has been modified to only
add the twitter javascripts files when a tweet is embedded into the page.__

Further modifications done for this project:
* Pelican not always parses the `@` sign into `&#64;`, so do an additional pass
to parse it.
* Add extra tests
* Formatting

Everything below this line corresponds to the original README.md file.

pelican-embed-tweet
===================

Embedding tweets into your Pelican blog posts.


How to use this?
----------------

 1. Download `embed_tweet.py`
 1. Copy it wherever or just into `pelican/plugins/`
 1. Push back `embed_tweet` into plugin list of settings.
    - `PLUGINS = ['pelican.plugins.embed_tweet']`

 1. That's all!


Conversion
----------

 1. `@username` will be replaced by `https://twitter.com/username`
 1. `@username/status/tweetid` will be replaced by `Embedded-tweet`
    - See: <https://dev.twitter.com/docs/embedded-tweets>
    - Example: <http://lqez.github.io/blog/gittipcom-and-forkorea.html>


License
-------

Distributed under MIT license.


AUTHOR
------
Park Hyunwoo / [@lqez](https://twitter.com/lqez)
