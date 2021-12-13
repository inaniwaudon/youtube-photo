from ..compat import compat_str as compat_str
from ..utils import int_or_none as int_or_none, merge_dicts as merge_dicts, try_get as try_get, unified_timestamp as unified_timestamp, urljoin as urljoin
from .youtube import YoutubeIE as YoutubeIE
from .zdf import ZDFBaseIE as ZDFBaseIE

class PhoenixIE(ZDFBaseIE):
    IE_NAME: str
