from ..compat import compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, url_basename as url_basename
from .common import InfoExtractor as InfoExtractor
from .soundcloud import SoundcloudIE as SoundcloudIE

class AudiomackIE(InfoExtractor):
    IE_NAME: str

class AudiomackAlbumIE(InfoExtractor):
    IE_NAME: str
