# -*- coding: utf-8 -*-
import json
import re

from webpreview import web_preview

from pelican import signals

MARKDOWN_DIRECTIVE_NAME = "SocialCard"

# TODO: Need to move the styles into a CSS file & recude sizes for mobile
HTML = """
<div style="
    display: block;
    height: 122px;
    padding: 0px;
    margin: 12px 24px;
    border-width: 1px;
    border-color: #bfbfbf;
    border-style: solid;
    border-radius: 6px;
    box-shadow: 0px 3px 6px rgb(0 0 0 / 7%);
    overflow: hidden;
">
    <div style="float: left; padding: 0; margin: 0; max-width: 192px; margin-right: 16px;{img_style}">
        <a href="{url}" target="_blank" style="border: none">
            <img src="{image}" style="height: 120px; object-fit: cover; padding: 0; margin: 0; border: none; margin-right: 16px;">
        </a>
    </div>
    <div style="margin: 16px; line-height: 1.2;">
        <a href="{url}" target="_blank"><span style="font-weight: bold;line-height: 1.8;">{title}</span></a>
        <br>
        <span style="line-height: 1.5">{description}</span>
    </div>
</div>
"""


def get_socialcard_entries(content):
    # Regex to match generic Markdown directives in this format:
    # ::Group1[Group2]{OptionalGroup3}
    # Group1 is the Directive name
    # Group2 is the values
    # Group3 are additional options as a json object of key value pairs
    directives = re.findall(r"\:\:([^\s]+?)\[([^\s]+?)](\{.*?\})?", content)
    # Filter only the directives for this extension, i.e. ::SocialCard[]{}
    return (e for e in directives if e[0] == MARKDOWN_DIRECTIVE_NAME)


def entries_to_html(entries):
    entries_html = []
    for entry in entries:
        if entry[2]:
            try:
                # We don't really any options right now
                options = json.loads(entry[2])
            except:
                raise Exception ("SocialCard Markdown option is not valid JSON", entry[2])
        card = web_preview(entry[1])
        # print("- {}\n\t- {}".format(entry, card))
        title, description, image = card
        card_options = {
             "title": title, "description": description, "url": entry[1]
        }
        if not image:
            card_options["img_style"] = "display: none"
            card_options["image"] = ""
        else:
            card_options["img_style"] = ""
            card_options["image"] = image
        card_html = HTML.format(**card_options)
        entries_html.append((
            "::{}[{}]{}".format(entry[0], entry[1], entry[2]),
            card_html
        ))
    return entries_html


def inject_socialcards(content):
    entries = get_socialcard_entries(content)
    entries_with_html = entries_to_html(entries)
    for (entry, html) in entries_with_html:
        content = content.replace(entry, html)
    return content


def embed_socialcard(content):
    if content and content._content:
        content._content = inject_socialcards(content._content)


def register():
    signals.content_object_init.connect(embed_socialcard)


if __name__ == '__main__':
    # TODO: Add some quick tests
    pass
