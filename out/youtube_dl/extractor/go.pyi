from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, int_or_none as int_or_none, parse_age_limit as parse_age_limit, try_get as try_get, urlencode_postdata as urlencode_postdata
from .adobepass import AdobePassIE as AdobePassIE

class GoIE(AdobePassIE): ...
