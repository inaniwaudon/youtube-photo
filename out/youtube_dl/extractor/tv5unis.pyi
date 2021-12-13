from ..utils import int_or_none as int_or_none, parse_age_limit as parse_age_limit, smuggle_url as smuggle_url, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class TV5UnisBaseIE(InfoExtractor): ...

class TV5UnisVideoIE(TV5UnisBaseIE):
    IE_NAME: str

class TV5UnisIE(TV5UnisBaseIE):
    IE_NAME: str
