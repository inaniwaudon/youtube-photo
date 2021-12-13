from ..compat import compat_HTTPError as compat_HTTPError, compat_kwargs as compat_kwargs, compat_str as compat_str, compat_urllib_request as compat_urllib_request, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, extract_attributes as extract_attributes, float_or_none as float_or_none, int_or_none as int_or_none, js_to_json as js_to_json, sanitized_Request as sanitized_Request, try_get as try_get, unescapeHTML as unescapeHTML, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class UdemyIE(InfoExtractor):
    IE_NAME: str

class UdemyCourseIE(UdemyIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
