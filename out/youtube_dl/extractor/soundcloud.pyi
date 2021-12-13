from ..compat import compat_HTTPError as compat_HTTPError, compat_kwargs as compat_kwargs, compat_str as compat_str, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, HEADRequest as HEADRequest, KNOWN_EXTENSIONS as KNOWN_EXTENSIONS, error_to_compat_str as error_to_compat_str, float_or_none as float_or_none, int_or_none as int_or_none, mimetype2ext as mimetype2ext, str_or_none as str_or_none, try_get as try_get, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_or_none as url_or_none, urlhandle_detect_ext as urlhandle_detect_ext
from .common import InfoExtractor as InfoExtractor, SearchInfoExtractor as SearchInfoExtractor

class SoundcloudEmbedIE(InfoExtractor): ...

class SoundcloudIE(InfoExtractor):
    IE_NAME: str

class SoundcloudPlaylistBaseIE(SoundcloudIE): ...

class SoundcloudSetIE(SoundcloudPlaylistBaseIE):
    IE_NAME: str

class SoundcloudPagedPlaylistBaseIE(SoundcloudIE): ...

class SoundcloudUserIE(SoundcloudPagedPlaylistBaseIE):
    IE_NAME: str

class SoundcloudTrackStationIE(SoundcloudPagedPlaylistBaseIE):
    IE_NAME: str

class SoundcloudPlaylistIE(SoundcloudPlaylistBaseIE):
    IE_NAME: str

class SoundcloudSearchIE(SearchInfoExtractor, SoundcloudIE):
    IE_NAME: str
    IE_DESC: str
