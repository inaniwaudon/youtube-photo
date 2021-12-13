from ..compat import compat_str as compat_str, compat_urllib_error as compat_urllib_error
from ..utils import ContentTooShortError as ContentTooShortError, XAttrMetadataError as XAttrMetadataError, XAttrUnavailableError as XAttrUnavailableError, encodeFilename as encodeFilename, int_or_none as int_or_none, sanitize_open as sanitize_open, sanitized_Request as sanitized_Request, write_xattr as write_xattr
from .common import FileDownloader as FileDownloader
from typing import Any

class HttpFD(FileDownloader):
    source_error: Any
    def real_download(self, filename, info_dict): ...
