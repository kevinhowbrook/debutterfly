"""Streamfields live in here."""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


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

class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=100)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If button page above is selected, that will be used first")),
            ]
        )
    )

    class Meta:  # noqa
         template = "streams/card_block.html"
         icon = "placeholder"
         label = "Cards"

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


class ImageChooserBlock(blocks.StructBlock):

    class Meta: #noqa
        template = "streams/image_chooser.html"
        icon = "image"
        label = "Image"