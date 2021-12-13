from ..utils import ExtractorError as ExtractorError
from .common import InfoExtractor as InfoExtractor

class TestURLIE(InfoExtractor):
    IE_DESC: bool
