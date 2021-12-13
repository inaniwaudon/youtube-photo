from ..compat import compat_HTTPError as compat_HTTPError, compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, try_get as try_get, update_url_query as update_url_query
from .brightcove import BrightcoveNewIE as BrightcoveNewIE

class SevenPlusIE(BrightcoveNewIE):
    IE_NAME: str
