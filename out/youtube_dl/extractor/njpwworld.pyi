from ..compat import compat_urlparse as compat_urlparse
from ..utils import get_element_by_class as get_element_by_class, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class NJPWWorldIE(InfoExtractor):
    IE_DESC: str
