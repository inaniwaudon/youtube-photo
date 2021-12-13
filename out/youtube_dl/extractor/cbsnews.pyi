from ..compat import compat_b64decode as compat_b64decode, compat_urllib_parse_unquote as compat_urllib_parse_unquote
from ..utils import parse_duration as parse_duration
from .cbs import CBSIE as CBSIE
from .common import InfoExtractor as InfoExtractor

class CBSNewsEmbedIE(CBSIE):
    IE_NAME: str

class CBSNewsIE(CBSIE):
    IE_NAME: str
    IE_DESC: str

class CBSNewsLiveVideoIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
