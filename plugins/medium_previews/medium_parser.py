#!/usr/bin/env python
"""
Retrieves Medium articles via RSS using FeedParser
"""
from abc import ABCMeta, abstractmethod
import json

import feedparser
import requests


class MediumParser(object):
    __metaclass__ = ABCMeta

    def __init__(self, username):
        self.username = username
        self.medium_url = 'https://www.medium.com/@{}'.format(self.username)

    @abstractmethod
    def get_preview_content(self):
        """ This should return a list of dictionaries with this format.
        {
            'title': 'Strig here',
            'thumbnailUrl': 'String with URL here',
            'summary': 'String here',
            'url': 'String with value full URL here'
        }
        """
        raise NotImplementedError


class MediumParserFake(MediumParser):
    """
    Retrieves Medium articles via RSS using FeedParser
    """

    def get_preview_content(self):
        return [{
                'title': 'Post one',
                'thumbnailUrl': '/images/theme/background_tile.png',
                'summary': 'This is the text for blog post one',
                'url': 'http://github.com'
            }, {
                'title': 'Post two',
                'thumbnailUrl': '/images/theme/background_tile.png',
                'summary': 'This is the text for blog post two',
                'url': 'http://github.com'
            }, {
                'title': 'Post three',
                'thumbnailUrl': '/images/theme/background_tile.png',
                'summary': 'This is the text for blog post three',
                'url': 'http://github.com'
            }
        ]


class MediumParserRss(MediumParser):
    """
    Retrieves Medium articles via RSS using FeedParser.
    """

    def get_preview_content(self):
        medium_rss_url = 'https://medium.com/feed/@{}'.format(self.username)
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


class MediumParserJson(MediumParser):
    """
    Retrieves Medium articles via JSON using Requests.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.medium_json_url = 'https://medium.com/@{}/latest?format=json'.format(self.username)
        self.json_escape_str = '])}while(1);</x>'

    def get_preview_content(self):
        json_str = requests.get(self.medium_json_url)
        json_dict = json.loads(json_str.text.replace(self.json_escape_str, '').strip())
        posts = json_dict['payload']['references']['Post']
        parsed_data = []
        for post_id in posts:
            thumb_id = posts[post_id]['virtuals']['previewImage']['imageId']
            parsed_data.append({
                'id': post_id,
                'title': posts[post_id]['title'],
                'thumbnailId': thumb_id,
                'thumbnailUrl': 'https://miro.medium.com/fit/c/1400/420/{}'.format(thumb_id),
                'summary': posts[post_id]['content']['subtitle'],
                'url': 'http://medium.com/p/{}'.format(post_id)
            })
        return parsed_data


class MediumParserScrapper(MediumParser):
    """
    Retrieves Medium articles scrapping the website.
    """

    def get_preview_content(self):
        from . import medium_scrapper
        return medium_scrapper.scrapped_medium(self.username)
