# Import necessary libraries
import os
import json
import requests
from flask import Flask, request, Response

# Load environment file, assign variables
from dotenv import load_dotenv
load_dotenv()

api_token = os.environ["API_TOKEN"]
channel_id = os.environ["CHANNEL_ID"]

# Initialize Flask app
app = Flask(__name__)

#
# You don't need to make changes to anything above this line
#

#@app.route('/events', methods=['GET'])
@app.route('/events', methods=['POST'])                                     ### CORRECTION #1
def events_handler():

    request_body_json = request.get_json()

    if "challenge" in request_body_json:

        # Respond to the challenge
        return Response(request_body_json["challenge"]), 200
    else:
        # Store details about the user

        #print(json.dumps(request_body_json))
        evt = request_body_json["event"]
        user_id = evt["user"]["id"]
        #user_name = evt["user"]["real_name_normalized"]
        user_name = evt["user"]["profile"]["real_name_normalized"]          ### CORRECTION #2
        status_text = evt["user"]["profile"]["status_text"]
        status_emoji = evt["user"]["profile"]["status_emoji"]

        # If no full name set, use the username instead
        if user_name == "":
            user_name = evt["user"]["name"]

        # Build the message payload
        build_message(user_id, user_name, status_text, status_emoji)

    # Return a 200 to the event request
    return Response(status=200)


# Build the message payload
def build_message(user_id, user_name, status_text, status_emoji):

    if len(status_text) > 0:
        # If their status contains some text
        message = [{
            "pretext": user_name + " updated their status:",
            "text": status_emoji + " *" + status_text + "*"
        }]
    else:
        # If their status is empty
        message = [{
            "pretext": user_name + " cleared their status",
        }]

    post_update(message)

    return


# Post the actual message to a channel
def post_update(attachments):
    data = {
        "token": api_token,
        "channel": channel_id,
        #"text": json.dumps(attachments, separators=(',', ':'))
        "attachments": json.dumps(attachments, separators=(',', ':')),              ### CORRECTION #4
        "pretty": True
    }

    #print(data["text"])
    #print(json.dumps(attachments, separators=(',', ':')))
    try:
        #r = requests.post("https://slack.com/api/chat.postmessage", data=data)
        r = requests.post("https://slack.com/api/chat.postMessage", data=data)      ### Correction #3
        r.raise_for_status()

        # log Slack API responses
        #print('try')
        print(r.json())

    except requests.exceptions.HTTPError as err:
        # If there's an HTTP error, log the error message
        #print("except")
        print(err)


    return

@app.route('/')
def index():
    return"<h1>Welcome to our server !!</h1>"