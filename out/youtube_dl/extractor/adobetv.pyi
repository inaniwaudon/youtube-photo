from ..compat import compat_str as compat_str
from ..utils import ISO639Utils as ISO639Utils, OnDemandPagedList as OnDemandPagedList, float_or_none as float_or_none, int_or_none as int_or_none, parse_duration as parse_duration, str_or_none as str_or_none, str_to_int as str_to_int, unified_strdate as unified_strdate
from .common import InfoExtractor as InfoExtractor

class AdobeTVBaseIE(InfoExtractor): ...

class AdobeTVEmbedIE(AdobeTVBaseIE):
    IE_NAME: str

class AdobeTVIE(AdobeTVBaseIE):
    IE_NAME: str

class AdobeTVPlaylistBaseIE(AdobeTVBaseIE): ...

class AdobeTVShowIE(AdobeTVPlaylistBaseIE):
    IE_NAME: str

class AdobeTVChannelIE(AdobeTVPlaylistBaseIE):
    IE_NAME: str

class AdobeTVVideoIE(AdobeTVBaseIE):
    IE_NAME: str
