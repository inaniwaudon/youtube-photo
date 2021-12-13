from ..utils import ExtractorError as ExtractorError, orderedSet as orderedSet, unescapeHTML as unescapeHTML
from .common import InfoExtractor as InfoExtractor

class StanfordOpenClassroomIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
