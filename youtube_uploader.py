import os, sys, time, random
import http.client
import httplib2

from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

httplib2.RETRIES = 1
MAX_RETRIES = 10
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error,
	IOError, http.client.NotConnected,
	http.client.IncompleteRead, http.client.ImproperConnectionState,
	http.client.CannotSendRequest, http.client.CannotSendHeader,
	http.client.ResponseNotReady, http.client.BadStatusLine)
	
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
CLIENT_SECRETS_FILE = "client_secrets.json"

MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:
	%s
with information from the API Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__), CLIENT_SECRETS_FILE))

YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def get_authenticated_service(args) :
	flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
								   scope=YOUTUBE_UPLOAD_SCOPE,
								   message=MISSING_CLIENT_SECRETS_MESSAGE)

	storage = Storage("%s-oauth2.json" % sys.argv[0])
	credentials = storage.get()

	if credentials is None or credentials.invalid:
		credentials = run_flow(flow, storage, args)

	return build(YOUTUBE_API_SERVICE_NAME,
				 YOUTUBE_API_VERSION,
				 http=credentials.authorize(httplib2.Http()))


def initialize_upload(youtube, options):
	body = {
		"snippet" : {
			"title" : options.title,
			"description" : options.description,
			"tags" : None,
			"categoryId" : options.category
		}, 
		"status" : { "privacyStatus" : options.privacyStatus }
	}

	insert_request = youtube.videos().insert(
		part=",".join(body.keys()),
		body=body,
		media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
	)
	
	return resumable_upload(insert_request)


def resumable_upload(insert_request) :
	response = None
	error = None
	retry = 0
	while response is None:
		try:
			print("Uploading file...")
			status, response = insert_request.next_chunk()
			if response is not None:
				if 'id' in response:
					print("Video id '%s' was successfully uploaded." % response["id"])
				else:
					exit("The upload failed with an unexpected response: %s" % response)
		except HttpError as e:
			if e.resp.status in RETRIABLE_STATUS_CODES:
				error = "A retriable HTTP error %d occurred:\n%s" % \
						(e.resp.status, e.content)
			else:
				raise
		except RETRIABLE_EXCEPTIONS as e:
			error = "A retriable error occurred: %s" % e
		if error is not None:
			print(error)
			retry += 1
			if retry > MAX_RETRIES:
			  exit("No longer attempting to retry.")
			max_sleep = 2 ** retry
			sleep_seconds = random.random() * max_sleep
			print("Sleeping %f seconds and then retrying..." % sleep_seconds)
			time.sleep(sleep_seconds)

	# succeeded
	return response["id"]


def upload(file, title, description) :
	argparser.add_argument("--file", default=file)
	argparser.add_argument("--title", default=title)
	argparser.add_argument("--description", default=description)
	argparser.add_argument("--category", default=22)
	argparser.add_argument("--privacyStatus", default="unlisted")
	args = argparser.parse_args()

	youtube = get_authenticated_service(args)

	try:
		return initialize_upload(youtube, args)
	except HttpError as e:
		print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))