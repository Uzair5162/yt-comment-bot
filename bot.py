# -*- coding: utf-8 -*-

# Sample Python code for youtube.comments.update
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)


    request = youtube.comments().update(
        part="snippet",
        body={
          "id": "UgyZ-rPsAprQL2-dKeh4AaABAg",
          "snippet": {
            numLike = "likeCount"
            "textOriginal": numLike
          }
        }
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()