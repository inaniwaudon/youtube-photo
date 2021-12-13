from . import Image as Image, ImageColor as ImageColor, ImageFont as ImageFont
from typing import Any

class ImageDraw:
    palette: Any
    im: Any
    draw: Any
    mode: Any
    ink: Any
    fontmode: str
    fill: int
    font: Any
    def __init__(self, im, mode: Any | None = ...) -> None: ...
    def getfont(self): ...
    def arc(self, xy, start, end, fill: Any | None = ..., width: int = ...) -> None: ...
    def bitmap(self, xy, bitmap, fill: Any | None = ...) -> None: ...
    def chord(
        self,
        xy,
        start,
        end,
        fill: Any | None = ...,
        outline: Any | None = ...,
        width: int = ...,
    ) -> None: ...
    def ellipse(
        self, xy, fill: Any | None = ..., outline: Any | None = ..., width: int = ...
    ) -> None: ...
    def line(
        self, xy, fill: Any | None = ..., width: int = ..., joint: Any | None = ...
    ): ...
    def shape(
        self, shape, fill: Any | None = ..., outline: Any | None = ...
    ) -> None: ...
    def pieslice(
        self,
        xy,
        start,
        end,
        fill: Any | None = ...,
        outline: Any | None = ...,
        width: int = ...,
    ) -> None: ...
    def point(self, xy, fill: Any | None = ...) -> None: ...
    def polygon(
        self, xy, fill: Any | None = ..., outline: Any | None = ...
    ) -> None: ...
    def regular_polygon(
        self,
        bounding_circle,
        n_sides,
        rotation: int = ...,
        fill: Any | None = ...,
        outline: Any | None = ...,
    ) -> None: ...
    def rectangle(
        self, xy, fill: Any | None = ..., outline: Any | None = ..., width: int = ...
    ) -> None: ...
    def rounded_rectangle(
        self,
        xy,
        radius: int = ...,
        fill: Any | None = ...,
        outline: Any | None = ...,
        width: int = ...,
    ): ...
    def text(
        self,
        xy,
        text,
        fill: Any | None = ...,
        font: Any | None = ...,
        anchor: Any | None = ...,
        spacing: int = ...,
        align: str = ...,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        stroke_width: int = ...,
        stroke_fill: Any | None = ...,
        embedded_color: bool = ...,
        *args,
        **kwargs
    ): ...
    def multiline_text(
        self,
        xy,
        text,
        fill: Any | None = ...,
        font: Any | None = ...,
        anchor: Any | None = ...,
        spacing: int = ...,
        align: str = ...,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        stroke_width: int = ...,
        stroke_fill: Any | None = ...,
        embedded_color: bool = ...,
    ) -> None: ...
    def textsize(
        self,
        text,
        font: Any | None = ...,
        spacing: int = ...,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        stroke_width: int = ...,
    ): ...
    def multiline_textsize(
        self,
        text,
        font: Any | None = ...,
        spacing: int = ...,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        stroke_width: int = ...,
    ): ...
    def textlength(
        self,
        text,
        font: Any | None = ...,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        embedded_color: bool = ...,
    ): ...
    def textbbox(
        self,
        xy,
        text,
        font: Any | None = ...,
        anchor: Any | None = ...,
        spacing: int = ...,
        align: str = ...,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        stroke_width: int = ...,
        embedded_color: bool = ...,
    ): ...
    def multiline_textbbox(
        self,
        xy,
        text,
        font: Any | None = ...,
        anchor: Any | None = ...,
        spacing: int = ...,
        align: str = ...,
        direction: Any | None = ...,
        features: Any | None = ...,
        language: Any | None = ...,
        stroke_width: int = ...,
        embedded_color: bool = ...,
    ): ...

def Draw(im, mode: Any | None = ...): ...

Outline: Any

def getdraw(im: Any | None = ..., hints: Any | None = ...): ...
def floodfill(
    image, xy, value, border: Any | None = ..., thresh: int = ...
) -> None: ...
