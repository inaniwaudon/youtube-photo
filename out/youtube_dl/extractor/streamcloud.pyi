from ..utils import ExtractorError as ExtractorError, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class StreamcloudIE(InfoExtractor):
    IE_NAME: str
