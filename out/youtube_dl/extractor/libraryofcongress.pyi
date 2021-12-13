from ..utils import determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, parse_filesize as parse_filesize
from .common import InfoExtractor as InfoExtractor

class LibraryOfCongressIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
