from ..compat import compat_os_name as compat_os_name
from ..utils import XAttrMetadataError as XAttrMetadataError, XAttrUnavailableError as XAttrUnavailableError, hyphenate_date as hyphenate_date, write_xattr as write_xattr
from .common import PostProcessor as PostProcessor

class XAttrMetadataPP(PostProcessor):
    def run(self, info): ...
