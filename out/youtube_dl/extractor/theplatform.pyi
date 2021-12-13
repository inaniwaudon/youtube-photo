from ..compat import compat_parse_qs as compat_parse_qs, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, find_xpath_attr as find_xpath_attr, float_or_none as float_or_none, int_or_none as int_or_none, mimetype2ext as mimetype2ext, sanitized_Request as sanitized_Request, unsmuggle_url as unsmuggle_url, update_url_query as update_url_query, xpath_with_ns as xpath_with_ns
from .adobepass import AdobePassIE as AdobePassIE
from .once import OnceIE as OnceIE

default_ns: str

class ThePlatformBaseIE(OnceIE): ...
class ThePlatformIE(ThePlatformBaseIE, AdobePassIE): ...
class ThePlatformFeedIE(ThePlatformBaseIE): ...
