from ..compat import compat_setenv as compat_setenv, compat_str as compat_str
from ..postprocessor.ffmpeg import EXT_TO_OUT_FORMATS as EXT_TO_OUT_FORMATS, FFmpegPostProcessor as FFmpegPostProcessor
from ..utils import check_executable as check_executable, cli_bool_option as cli_bool_option, cli_configuration_args as cli_configuration_args, cli_option as cli_option, cli_valueless_option as cli_valueless_option, encodeArgument as encodeArgument, encodeFilename as encodeFilename, handle_youtubedl_headers as handle_youtubedl_headers, is_outdated_version as is_outdated_version
from .common import FileDownloader as FileDownloader

class ExternalFD(FileDownloader):
    def real_download(self, filename, info_dict): ...
    @classmethod
    def get_basename(cls): ...
    @property
    def exe(self): ...
    @classmethod
    def available(cls): ...
    @classmethod
    def supports(cls, info_dict): ...
    @classmethod
    def can_download(cls, info_dict): ...

class CurlFD(ExternalFD):
    AVAILABLE_OPT: str

class AxelFD(ExternalFD):
    AVAILABLE_OPT: str

class WgetFD(ExternalFD):
    AVAILABLE_OPT: str

class Aria2cFD(ExternalFD):
    AVAILABLE_OPT: str

class HttpieFD(ExternalFD):
    @classmethod
    def available(cls): ...

class FFmpegFD(ExternalFD):
    @classmethod
    def supports(cls, info_dict): ...
    @classmethod
    def available(cls): ...

class AVconvFD(FFmpegFD): ...

def list_external_downloaders(): ...
def get_external_downloader(external_downloader): ...
