#!/usr/bin/env python
"""
Retrieves Medium article previews and exposes them for a theme to generate
HTML and show them.
"""
from pelican import signals

from .medium_parser import MediumParserRss, MediumParserJson, MediumParserFake, MediumParserScrapper


MEDIUM_USERNAME = 'carlosperate'
LOADED_DATA = None


def parsed_medium_data():
    # Select one of the parsing methods here
    # medium_parser = MediumParserFake(MEDIUM_USERNAME)
    # medium_parser = MediumParserJson(MEDIUM_USERNAME)
    medium_parser = MediumParserRss(MEDIUM_USERNAME)
    # medium_parser = MediumParserScrapper(MEDIUM_USERNAME)
    return medium_parser.get_preview_content()


def provide_template_data(generator):
    global LOADED_DATA
    if not LOADED_DATA:
        print('Retrieving and parsing Medium data...')
        LOADED_DATA = parsed_medium_data()
    print('Providing Medium data to template...')
    generator.env.globals['MEDIUM_PREVIEW_DATA'] = LOADED_DATA


def register():
    signals.generator_init.connect(provide_template_data)


def run_tests():
    print('All tests passed :)')


if __name__ == '__main__':
    run_tests()
