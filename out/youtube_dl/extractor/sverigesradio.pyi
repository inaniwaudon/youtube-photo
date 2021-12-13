from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, str_or_none as str_or_none
from .common import InfoExtractor as InfoExtractor

class SverigesRadioBaseIE(InfoExtractor): ...

class SverigesRadioPublicationIE(SverigesRadioBaseIE):
    IE_NAME: str

class SverigesRadioEpisodeIE(SverigesRadioBaseIE):
    IE_NAME: str
