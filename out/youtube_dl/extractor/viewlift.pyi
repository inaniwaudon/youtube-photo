from ..compat import compat_HTTPError as compat_HTTPError
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_age_limit as parse_age_limit
from .common import InfoExtractor as InfoExtractor

class ViewLiftBaseIE(InfoExtractor): ...

class ViewLiftEmbedIE(ViewLiftBaseIE):
    IE_NAME: str

class ViewLiftIE(ViewLiftBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
