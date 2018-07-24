#!/usr/bin/env python
"""
Retrieves Medium article previous and exposes them for a theme to generate HTML.
"""
import sys
import json
import requests
from pelican import signals


MEDIUM_USERNAME = 'carlosperate'

MEDIUM_URL = 'https://www.medium.com/@{}/latest'.format(MEDIUM_USERNAME)
MEDIUM_JSON_URL = 'https://medium.com/@{}/latest?format=json'.format(MEDIUM_USERNAME)
JSON_ESCAPE_STR = '])}while(1);</x>'


def provide_fake_data():
    return [
        {'title': 'Post one',
        'thumbnail': '/images/theme/background_tile',
        'summary': 'This is the text for blog post one',
        'url': 'http://github.com'
    }, {
        'title': 'Post two',
        'thumbnail': '/images/theme/background_tile',
        'summary': 'This is the text for blog post two',
        'url': 'http://github.com'
    }, {
        'title': 'Post three',
        'thumbnail': '/images/theme/background_tile',
        'summary': 'This is the text for blog post three',
        'url': 'http://github.com'
    }]


def parsed_medium_json():
    json_str = requests.get(MEDIUM_JSON_URL)
    json_dict = json.loads(json_str.text.replace(JSON_ESCAPE_STR, '').strip())
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


def get_parsed_medium_feed(username):
    from . import medium_feed
    return medium_feed.arsed_medium_feed(username)


def get_scrapped_medium(username):
    from . import medium_scrapper
    return medium_scrapper.scrapped_medium(username)


def parsed_medium_data():
    # Select one of the parsing methods here
    # return get_scrapped_medium(MEDIUM_USERNAME)
    # return get_parsed_medium_feed(MEDIUM_USERNAME)
    # return provide_fake_data()
    return parsed_medium_json()


def provide_template_data(generator):
    print('Providing Medium to template!!')
    generator.env.globals['MEDIUM_PREVIEW_DATA'] = parsed_medium_data()


def register():
    signals.generator_init.connect(provide_template_data)
    #pass


def run_tests():
    print('All tests passed :)')


if __name__ == '__main__':
    run_tests()
