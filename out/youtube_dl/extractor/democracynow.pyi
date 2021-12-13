from ..compat import compat_urlparse as compat_urlparse
from ..utils import remove_start as remove_start, url_basename as url_basename
from .common import InfoExtractor as InfoExtractor

class DemocracynowIE(InfoExtractor):
    IE_NAME: str
