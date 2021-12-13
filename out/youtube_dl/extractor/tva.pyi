from ..utils import float_or_none as float_or_none, int_or_none as int_or_none, smuggle_url as smuggle_url, strip_or_none as strip_or_none
from .common import InfoExtractor as InfoExtractor

class TVAIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str

class QubIE(InfoExtractor): ...
