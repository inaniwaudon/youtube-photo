from ..compat import compat_HTTPError as compat_HTTPError, compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, merge_dicts as merge_dicts, str_or_none as str_or_none, strip_or_none as strip_or_none, try_get as try_get, urlencode_postdata as urlencode_postdata
from .naver import NaverBaseIE as NaverBaseIE

class VLiveBaseIE(NaverBaseIE): ...

class VLiveIE(VLiveBaseIE):
    IE_NAME: str

class VLivePostIE(VLiveIE):
    IE_NAME: str

class VLiveChannelIE(VLiveBaseIE):
    IE_NAME: str
