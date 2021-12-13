from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, determine_ext as determine_ext, get_element_by_attribute as get_element_by_attribute, orderedSet as orderedSet
from .common import InfoExtractor as InfoExtractor

class TVPIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class TVPEmbedIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class TVPWebsiteIE(InfoExtractor):
    IE_NAME: str
