from ..compat import compat_str as compat_str
from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, unescapeHTML as unescapeHTML, urljoin as urljoin
from .srgssr import SRGSSRIE as SRGSSRIE

class RTSIE(SRGSSRIE):
    IE_DESC: str
