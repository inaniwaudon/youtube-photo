from ..compat import compat_HTTPError as compat_HTTPError
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, str_or_none as str_or_none, strip_or_none as strip_or_none, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class PacktPubBaseIE(InfoExtractor): ...
class PacktPubIE(PacktPubBaseIE): ...

class PacktPubCourseIE(PacktPubBaseIE):
    @classmethod
    def suitable(cls, url): ...
