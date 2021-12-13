from ..utils import clean_html as clean_html, int_or_none as int_or_none, str_or_none as str_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class TelecincoIE(InfoExtractor):
    IE_DESC: str
