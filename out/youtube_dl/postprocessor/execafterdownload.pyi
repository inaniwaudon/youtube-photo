from ..compat import compat_shlex_quote as compat_shlex_quote
from ..utils import PostProcessingError as PostProcessingError, encodeArgument as encodeArgument
from .common import PostProcessor as PostProcessor
from typing import Any

class ExecAfterDownloadPP(PostProcessor):
    exec_cmd: Any
    def __init__(self, downloader, exec_cmd) -> None: ...
    def run(self, information): ...
