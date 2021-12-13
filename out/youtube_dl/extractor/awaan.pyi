from ..compat import compat_str as compat_str, compat_urllib_parse_urlencode as compat_urllib_parse_urlencode
from ..utils import int_or_none as int_or_none, parse_iso8601 as parse_iso8601, smuggle_url as smuggle_url, unsmuggle_url as unsmuggle_url, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class AWAANIE(InfoExtractor): ...
class AWAANBaseIE(InfoExtractor): ...

class AWAANVideoIE(AWAANBaseIE):
    IE_NAME: str

class AWAANLiveIE(AWAANBaseIE):
    IE_NAME: str

class AWAANSeasonIE(InfoExtractor):
    IE_NAME: str
