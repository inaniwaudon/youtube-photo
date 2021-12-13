from ..compat import compat_parse_qs as compat_parse_qs, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_age_limit as parse_age_limit, parse_iso8601 as parse_iso8601, sanitized_Request as sanitized_Request, std_headers as std_headers, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class VikiBaseIE(InfoExtractor):
    @staticmethod
    def dict_selection(dict_obj, preferred_key, allow_fallback: bool = ...): ...

class VikiIE(VikiBaseIE):
    IE_NAME: str

class VikiChannelIE(VikiBaseIE):
    IE_NAME: str
