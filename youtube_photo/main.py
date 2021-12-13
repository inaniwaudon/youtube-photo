#!/usr/bin/env python
import argparse
import os
import typing
from shutil import get_terminal_size

import youtube_photo

from .download import Downloader
from .upload import Uploader

ArgList = typing.Optional[typing.List[str]]


class Formatter(
    argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter
):
    """Customized formatter class"""

    pass


def check_file(path: str) -> str:
    if os.path.isfile(path):
        return path
    else:
        raise FileNotFoundError("'{}' is not found.".format(path))


def check_dir(path: str) -> str:
    if os.path.isdir(path):
        return path
    else:
        raise FileNotFoundError("'{}' is not found.".format(path))


def func_download(ns: argparse.Namespace) -> None:
    d = Downloader()
    d.download(ns.video_id, ns.img_dir)


def func_upload(ns: argparse.Namespace) -> None:
    u = Uploader()
    print(u.upload(ns.img_dir, ns.auth_path))


def parse_args(test: ArgList = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="ytp",
        formatter_class=(
            lambda prog: Formatter(
                prog,
                **{
                    "width": get_terminal_size(fallback=(120, 50)).columns,
                    "max_help_position": 40,
                },
            )
        ),
        description=(
            "Generating a H.264 video from "
            "the specified pictures and upload to YouTube."
        ),
    )

    parser.set_defaults(func=lambda _: parser.print_usage())

    subparsers = parser.add_subparsers()

    upload_parser = subparsers.add_parser(
        "upload",
        aliases=["up"],
        help="upload images",
        formatter_class=(
            lambda prog: Formatter(
                prog,
                **{
                    "width": get_terminal_size(fallback=(120, 50)).columns,
                    "max_help_position": 40,
                },
            )
        ),
    )
    upload_parser.add_argument(
        "-d",
        "--img_dir",
        metavar="DIR",
        type=check_dir,
        help="upload dir",
        default="img",
    )
    upload_parser.add_argument(
        "-a",
        "--auth_path",
        metavar="JSON",
        type=check_file,
        default="client_secrets.json",
        help="credencial path",
    )
    upload_parser.set_defaults(func=func_upload)

    download_parser = subparsers.add_parser(
        "download",
        aliases=["dl"],
        help="download images",
        formatter_class=(
            lambda prog: Formatter(
                prog,
                **{
                    "width": get_terminal_size(fallback=(120, 50)).columns,
                    "max_help_position": 50,
                },
            )
        ),
    )
    download_parser.add_argument(
        "video_id", metavar="ID", type=str, help="target youtube video id"
    )
    download_parser.add_argument(
        "-d",
        "--img_dir",
        metavar="DIR",
        type=str,
        help="dir contains pictures",
        default="download-img",
    )
    download_parser.set_defaults(func=func_download)

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="%(prog)s {}".format(youtube_photo.__version__),
    )
    if test is not None:
        return parser.parse_args(test)
    else:
        return parser.parse_args()


def _main(test: ArgList = None) -> None:
    args = parse_args(test=test)
    args.func(args)


def main(test: ArgList = None) -> None:
    try:
        _main(test)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
