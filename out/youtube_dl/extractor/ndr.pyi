from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, merge_dicts as merge_dicts, parse_iso8601 as parse_iso8601, qualities as qualities, try_get as try_get, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class NDRBaseIE(InfoExtractor): ...

class NDRIE(NDRBaseIE):
    IE_NAME: str
    IE_DESC: str

class NJoyIE(NDRBaseIE):
    IE_NAME: str
    IE_DESC: str

class NDREmbedBaseIE(InfoExtractor):
    IE_NAME: str

class NDREmbedIE(NDREmbedBaseIE):
    IE_NAME: str

class NJoyEmbedIE(NDREmbedBaseIE):
    IE_NAME: str
