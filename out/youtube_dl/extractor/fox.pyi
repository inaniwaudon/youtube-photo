from ..compat import compat_HTTPError as compat_HTTPError, compat_str as compat_str, compat_urllib_parse_unquote as compat_urllib_parse_unquote
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_age_limit as parse_age_limit, parse_duration as parse_duration, try_get as try_get, unified_timestamp as unified_timestamp
from .adobepass import AdobePassIE as AdobePassIE

class FOXIE(AdobePassIE): ...
