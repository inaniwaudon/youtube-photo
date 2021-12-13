from ..compat import compat_parse_qs as compat_parse_qs, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, update_url_query as update_url_query
from .theplatform import ThePlatformBaseIE as ThePlatformBaseIE

class MediasetIE(ThePlatformBaseIE): ...
