"""https://github.com/youtube/api-samples/blob/master/python/upload_video.py"""

import argparse
import http.client
import random
import sys
import time
from typing import Any

import httplib2  # type: ignore
from apiclient.discovery import build  # type: ignore
from apiclient.errors import HttpError  # type: ignore
from apiclient.http import MediaFileUpload  # type: ignore
from oauth2client.client import flow_from_clientsecrets  # type: ignore
from oauth2client.file import Storage  # type: ignore
from oauth2client.tools import argparser, run_flow  # type: ignore


class YTUploader:
    httplib2.RETRIES = 1
    MAX_RETRIES = 10
    RETRIABLE_EXCEPTIONS = (
        httplib2.HttpLib2Error,
        IOError,
        http.client.NotConnected,
        http.client.IncompleteRead,
        http.client.ImproperConnectionState,
        http.client.CannotSendRequest,
        http.client.CannotSendHeader,
        http.client.ResponseNotReady,
        http.client.BadStatusLine,
    )

    RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

    MISSING_CLIENT_SECRETS_MESSAGE = """
    WARNING: Please configure OAuth 2.0

    To make this sample run you will need to populate the client_secrets.json file
    with information from the API Console
    https://console.developers.google.com/

    For more information about the client_secrets.json file format, please visit:
    https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
    """

    YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    def __init__(self, auth_path: str = "client_secrets.json") -> None:
        self.CLIENT_SECRETS_FILE = auth_path

    def get_authenticated_service(self, args: argparse.Namespace) -> Any:
        flow = flow_from_clientsecrets(
            self.CLIENT_SECRETS_FILE,
            scope=self.YOUTUBE_UPLOAD_SCOPE,
            message=self.MISSING_CLIENT_SECRETS_MESSAGE,
        )

        storage = Storage("%s-oauth2.json" % sys.argv[0])
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            credentials = run_flow(flow, storage, args)

        return build(
            self.YOUTUBE_API_SERVICE_NAME,
            self.YOUTUBE_API_VERSION,
            http=credentials.authorize(httplib2.Http()),
        )

    def initialize_upload(self, youtube: Any, options: argparse.Namespace) -> str:
        body = {
            "snippet": {
                "title": options.title,
                "description": options.description,
                "tags": None,
                "categoryId": options.category,
            },
            "status": {"privacyStatus": options.privacyStatus},
        }

        insert_request: Any = youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True),
        )

        return self.resumable_upload(insert_request)

    def resumable_upload(self, insert_request: Any) -> str:
        response = None
        error = None
        retry = 0
        while response is None:
            try:
                print("Uploading file...")
                status, response = insert_request.next_chunk()
                if response is not None:
                    if "id" in response:
                        print(
                            "Video id '%s' was successfully uploaded." % response["id"]
                        )
                    else:
                        exit(
                            "The upload failed with an unexpected response: %s"
                            % response
                        )
            except HttpError as e:
                if e.resp.status in self.RETRIABLE_STATUS_CODES:
                    error = "A retriable HTTP error %d occurred:\n%s" % (
                        e.resp.status,
                        e.content,
                    )
                else:
                    raise e
            except self.RETRIABLE_EXCEPTIONS as e:
                error = "A retriable error occurred: %s" % e
            if error is not None:
                print(error)
                retry += 1
                if retry > self.MAX_RETRIES:
                    exit("No longer attempting to retry.")
                max_sleep = 2 ** retry
                sleep_seconds = random.random() * max_sleep
                print("Sleeping %f seconds and then retrying..." % sleep_seconds)
                time.sleep(sleep_seconds)

        # succeeded
        return response["id"]

    def upload(self, file: str, title: str, description: str) -> str:
        argparser.add_argument("--file", default=file)
        argparser.add_argument("--title", default=title)
        argparser.add_argument("--description", default=description)
        argparser.add_argument("--category", default=22)
        argparser.add_argument("--privacyStatus", default="unlisted")
        args = argparser.parse_args()

        youtube: Any = self.get_authenticated_service(args)

        try:
            return self.initialize_upload(youtube, args)
        except HttpError as e:
            raise ConnectionError(
                "An HTTP error %d occurred: %s" % (e.resp.status, e.content)
            )
