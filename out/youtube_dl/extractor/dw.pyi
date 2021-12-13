from ..compat import compat_urlparse as compat_urlparse
from ..utils import int_or_none as int_or_none, unified_strdate as unified_strdate
from .common import InfoExtractor as InfoExtractor

class DWIE(InfoExtractor):
    IE_NAME: str

class DWArticleIE(InfoExtractor):
    IE_NAME: str
