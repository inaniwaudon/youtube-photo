from .amp import AMPIE as AMPIE
from .common import InfoExtractor as InfoExtractor

class FoxNewsIE(AMPIE):
    IE_NAME: str
    IE_DESC: str

class FoxNewsArticleIE(InfoExtractor):
    IE_NAME: str
