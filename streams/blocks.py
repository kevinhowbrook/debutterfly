"""Streamfields live in here."""

from wagtail.core import blocks


class ImageChooserBlock(blocks.StructBlock):

    class Meta: #noqa
        template = "streams/image_chooser.html"
        icon = "image"
        label = "Image"

class RawHTMLBlock(blocks.RawHTMLBlock):
    
    class Meta: #noqa
        template = "streams/embed_block.html"
        icon = "code"
        label = "HTML"

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add your text")

    class Meta: #noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichTextBlock(blocks.RichTextBlock):
    """"Richtext with all the features."""

    class Meta: #noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"

class SimpleRichTextBlock(blocks.RichTextBlock):
    """"Richtext without (limited) all the features."""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "blod",
            "italic",
            "link",
        ]
        super().__init__(**kwargs)


    class Meta: #noqa
        template = "streams/simple_richtext_block.html"
        icon = "edit"
        label = "Simple RichText"
