from ..compat import compat_str as compat_str
from ..utils import HEADRequest as HEADRequest, clean_html as clean_html, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, orderedSet as orderedSet, remove_end as remove_end, str_or_none as str_or_none, strip_jsonp as strip_jsonp, unescapeHTML as unescapeHTML, unified_strdate as unified_strdate, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class ORFTVthekIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class ORFRadioIE(InfoExtractor): ...

class ORFFM4IE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFNOEIE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFWIEIE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFBGLIE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFOOEIE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFSTMIE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFKTNIE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFSBGIE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFTIRIE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFVBGIE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFOE3IE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFOE1IE(ORFRadioIE):
    IE_NAME: str
    IE_DESC: str

class ORFIPTVIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class ORFFM4StoryIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
