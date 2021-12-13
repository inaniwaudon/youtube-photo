from ..utils import int_or_none as int_or_none, parse_iso8601 as parse_iso8601, unescapeHTML as unescapeHTML
from .common import InfoExtractor as InfoExtractor

class PeriscopeBaseIE(InfoExtractor): ...

class PeriscopeIE(PeriscopeBaseIE):
    IE_DESC: str
    IE_NAME: str

class PeriscopeUserIE(PeriscopeBaseIE):
    IE_DESC: str
    IE_NAME: str
