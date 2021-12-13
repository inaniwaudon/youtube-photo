from ..compat import compat_urllib_error as compat_urllib_error
from ..utils import DownloadError as DownloadError, urljoin as urljoin
from .fragment import FragmentFD as FragmentFD

class DashSegmentsFD(FragmentFD):
    FD_NAME: str
    def real_download(self, filename, info_dict): ...
