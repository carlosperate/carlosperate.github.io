#!/usr/bin/env python
"""
Retrieves Medium articles via RSS using FeedParser
"""
import feedparser


def parsed_medium_feed(username):
    medium_rss_url = 'https://medium.com/feed/@{}'.format(username)
    parsed_feed = feedparser.parse(medium_rss_url)
    parsed_data = []
    for post in parsed_feed.entries:
        parsed_data.append({
            'title': post['title'],
            'thumbnailUrl': '',
            'summary': post['summary'],
            'url': post['link']
        })
    return parsed_data
