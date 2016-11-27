#!/usr/bin/env python

"""
Embedded tweet plugin for Pelican
=================================

This plugin allows you to embed Twitter tweets into your articles.
And also provides a link for Twitter username.

    i.e.

        @username

        will be replaced by a link to Twitter username page.

        @username/status/tweetid

        will be replaced by a `Embedded-tweet`_ API.

.. _Embedded-tweet: https://dev.twitter.com/docs/embedded-tweets

"""

if __name__ != '__main__':
    from pelican import signals
import re

def append_javascript(content):
    return content + '<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>'

def replace_twitter_handle(content):
    return re.sub(
        r'(^|[^@\w])&#64;(\w{1,15})\b',
        '\\1<a href="https://twitter.com/\\2">&#64;\\2</a>',
        content)

def replace_tweet(content):
    return re.subn(
        r'(^|[^@\w])&#64;(\w{1,15})/status/(\d+)\b',
        '\\1<blockquote class="twitter-tweet"><a href="https://twitter.com/\\2/status/\\3">Tweet of \\2/\\3</a></blockquote>',
        content
    )

def inject_twitter(content):
    content, embedding_replacements_made = replace_tweet(content)
    content = replace_twitter_handle(content)

    if embedding_replacements_made > 0:
        content = append_javascript(content)

    return content

def embed_tweet(content):
    content._content = inject_twitter(content._content)

def register():
    signals.content_object_init.connect(embed_tweet)

class ContentMock:
    def __init__(self, preferred_content = ''):
        self._content = preferred_content

if __name__ == '__main__':
    assert -1 != inject_twitter(ContentMock('Link check &#64;professorsloth!')._content).find('href')
    assert -1 != inject_twitter(ContentMock('Presence check &#64;professorsloth/status/639825328274309120 trailing content')._content).find('blockquote')
    assert -1 != inject_twitter(ContentMock('JS check &#64;professorsloth/status/639825328274309120 trailing content')._content).find('script')
    assert -1 == inject_twitter(ContentMock('No JS check &#64;professorsloth')._content).find('script')

    print "All tests passed."

