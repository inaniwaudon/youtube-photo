from ..utils import clean_html as clean_html, get_element_by_class as get_element_by_class, get_element_by_id as get_element_by_id
from .brightcove import BrightcoveNewIE as BrightcoveNewIE
from .common import InfoExtractor as InfoExtractor

class GameInformerIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str
