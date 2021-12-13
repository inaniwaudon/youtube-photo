from ..utils import ExtractorError as ExtractorError, unescapeHTML as unescapeHTML, unified_strdate as unified_strdate, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class DouyuTVIE(InfoExtractor):
    IE_DESC: str

class DouyuShowIE(InfoExtractor): ...
