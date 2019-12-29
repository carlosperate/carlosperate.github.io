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

from pelican import signals
import re


def append_javascript(content):
    return content + '<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>'


def replace_twitter_handle(content):
    first_pass = re.sub(
        r'(^|[^@\w])&#64;(\w{1,15})\b',
        '\\1<a href="https://twitter.com/\\2" target="_blank">&#64;\\2</a>',
        content)
    return re.sub(
        r'(^|[^@\w])\@(\w{1,15})\b',
        '\\1<a href="https://twitter.com/\\2" target="_blank">&#64;\\2</a>',
        first_pass)


def replace_tweet(content, data_align):
    replace_str = '\\1<blockquote class="twitter-tweet" {}><a href="https://twitter.com/\\2/status/\\3">Tweet of \\2/\\3</a></blockquote>'.format(data_align)
    first_pass, first_count = re.subn(
        r'(^|[^@\w])&#64;(\w{1,15})/status/(\d+)\b', replace_str, content)
    second_pass, second_count = re.subn(
        r'(^|[^@\w])\@(\w{1,15})/status/(\d+)\b', replace_str, first_pass)
    return second_pass, (first_count + second_count)


def inject_twitter(content, tweet_align):
    content, embedding_replacements_made = replace_tweet(content, tweet_align)
    content = replace_twitter_handle(content)

    if embedding_replacements_made > 0:
        content = append_javascript(content)

    return content


def embed_tweet(content):
    tweet_align = ''
    if 'EMBED_TWEET_ALIGN' in content.settings:
        tweet_align = 'data-align="{}"'.format(content.settings['EMBED_TWEET_ALIGN'])
    if content and content._content:
        content._content = inject_twitter(content._content, tweet_align)


def register():
    signals.content_object_init.connect(embed_tweet)


class ContentMock:
    def __init__(self, preferred_content = ''):
        self._content = preferred_content


if __name__ == '__main__':
    assert -1 != inject_twitter(ContentMock('Link check &#64;professorsloth!')._content, '').find('href')
    assert -1 != inject_twitter(ContentMock('Link check @professorsloth!')._content, '').find('href')
    assert -1 != inject_twitter(ContentMock('Presence check &#64;professorsloth/status/639825328274309120 trailing content')._content, '').find('blockquote')
    assert -1 != inject_twitter(ContentMock('Presence check @professorsloth/status/639825328274309120 trailing content')._content, '').find('blockquote')
    assert -1 != inject_twitter(ContentMock('JS check &#64;professorsloth/status/639825328274309120 trailing content')._content, '').find('script')
    assert -1 != inject_twitter(ContentMock('JS check @professorsloth/status/639825328274309120 trailing content')._content, '').find('script')
    assert -1 == inject_twitter(ContentMock('No JS check &#64;professorsloth')._content, '').find('script')
    assert -1 == inject_twitter(ContentMock('No JS check @professorsloth')._content, '').find('script')
    assert -1 != inject_twitter(ContentMock('Set align check @professorsloth/status/639825328274309120 trailing content')._content, 'data-align="left"').find('data-align')
    assert -1 == inject_twitter(ContentMock('No align check @professorsloth/status/639825328274309120 trailing content')._content, '').find('data-align')
    print("All tests passed.")
