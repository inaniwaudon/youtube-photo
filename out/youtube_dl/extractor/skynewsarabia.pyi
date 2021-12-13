from ..compat import compat_str as compat_str
from ..utils import parse_duration as parse_duration, parse_iso8601 as parse_iso8601
from .common import InfoExtractor as InfoExtractor

class SkyNewsArabiaBaseIE(InfoExtractor): ...

class SkyNewsArabiaIE(SkyNewsArabiaBaseIE):
    IE_NAME: str

class SkyNewsArabiaArticleIE(SkyNewsArabiaBaseIE):
    IE_NAME: str
