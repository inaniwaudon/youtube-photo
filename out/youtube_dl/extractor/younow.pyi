from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor
from typing import Any

CDN_API_BASE: str
MOMENT_URL_FORMAT: Any

class YouNowLiveIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...

class YouNowChannelIE(InfoExtractor): ...

class YouNowMomentIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
