from ..compat import compat_b64decode as compat_b64decode, compat_urllib_parse_unquote as compat_urllib_parse_unquote, compat_urlparse as compat_urlparse
from ..utils import determine_ext as determine_ext, update_url_query as update_url_query
from .bokecc import BokeCCBaseIE as BokeCCBaseIE

class InfoQIE(BokeCCBaseIE): ...
