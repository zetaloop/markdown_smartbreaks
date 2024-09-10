from markdown.extensions import Extension
from markdown.inlinepatterns import SubstituteTagInlineProcessor
from markdown.util import HTML_PLACEHOLDER
from xml.etree import ElementTree as etree
import re

BR_RE = r"\n"
HTML_PLACEHOLDER_RE = re.compile(HTML_PLACEHOLDER % r"([0-9]+)" + "$")


class SmartBreaksProcessor(SubstituteTagInlineProcessor):
    def handleMatch(
        self, m: re.Match[str], data: str
    ) -> tuple[etree.Element | str | None, int | None, int | None]:
        # if line ends with a html tag, don't add <br>
        if HTML_PLACEHOLDER_RE.search(data[: m.start(0)]):
            return None, None, None
        return etree.Element(self.tag), m.start(0), m.end(0)


class SmartBreaksExtension(Extension):
    def extendMarkdown(self, md):
        smartbr = SmartBreaksProcessor(BR_RE, "br")
        md.inlinePatterns.register(smartbr, "smartbreaks", 5.2374)


def makeExtension(**kwargs):
    return SmartBreaksExtension(**kwargs)
