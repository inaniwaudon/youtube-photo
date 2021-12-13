from ..compat import compat_str as compat_str, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, dict_get as dict_get, float_or_none as float_or_none, int_or_none as int_or_none, parse_duration as parse_duration, qualities as qualities, srt_subtitles_timecode as srt_subtitles_timecode, try_get as try_get, update_url_query as update_url_query, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class PluralsightBaseIE(InfoExtractor): ...

class PluralsightIE(PluralsightBaseIE):
    IE_NAME: str
    GRAPHQL_VIEWCLIP_TMPL: str

class PluralsightCourseIE(PluralsightBaseIE):
    IE_NAME: str
