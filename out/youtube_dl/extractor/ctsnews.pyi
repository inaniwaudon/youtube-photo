from ..utils import unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor
from .youtube import YoutubeIE as YoutubeIE

class CtsNewsIE(InfoExtractor):
    IE_DESC: str
