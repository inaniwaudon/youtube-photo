from ..utils import clean_html as clean_html, clean_podcast_url as clean_podcast_url, int_or_none as int_or_none, str_or_none as str_or_none
from .common import InfoExtractor as InfoExtractor

class IHeartRadioBaseIE(InfoExtractor): ...

class IHeartRadioIE(IHeartRadioBaseIE):
    IENAME: str

class IHeartRadioPodcastIE(IHeartRadioBaseIE):
    IE_NAME: str
