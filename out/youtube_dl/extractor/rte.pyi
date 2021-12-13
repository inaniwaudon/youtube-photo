from ..compat import compat_HTTPError as compat_HTTPError
from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, parse_iso8601 as parse_iso8601, str_or_none as str_or_none, try_get as try_get, unescapeHTML as unescapeHTML, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class RteBaseIE(InfoExtractor): ...

class RteIE(RteBaseIE):
    IE_NAME: str
    IE_DESC: str

class RteRadioIE(RteBaseIE):
    IE_NAME: str
    IE_DESC: str
