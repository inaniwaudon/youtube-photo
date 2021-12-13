from ..compat import compat_HTTPError as compat_HTTPError, compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, fix_xml_ampersands as fix_xml_ampersands, int_or_none as int_or_none, merge_dicts as merge_dicts, orderedSet as orderedSet, parse_duration as parse_duration, qualities as qualities, str_or_none as str_or_none, strip_jsonp as strip_jsonp, unified_strdate as unified_strdate, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class NPOBaseIE(InfoExtractor): ...

class NPOIE(NPOBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class NPOLiveIE(NPOBaseIE):
    IE_NAME: str

class NPORadioIE(InfoExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class NPORadioFragmentIE(InfoExtractor):
    IE_NAME: str

class NPODataMidEmbedIE(InfoExtractor): ...

class SchoolTVIE(NPODataMidEmbedIE):
    IE_NAME: str

class HetKlokhuisIE(NPODataMidEmbedIE):
    IE_NAME: str

class NPOPlaylistBaseIE(NPOIE): ...

class VPROIE(NPOPlaylistBaseIE):
    IE_NAME: str

class WNLIE(NPOPlaylistBaseIE):
    IE_NAME: str

class AndereTijdenIE(NPOPlaylistBaseIE):
    IE_NAME: str
