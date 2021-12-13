from ..compat import compat_parse_qs as compat_parse_qs, compat_str as compat_str, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import dict_get as dict_get, int_or_none as int_or_none, parse_duration as parse_duration, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class SkyItPlayerIE(InfoExtractor):
    IE_NAME: str

class SkyItVideoIE(SkyItPlayerIE):
    IE_NAME: str

class SkyItVideoLiveIE(SkyItPlayerIE):
    IE_NAME: str

class SkyItIE(SkyItPlayerIE):
    IE_NAME: str

class SkyItAcademyIE(SkyItIE):
    IE_NAME: str

class SkyItArteIE(SkyItIE):
    IE_NAME: str

class CieloTVItIE(SkyItIE):
    IE_NAME: str

class TV8ItIE(SkyItVideoIE):
    IE_NAME: str
