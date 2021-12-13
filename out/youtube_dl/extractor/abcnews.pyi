from ..utils import parse_duration as parse_duration, parse_iso8601 as parse_iso8601, try_get as try_get
from .amp import AMPIE as AMPIE
from .common import InfoExtractor as InfoExtractor

class AbcNewsVideoIE(AMPIE):
    IE_NAME: str

class AbcNewsIE(InfoExtractor):
    IE_NAME: str
