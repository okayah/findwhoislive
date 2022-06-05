# FindWhoisLive
Find streamers that are currently live from a json file.

# Installation:
Go to [releases](https://github.com/okayah/findwhoislive/releases/latest/) and download the latest release.

Unzip the file into a directory of your choice.

After unzipping you want to open ``setup.bat``, this will download what you need for the program to run.

Configure ``config.json`` and ``streamers.json`` to your liking then use ``run.bat``.

# config.json
"Open_In_Browser" - Opens livestreams if they are live. (true/false)

"Find" - Finds certain categories from ``streamers.json`` (["English", "Non-English"])

"Load_Streamers_From" - decides where streamers are loaded from. `Github w/ (30+) PC Streamers` or `File w/ your own streamers.` ("github/file")

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
