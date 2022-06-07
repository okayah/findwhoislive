# FindWhoisLive
Find streamers that are currently live from a json file.

# Installation:
Go to [releases](https://github.com/okayah/findwhoislive/releases/latest/) and download the latest release.

Unzip the file into a directory of your choice.

After unzipping you want to open ``setup.bat``, this will download what you need for the program to run.

Configure ``config.json`` and ``streamers.json`` to your liking then use ``run.bat``.

# config.json
"simple_method" - Bypasses the need for Authentication, shows if the streamer is live or not. (true/false)

"api_method" - Requires client_id & client_secret. https://dev.twitch.tv/docs/api (true/false)

`Authentication`

"client_id" - client ID for your application.

"client_secret" - client secret for your application.

`Settings`

"Open_In_Browser" - Opens livestreams if they are live. (true/false)

"Find_By_Game" - only find streamers play the game specified, must be exactly how twitch names the category. ("Game Name")

# streamers.json
To make your own categories, you may need slight json file syntax knowledge.

You can use a [JsonChecker](https://jsonchecker.com/) to check for errors in your file.

{
  "name": {
    "streamer's link": "scname/scid",
    "streamer's link 2": "scname/scid"
  }
}

Once you have made your own section you need to define it in `"Find"` which you can find in ``config.json``.
