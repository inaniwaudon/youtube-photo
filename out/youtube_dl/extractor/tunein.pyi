from ..compat import compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError
from .common import InfoExtractor as InfoExtractor

class TuneInBaseIE(InfoExtractor): ...

class TuneInClipIE(TuneInBaseIE):
    IE_NAME: str

class TuneInStationIE(TuneInBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class TuneInProgramIE(TuneInBaseIE):
    IE_NAME: str

class TuneInTopicIE(TuneInBaseIE):
    IE_NAME: str

class TuneInShortenerIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: bool
