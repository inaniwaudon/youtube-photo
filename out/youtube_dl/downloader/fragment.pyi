from ..utils import encodeFilename as encodeFilename, error_to_compat_str as error_to_compat_str, sanitize_open as sanitize_open, sanitized_Request as sanitized_Request
from .common import FileDownloader as FileDownloader
from .http import HttpFD as HttpFD

class HttpQuietDownloader(HttpFD):
    def to_screen(self, *args, **kargs) -> None: ...

class FragmentFD(FileDownloader):
    def report_retry_fragment(self, err, frag_index, count, retries) -> None: ...
    def report_skip_fragment(self, frag_index) -> None: ...
