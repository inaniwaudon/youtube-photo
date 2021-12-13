from ..compat import compat_struct_pack as compat_struct_pack, compat_urllib_error as compat_urllib_error, compat_urlparse as compat_urlparse
from ..utils import parse_m3u8_attributes as parse_m3u8_attributes, update_url_query as update_url_query
from .external import FFmpegFD as FFmpegFD
from .fragment import FragmentFD as FragmentFD

can_decrypt_frag: bool

class HlsFD(FragmentFD):
    FD_NAME: str
    @staticmethod
    def can_download(manifest, info_dict): ...
    def real_download(self, filename, info_dict): ...
