from ..compat import compat_urlparse as compat_urlparse
from ..utils import ExtractorError as ExtractorError, InAdvancePagedList as InAdvancePagedList, clean_html as clean_html, get_element_by_id as get_element_by_id, remove_start as remove_start
from .common import InfoExtractor as InfoExtractor

class KuwoBaseIE(InfoExtractor): ...

class KuwoIE(KuwoBaseIE):
    IE_NAME: str
    IE_DESC: str

class KuwoAlbumIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class KuwoChartIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class KuwoSingerIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    PAGE_SIZE: int

class KuwoCategoryIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class KuwoMvIE(KuwoBaseIE):
    IE_NAME: str
    IE_DESC: str
