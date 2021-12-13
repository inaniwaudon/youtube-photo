from . import Image as Image, features as features
from ._util import isDirectory as isDirectory, isPath as isPath
from typing import Any

LAYOUT_BASIC: int
LAYOUT_RAQM: int

class _imagingft_not_installed:
    def __getattr__(self, id) -> None: ...

class ImageFont:
    def getsize(self, text, *args, **kwargs): ...
    def getmask(self, text, mode: str = ..., *args, **kwargs): ...

class FreeTypeFont:
    path: Any
    size: Any
    index: Any
    encoding: Any
    layout_engine: Any
    font_bytes: Any
    font: Any
    def __init__(
        self,
        font: Any | None = ...,
        size: int = ...,
        index: int = ...,
        encoding: str = ...,
        layout_engine: Any | None = ...,
    ) -> None: ...
    def getname(self): ...
    def getmetrics(self): ...
    def getlength(
        self,
        text,
        mode: str = ...,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
    ): ...
    def getbbox(
        self,
        text,
        mode: str = ...,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        stroke_width: int = ...,
        anchor: Any | None = ...,
    ): ...
    def getsize(
        self,
        text,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        stroke_width: int = ...,
    ): ...
    def getsize_multiline(
        self,
        text,
        direction: Any | None = ...,
        spacing: int = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        stroke_width: int = ...,
    ): ...
    def getoffset(self, text): ...
    def getmask(
        self,
        text,
        mode: str = ...,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        stroke_width: int = ...,
        anchor: Any | None = ...,
        ink: int = ...,
    ): ...
    def getmask2(
        self,
        text,
        mode: str = ...,
        fill=...,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        stroke_width: int = ...,
        anchor: Any | None = ...,
        ink: int = ...,
        *args,
        **kwargs
    ): ...
    def font_variant(
        self,
        font: Any | None = ...,
        size: Any | None = ...,
        index: Any | None = ...,
        encoding: Any | None = ...,
        layout_engine: Any | None = ...,
    ): ...
    def get_variation_names(self): ...
    def set_variation_by_name(self, name) -> None: ...
    def get_variation_axes(self): ...
    def set_variation_by_axes(self, axes) -> None: ...

class TransposedFont:
    font: Any
    orientation: Any
    def __init__(self, font, orientation: Any | None = ...) -> None: ...
    def getsize(self, text, *args, **kwargs): ...
    def getmask(self, text, mode: str = ..., *args, **kwargs): ...

def load(filename): ...
def truetype(
    font: Any | None = ...,
    size: int = ...,
    index: int = ...,
    encoding: str = ...,
    layout_engine: Any | None = ...,
): ...
def load_path(filename): ...
def load_default(): ...
