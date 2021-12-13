from ..compat import compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, get_element_by_class as get_element_by_class, int_or_none as int_or_none, orderedSet as orderedSet, str_or_none as str_or_none, str_to_int as str_to_int, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor
from .dailymotion import DailymotionIE as DailymotionIE
from .odnoklassniki import OdnoklassnikiIE as OdnoklassnikiIE
from .pladform import PladformIE as PladformIE
from .vimeo import VimeoIE as VimeoIE
from .youtube import YoutubeIE as YoutubeIE
from typing import Any, NamedTuple

class VKBaseIE(InfoExtractor): ...

class VKIE(VKBaseIE):
    IE_NAME: str
    IE_DESC: str

class VKUserVideosIE(VKBaseIE):
    IE_NAME: str
    IE_DESC: str

    class _VIDEO(NamedTuple):
        owner_id: Any
        id: Any

class VKWallPostIE(VKBaseIE):
    IE_NAME: str

    class _AUDIO(NamedTuple):
        id: Any
        owner_id: Any
        url: Any
        title: Any
        performer: Any
        duration: Any
        album_id: Any
        unk: Any
        author_link: Any
        lyrics: Any
        flags: Any
        context: Any
        extra: Any
        hashes: Any
        cover_url: Any
        ads: Any
