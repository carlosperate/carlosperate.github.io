# -*- coding: utf-8 -*-

# Copyright (c) 2013 Kura
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import directives, Directive
from pelican import signals
import re


class YouTube(Directive):
    """ Embed YouTube video in posts.

    Based on the YouTube directive by Brian Hsu:
    https://gist.github.com/1422773

    VIDEO_ID is required, other arguments are optional

    Usage:
    .. youtube:: VIDEO_ID
    """

    @staticmethod
    def boolean(argument):
        """Conversion function for yes/no True/False."""
        value = directives.choice(argument, ('yes', 'True', 'no', 'False'))
        return value in ('yes', 'True')

    required_arguments = 1
    optional_arguments = 5
    option_spec = {
        'class': directives.unchanged,
        'width': directives.positive_int,
        'height': directives.positive_int,
        'allowfullscreen': boolean,
        'seamless': boolean,
    }

    final_argument_whitespace = False
    has_content = False


    @staticmethod
    def generate_youtube_html(thisObj):
        """Simple refactor of all the code in the run method to be able to call
        it externally without touching the restructured text directives."""
        videoID = thisObj.arguments[0].strip()
        url = 'https://www.youtube.com/embed/{}'.format(videoID)

        width = thisObj.options['width'] if 'width' in thisObj.options else None
        height = thisObj.options['height'] if 'height' in thisObj.options else None
        fullscreen = thisObj.options['allowfullscreen'] \
            if 'allowfullscreen' in thisObj.options else True
        seamless = thisObj.options['seamless'] \
            if 'seamless' in thisObj.options else True

        css_classes = 'youtube'
        if 'class' in thisObj.options:
            css_classes += ' {}'.format(thisObj.options['class'])
        elif height is None:
            # use responsive design with 16:9 aspect ratio by default
            css_classes += ' {}'.format('youtube-16x9')
        # no additional classes if dimensions (height/width) are specified

        iframe_arguments = [
            (width, 'width="{}"'),
            (height, 'height="{}"'),
            (fullscreen, 'allowfullscreen'),
            (seamless, 'seamless frameBorder="0"'),
        ]

        div_block = '<div class="{}">'.format(css_classes)
        embed_block = '<iframe src="{}" '.format(url)

        for value, format in iframe_arguments:
            embed_block += (format + ' ').format(value) if value else ''

        embed_block = embed_block[:-1] + '></iframe>'

        return [
            div_block,
            embed_block,
            '</div>',
        ]
    
    def run(self):
        code_str = self.generate_youtube_html(self)
        return [nodes.raw('', item, format='html') for item in code_str]


# Old register for Restructured Text, new one on the section below
# def register():
#     directives.register_directive('youtube', YouTube)

##############################################################################
# The following code has been added to work with Markdown to inject the HTML
# directly into the content when a special hook is found: [[{ ... }]]
#
# The implementation is very very rough and inneficient, but it will do for
# the purposes of this blog.
##############################################################################

class FakeDirective():
    """We create a fake Restructured Text directive to reuse the plugin code."""

    def __init__(self, video_id, options):
        self.arguments = [video_id]
        self.options = options


def get_youtube_entries(content):
    return re.findall(r"\[\[{((.|\n|\r)*?)}\]\]", content)


def parse_entries(entries):
    entries_html = []
    for entry in entries:
        code = "{%s}" % entry[0]
        options = eval(code)
        fake_directive = FakeDirective(options["YouTube"], options)
        youtube_html = YouTube.generate_youtube_html(fake_directive)
        youtube_html = "".join(youtube_html)
        entries_html.append(('[[%s]]' % code, youtube_html))
    return entries_html


def replace_entries_with_html(content, entries_html):
    for (entrie, html) in entries_html:
        content = content.replace(entrie, html)
    return content


def inject_youtube(content):
    entries = get_youtube_entries(content)
    entries_html = parse_entries(entries)
    content = replace_entries_with_html(content, entries_html)
    return content


def embed_youtube(content):
    if content and content._content:
        content._content = inject_youtube(content._content)


def register():
    signals.content_object_init.connect(embed_youtube)
    directives.register_directive('youtube', YouTube)


def run_tests():
    test_content = """Some text goes here and then: [[{
        "YouTube": "8dc4siImaz8",
        "allowfullscreen": True,
        "seamless": True
    }]]
    More Youtube stuff:
    [[{
        "YouTube": "8dc4siImaz8",
        "width": 640,
        "height": 480
    }]]"""

    test_entries = ("""[[{
        "YouTube": "8dc4siImaz8",
        "allowfullscreen": True,
        "seamless": True
    }]]""", """[[{
        "YouTube": "8dc4siImaz8",
        "width": 640,
        "height": 480
    }]]""")

    test_result_html = ('<div class="youtube youtube-16x9">'
        '<iframe src="https://www.youtube.com/embed/8dc4siImaz8" '
        'allowfullscreen seamless frameBorder="0"></iframe></div>',
        '<div class="youtube">'
        '<iframe src="https://www.youtube.com/embed/8dc4siImaz8" width="640" '
        'height="480" allowfullscreen seamless frameBorder="0"></iframe></div>'
    )

    test_content_injected = "Some text goes here and then: " + \
        test_result_html[0] + "\n    More Youtube stuff:\n    " + \
        test_result_html[1]

    # Testing get_youtube_entries()
    # print(get_youtube_entries(test_content))
    assert len(get_youtube_entries(test_content)) == 2
    re_valid_strs = '[[{this}]] [[{!this = ʤ}]] [[{"this one": True}]] [[{{"nested object"}}]]'
    assert len(get_youtube_entries(re_valid_strs)) == 4
    re_invalid_strs = '[nope] {nope} [[nope]] {{nope}} [{nope}]  [{{nope}}]'
    assert len(get_youtube_entries(re_invalid_strs)) == 0

    # Testing parse_content()
    result_tuple = parse_entries(get_youtube_entries(test_content))
    assert result_tuple[0][0] == test_entries[0]
    assert result_tuple[0][1] == test_result_html[0]
    assert result_tuple[1][0] == test_entries[1]
    assert result_tuple[0][1] == test_result_html[0]

    # Testing inject_youtube()
    assert inject_youtube(test_content) == test_content_injected
    print(inject_youtube(test_content))
    print("All tests passed.")


if __name__ == '__main__':
    run_tests()
