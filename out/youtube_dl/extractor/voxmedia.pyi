from ..compat import compat_urllib_parse_unquote as compat_urllib_parse_unquote
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, try_get as try_get, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor
from .once import OnceIE as OnceIE

class VoxMediaVolumeIE(OnceIE): ...
class VoxMediaIE(InfoExtractor): ...
