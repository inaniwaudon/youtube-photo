from ..compat import compat_HTTPError as compat_HTTPError
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, age_restricted as age_restricted, clean_html as clean_html, int_or_none as int_or_none, try_get as try_get, unescapeHTML as unescapeHTML, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class DailymotionBaseInfoExtractor(InfoExtractor): ...

class DailymotionIE(DailymotionBaseInfoExtractor):
    IE_NAME: str

class DailymotionPlaylistBaseIE(DailymotionBaseInfoExtractor): ...

class DailymotionPlaylistIE(DailymotionPlaylistBaseIE):
    IE_NAME: str

class DailymotionUserIE(DailymotionPlaylistBaseIE):
    IE_NAME: str
