from ..compat import compat_HTTPError as compat_HTTPError, compat_etree_Element as compat_etree_Element, compat_parse_qs as compat_parse_qs, compat_str as compat_str, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, dict_get as dict_get, float_or_none as float_or_none, get_element_by_class as get_element_by_class, int_or_none as int_or_none, js_to_json as js_to_json, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, strip_or_none as strip_or_none, try_get as try_get, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor
from typing import Any

class BBCCoUkIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    class MediaSelectionError(Exception):
        id: Any
        def __init__(self, id) -> None: ...

class BBCIE(BBCCoUkIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class BBCCoUkArticleIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class BBCCoUkPlaylistBaseIE(InfoExtractor): ...
class BBCCoUkIPlayerPlaylistBaseIE(InfoExtractor): ...

class BBCCoUkIPlayerEpisodesIE(BBCCoUkIPlayerPlaylistBaseIE):
    IE_NAME: str

class BBCCoUkIPlayerGroupIE(BBCCoUkIPlayerPlaylistBaseIE):
    IE_NAME: str

class BBCCoUkPlaylistIE(BBCCoUkPlaylistBaseIE):
    IE_NAME: str
