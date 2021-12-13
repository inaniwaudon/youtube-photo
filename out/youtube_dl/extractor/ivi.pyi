from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, qualities as qualities
from .common import InfoExtractor as InfoExtractor

class IviIE(InfoExtractor):
    IE_DESC: str
    IE_NAME: str

class IviCompilationIE(InfoExtractor):
    IE_DESC: str
    IE_NAME: str
