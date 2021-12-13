from ..compat import compat_xpath as compat_xpath
from ..utils import int_or_none as int_or_none, parse_duration as parse_duration, smuggle_url as smuggle_url, unsmuggle_url as unsmuggle_url, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class MicrosoftVirtualAcademyBaseIE(InfoExtractor): ...

class MicrosoftVirtualAcademyIE(MicrosoftVirtualAcademyBaseIE):
    IE_NAME: str
    IE_DESC: str

class MicrosoftVirtualAcademyCourseIE(MicrosoftVirtualAcademyBaseIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...
