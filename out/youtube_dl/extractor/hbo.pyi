from ..utils import int_or_none as int_or_none, parse_duration as parse_duration, urljoin as urljoin, xpath_element as xpath_element, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class HBOBaseIE(InfoExtractor): ...

class HBOIE(HBOBaseIE):
    IE_NAME: str
