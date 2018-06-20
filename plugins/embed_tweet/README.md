__This a Pelican plugin from
https://github.com/professorsloth/pelican-embed-tweet , which is a fork of
https://github.com/lqez/pelican-embed-tweet , modified to only add the twitter
js files when a tweet is embedded into the page.__

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
