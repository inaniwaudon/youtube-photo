from ..compat import compat_HTTPError as compat_HTTPError, compat_str as compat_str
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, int_or_none as int_or_none, parse_age_limit as parse_age_limit, str_or_none as str_or_none, try_get as try_get
from .adobepass import AdobePassIE as AdobePassIE
from .common import InfoExtractor as InfoExtractor
from .youtube import YoutubeIE as YoutubeIE

class ViceBaseIE(InfoExtractor): ...

class ViceIE(ViceBaseIE, AdobePassIE):
    IE_NAME: str

class ViceShowIE(ViceBaseIE):
    IE_NAME: str

class ViceArticleIE(ViceBaseIE):
    IE_NAME: str
