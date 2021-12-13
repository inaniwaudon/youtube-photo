from ..utils import clean_html as clean_html, determine_ext as determine_ext, get_element_by_class as get_element_by_class
from .common import InfoExtractor as InfoExtractor

class NFLBaseIE(InfoExtractor): ...

class NFLIE(NFLBaseIE):
    IE_NAME: str

class NFLArticleIE(NFLBaseIE):
    IE_NAME: str
