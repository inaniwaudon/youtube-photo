from ..compat import compat_str as compat_str
from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, try_get as try_get, unified_timestamp as unified_timestamp, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class EggheadBaseIE(InfoExtractor): ...

class EggheadCourseIE(EggheadBaseIE):
    IE_DESC: str
    IE_NAME: str

class EggheadLessonIE(EggheadBaseIE):
    IE_DESC: str
    IE_NAME: str
