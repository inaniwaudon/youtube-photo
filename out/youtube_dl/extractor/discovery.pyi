from ..compat import compat_HTTPError as compat_HTTPError, compat_urllib_parse_unquote as compat_urllib_parse_unquote
from ..utils import ExtractorError as ExtractorError
from .discoverygo import DiscoveryGoBaseIE as DiscoveryGoBaseIE

class DiscoveryIE(DiscoveryGoBaseIE): ...
