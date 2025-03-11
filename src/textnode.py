from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL

    def __eq__(self, object):
        return self.text == object.text and self.text_type == object.text_type and self.url == object.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"