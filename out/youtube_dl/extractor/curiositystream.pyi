from ..utils import ExtractorError as ExtractorError, compat_str as compat_str, int_or_none as int_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class CuriosityStreamBaseIE(InfoExtractor): ...

class CuriosityStreamIE(CuriosityStreamBaseIE):
    IE_NAME: str

class CuriosityStreamCollectionIE(CuriosityStreamBaseIE):
    IE_NAME: str
