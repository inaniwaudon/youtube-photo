from ..compat import compat_str as compat_str
from ..utils import check_executable as check_executable, encodeArgument as encodeArgument, encodeFilename as encodeFilename, get_exe_version as get_exe_version
from .common import FileDownloader as FileDownloader

def rtmpdump_version(): ...

class RtmpFD(FileDownloader):
    def real_download(self, filename, info_dict): ...
