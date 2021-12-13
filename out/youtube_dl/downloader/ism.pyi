from ..compat import compat_Struct as compat_Struct, compat_urllib_error as compat_urllib_error
from .fragment import FragmentFD as FragmentFD
from typing import Any

u8: Any
u88: Any
u16: Any
u1616: Any
u32: Any
u64: Any
s88: Any
s16: Any
s1616: Any
s32: Any
unity_matrix: Any
TRACK_ENABLED: int
TRACK_IN_MOVIE: int
TRACK_IN_PREVIEW: int
SELF_CONTAINED: int

def box(box_type, payload): ...
def full_box(box_type, version, flags, payload): ...
def write_piff_header(stream, params) -> None: ...
def extract_box_data(data, box_sequence): ...

class IsmFD(FragmentFD):
    FD_NAME: str
    def real_download(self, filename, info_dict): ...
