from ..compat import compat_b64decode as compat_b64decode, compat_chr as compat_chr, compat_ord as compat_ord, compat_str as compat_str, compat_urllib_parse_unquote as compat_urllib_parse_unquote, compat_zip as compat_zip
from ..utils import int_or_none as int_or_none, parse_iso8601 as parse_iso8601, strip_or_none as strip_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class MixcloudBaseIE(InfoExtractor): ...

class MixcloudIE(MixcloudBaseIE):
    IE_NAME: str

class MixcloudPlaylistBaseIE(MixcloudBaseIE): ...

class MixcloudUserIE(MixcloudPlaylistBaseIE):
    IE_NAME: str

class MixcloudPlaylistIE(MixcloudPlaylistBaseIE):
    IE_NAME: str
