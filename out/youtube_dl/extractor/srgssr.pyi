from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, qualities as qualities, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class SRGSSRIE(InfoExtractor): ...

class SRGSSRPlayIE(InfoExtractor):
    IE_DESC: str
