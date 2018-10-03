# Discord Chat Logger
A super simple Discord chat logging bot, built on (pre-rewrite) [discord.py](https://github.com/Rapptz/discord.py/). Track and download logs from within Discord.

I made this because I wasn't satisfied with any of the other logging bots - none of them had all the features I wanted - namely an easy way to retrieve logs _within_ Discord. And because writing a logging bot is pretty easy, I wrote my own from scratch.

### Features
- Text file based logging
- No file server
- Tracks edited messages
- Retrieve logs without leaving Discord

~~The only issue currently is that it doesn't log images. I don't need to log images for my use, but I might add it at some point.~~ It kind of logs images - it doesn't keep the file but keeps the link now. Keeping the file would use too much space for me. I don't really develop this bot unless it's broken by a discord change so don't expect anything.


## Setup
- Clone this repository: `git clone https://github.com/jaffacakes6/Discord-Chat-Logger.git`.
- Navigate to the cloned repo.
- Make a copy of `config.example.json` in the same folder called `config.json`.
	- Open the file and add your values.
- Install dependencies: `pip install -r requirements.txt`.
- Add the bot to your server.
- Run the bot: `python main.py`

## Usage
By default, use `[logs <channel name> <date>` in the channel specified in `config.json` to retrieve the logs for that day. You can also omit the date to retrieve the logs for today.

The channel name should be exactly as seen in the channel selector. The date should be ISO format (e.g. 1970-01-01).
