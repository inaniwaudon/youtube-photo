from ..compat import compat_urlparse as compat_urlparse
from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, js_to_json as js_to_json
from .common import InfoExtractor as InfoExtractor

class UDNEmbedIE(InfoExtractor):
    IE_DESC: str
