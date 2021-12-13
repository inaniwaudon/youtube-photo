from . import Image as Image
from typing import Any

modules: Any

def check_module(feature): ...
def version_module(feature): ...
def get_supported_modules(): ...

codecs: Any

def check_codec(feature): ...
def version_codec(feature): ...
def get_supported_codecs(): ...

features: Any

def check_feature(feature): ...
def version_feature(feature): ...
def get_supported_features(): ...
def check(feature): ...
def version(feature): ...
def get_supported(): ...
def pilinfo(out: Any | None = ..., supported_formats: bool = ...) -> None: ...
