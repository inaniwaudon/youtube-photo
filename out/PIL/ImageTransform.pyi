from . import Image as Image
from typing import Any

class Transform(Image.ImageTransformHandler):
    data: Any
    def __init__(self, data) -> None: ...
    def getdata(self): ...
    def transform(self, size, image, **options): ...

class AffineTransform(Transform):
    method: Any

class ExtentTransform(Transform):
    method: Any

class QuadTransform(Transform):
    method: Any

class MeshTransform(Transform):
    method: Any
