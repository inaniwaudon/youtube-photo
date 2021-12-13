from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor
from .xstream import XstreamIE as XstreamIE

class VGTVIE(XstreamIE):
    IE_DESC: str

class BTArticleIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class BTVestlendingenIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
