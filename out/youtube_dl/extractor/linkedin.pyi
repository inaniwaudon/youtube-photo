from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class LinkedInLearningBaseIE(InfoExtractor): ...

class LinkedInLearningIE(LinkedInLearningBaseIE):
    IE_NAME: str

class LinkedInLearningCourseIE(LinkedInLearningBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
