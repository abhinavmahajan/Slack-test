## End goal

This app makes use of Slack's Events API. It listens for a user's Status Changes in the `user_change` event, and then posts a message containing their custom status to the #statuses channel in their Slack workspace.

The final design should look like this:

![final result](Final%20Result.png)

## Files

You will need to create a `.env` file and modify the two values to point to a channel on your workspace and the user token generated when you install your Slack app to your test workspace. It should look like this:
CHANNEL_ID=Cxxxxxx
API_TOKEN=xpop-dscdscds-sdvffdv-dfvdfvdf


## Setup

You will need to host your Python Flask application.  You can do this on a platform such as [Heroku](https://devcenter.heroku.com/categories/python-support) with a free account, on any other Python hosting platform you are familiar with (e.g. [Glitch](https://glitch.com/~flask-hello-world)), or you can host the app locally using [ngrok](https://ngrok.com/download).  The rest of the steps make use of `ngrok`.

#### Dependencies

This application was developed on Python version `3.7`

You can use either [pip](https://packaging.python.org/tutorials/installing-packages/#id21) or [pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-packages-for-your-project) to install the project's dependencies.  `flask`, `python-dotenv`, and `requests` are all required to be installed and availble to be imported into your project.

#### Monitoring network requests

If you decide to use *ngrok* to host the project locally, download and unzip [ngrok](https://ngrok.com/download). In the Terminal window pointing to the unzipped contents, type:

```
./ngrok http 5000
```

This starts an app called *ngrok*, which will allow your local flask app to connect to Slack. Port `5000` is the default for a Flask app.  This app is needed if you are hosting your code/app on your local machine so that Slack can send your app reuqests.  You will see inbound requests appearing in your terminal.

Once ngrok is running, you can also view more detailed network logs at  http://127.0.0.1:4040

#### Running/restarting the app

In the Terminal window that points to your working directory, type:

```
flask run
```

If you are hosting your Flask application in a cloud hosting platform, it may automatically be running when you deploy the code.  Check the server logs to make sure this is the case.

#### Create Slack application

1. Create a new Slack workspace for testing: https://slack.com/create
2. In that workspace, create a new public channel.
3. Right-click on the channel's name in the sidebar and copy the channel link. Paste the ID from that link (which looks like `C0123ABC`) into the `.env` file next to the `CHANNEL_ID` variable.  You will need to rename the file `.env-sample` to `.env`.
4. Create a new Slack app and assign it to your newly created workspace: https://api.slack.com/apps
5. Go to the app's **OAuth & Permission** page and add the `chat:write:bot` and `users:read` scopes. Save your changes.
6. At the top of that page, press the green **Install App to Workspace** button to install it on your new workspace.
7. After authorizing the app, you'll see an **OAuth Access Token** that starts with `xoxp`. Copy that token and paste it into the `.env` file next to the `API_TOKEN` variable.
8. Save the changes to your `.env` file.
9. Be sure your flask app is running.  This can be on your local machine using `ngrok` or on another hosting platform.  Make sure the app flask app is running and listening for requests using `flask run`.
10. Go to the app's **Event Subscriptions** page and enable the feature.
11. Copy your app's server or ngrok URL and add `/events` to the end of it. Paste that full URL as the **Request URL**.
12. Subscribe to the `user_change` event on the same page and save the settings.

## Testing your Changes

Whenever you make changes to the code, you will need to restart your flask app.

#### Triggering `user_change` events

As long as the app is running, [change your Slack status](https://get.slack.help/hc/en-us/articles/201864558-Set-your-Slack-status-and-availability) to something new in order for an event to be triggered.

## Links to help you out
* [Building Slack apps](https://api.slack.com/slack-apps)
* [Events API](https://api.slack.com/events-api)
* [`user_change` event](https://api.slack.com/events/user_change)
