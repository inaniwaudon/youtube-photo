from ..compat import compat_parse_qs as compat_parse_qs, compat_urllib_request as compat_urllib_request, compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, sanitized_Request as sanitized_Request, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class FC2IE(InfoExtractor):
    IE_NAME: str

class FC2EmbedIE(InfoExtractor):
    IE_NAME: str
