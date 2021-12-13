import base64
import cookielib as compat_cookiejar
import Cookie as compat_cookies
import htmlentitydefs as compat_html_entities
import httplib as compat_http_client
import BaseHTTPServer as compat_http_server
import urllib2 as compat_urllib_error
import urllib as compat_urllib_parse
import urllib2 as compat_urllib_request
import urllib as compat_urllib_response
import urlparse as compat_urlparse
import getpass
import itertools
import shlex
import shutil
import socket
import struct
import xml.etree.ElementTree
from HTMLParser import HTMLParser as compat_HTMLParser
from html.parser import HTMLParseError as compat_HTMLParseError
from itertools import izip as compat_zip
from shlex import quote as compat_shlex_quote
from tokenize import tokenize as compat_tokenize_tokenize
from typing import Any, NamedTuple
from urllib import urlretrieve as compat_urlretrieve
from urllib.parse import parse_qs as compat_parse_qs, unquote as compat_urllib_parse_unquote, unquote_plus as compat_urllib_parse_unquote_plus, unquote_to_bytes as compat_urllib_parse_unquote_to_bytes, urlencode as compat_urllib_parse_urlencode
from urllib.request import DataHandler as compat_urllib_request_DataHandler
from urllib2 import HTTPError as compat_HTTPError
from urlparse import urlparse as compat_urllib_parse_urlparse
from xml.etree.ElementTree import _ElementInterface as compat_etree_Element
from xml.parsers.expat import ExpatError as compat_xml_parse_error

compat_cookiejar_Cookie = compat_cookiejar.Cookie
compat_cookies_SimpleCookie = compat_cookies.SimpleCookie
compat_html_entities_html5: Any

class compat_HTMLParseError(Exception): ...

compat_subprocess_get_DEVNULL: Any
compat_str = unicode
compat_str = str

class compat_urllib_request_DataHandler(compat_urllib_request.BaseHandler):
    def data_open(self, req): ...
compat_basestring = basestring
compat_basestring = str
compat_chr = unichr
compat_chr = chr
etree = xml.etree.ElementTree

class _TreeBuilder(etree.TreeBuilder):
    def doctype(self, name, pubid, system) -> None: ...

def compat_etree_fromstring(text): ...
compat_etree_register_namespace = etree.register_namespace
compat_xpath: Any
compat_os_name: Any

def compat_shlex_quote(s): ...
compat_shlex_split = shlex.split

def compat_ord(c): ...

compat_getenv: Any
compat_expanduser: Any

def compat_setenv(key, value, env=...) -> None: ...
def compat_realpath(path): ...

compat_realpath: Any

def compat_print(s) -> None: ...
compat_getpass = getpass.getpass
compat_input = raw_input
compat_input = input

def compat_kwargs(kwargs): ...

compat_kwargs: Any
compat_numeric_types: Any
compat_integer_types: Any
compat_socket_create_connection = socket.create_connection

def workaround_optparse_bug9161(): ...
compat_get_terminal_size = shutil.get_terminal_size

class _terminal_size(NamedTuple):
    columns: Any
    lines: Any
compat_itertools_count = itertools.count

def compat_struct_pack(spec, *args): ...
def compat_struct_unpack(spec, *args): ...

class compat_Struct(struct.Struct):
    def __init__(self, fmt) -> None: ...
compat_struct_pack = struct.pack
compat_struct_unpack = struct.unpack

class compat_Struct(struct.Struct):
    def unpack(self, string): ...
compat_Struct = struct.Struct
compat_zip = zip
compat_b64decode = base64.b64decode

def compat_ctypes_WINFUNCTYPE(*args, **kwargs): ...
