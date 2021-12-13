from ..compat import compat_urlparse as compat_urlparse
from ..utils import parse_iso8601 as parse_iso8601, unified_timestamp as unified_timestamp
from .anvato import AnvatoIE as AnvatoIE
from .sendtonews import SendtoNewsIE as SendtoNewsIE

class CBSLocalIE(AnvatoIE): ...
class CBSLocalArticleIE(AnvatoIE): ...
