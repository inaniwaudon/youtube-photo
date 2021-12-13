from ..compat import compat_parse_qs as compat_parse_qs, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import clean_html as clean_html, float_or_none as float_or_none, int_or_none as int_or_none, try_get as try_get, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor
from typing import Any

class CiscoLiveBaseIE(InfoExtractor):
    RAINFOCUS_API_URL: str
    RAINFOCUS_API_PROFILE_ID: str
    RAINFOCUS_WIDGET_ID: str
    BRIGHTCOVE_URL_TEMPLATE: str
    HEADERS: Any

class CiscoLiveSessionIE(CiscoLiveBaseIE): ...

class CiscoLiveSearchIE(CiscoLiveBaseIE):
    @classmethod
    def suitable(cls, url): ...
