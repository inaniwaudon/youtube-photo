from ..utils import float_or_none as float_or_none, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, sanitized_Request as sanitized_Request
from .common import InfoExtractor as InfoExtractor

class EitbIE(InfoExtractor):
    IE_NAME: str
