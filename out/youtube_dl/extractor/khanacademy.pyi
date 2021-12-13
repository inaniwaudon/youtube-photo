from ..utils import int_or_none as int_or_none, parse_iso8601 as parse_iso8601, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class KhanAcademyBaseIE(InfoExtractor): ...

class KhanAcademyIE(KhanAcademyBaseIE):
    IE_NAME: str

class KhanAcademyUnitIE(KhanAcademyBaseIE):
    IE_NAME: str
