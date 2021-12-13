from ..compat import compat_HTTPError as compat_HTTPError
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, smuggle_url as smuggle_url, try_get as try_get, unsmuggle_url as unsmuggle_url
from .common import InfoExtractor as InfoExtractor

class LimelightBaseIE(InfoExtractor): ...

class LimelightMediaIE(LimelightBaseIE):
    IE_NAME: str

class LimelightChannelIE(LimelightBaseIE):
    IE_NAME: str

class LimelightChannelListIE(LimelightBaseIE):
    IE_NAME: str
