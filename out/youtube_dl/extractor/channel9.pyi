from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, qualities as qualities, unescapeHTML as unescapeHTML
from .common import InfoExtractor as InfoExtractor

class Channel9IE(InfoExtractor):
    IE_DESC: str
    IE_NAME: str
