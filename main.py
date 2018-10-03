import discord
import datetime
import json

client = discord.Client()


@client.event
async def on_message_edit(before, after):
    msg = '[{}] {} edited their message. \'{}\' -> \'{}\'\n'.format(after.edited_timestamp.strftime("%Y-%m-%d %H:%M:%S"), before.author, before.clean_content, after.clean_content)
    file_name = '{}-{}.txt'.format(datetime.date.today(), after.channel.id)

    with open(file_name, 'a', encoding='utf8') as f:
        f.write(msg)


@client.event
async def on_message(message):
    # If it can get an attachment URL, put it in the message
    # Not the cleanest solution :shrug:
    try:
        msg = '[{}] {}: {} {}\n'.format(message.timestamp.strftime('%Y-%m-%d %H:%M:%S'), message.author, message.clean_content, message.attachments[0].get('url') )
    except IndexError:
        msg = '[{}] {}: {}\n'.format(message.timestamp.strftime('%Y-%m-%d %H:%M:%S'), message.author, message.clean_content)

    file_name = '{}-{}.txt'.format(datetime.date.today(), message.channel.id)

    with open(file_name, 'a', encoding='utf8') as f:
        f.write(msg)

    # If in the log channel, and you're using the logs command
    if message.channel.id == cfg['log_channel'] and message.content.startswith('{}logs'.format(cfg['prefix'])):
        await get_log_file(message)


async def get_log_file(message):
    args = message.content.split()
    # Channel name, date (ISO)

    try:
        if len(args) == 2: # If date not supplied, use today's date
            args.append(datetime.date.today())

        file_name = '{}-{}.txt'.format(args[2], args[1][2:-1])  # Turns channel ID into usable string

        with open(file_name, 'rb') as f:
            await client.send_file(message.channel, f)
    except FileNotFoundError:
        await client.send_message(message.channel, "**Log file not found** for `{}` on `{}`.\nDoes the channel exist? Is the date correct?".format(args[1], args[2]))
    except IndexError:
        await client.send_message(message.channel, "**No channel name supplied**")


with open('config.json') as json_data_file:
    cfg = json.load(json_data_file)

client.run(cfg['token'])
