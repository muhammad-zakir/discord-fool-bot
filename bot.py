import discord
import io
import os
import requests

from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True


class MyClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="his own existential crisis"))
        print('------')
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hi'):
            reply_message = "Hi fool, I'm Chakcha A.K.A Fool the Bot. I'm here trying to help everyone in this Server. "
            reply_message += "You can try to ask my help with using '!' prefix "
            reply_message += "before entering the command that you wishes to use." + '\n' + '\n'
            reply_message += "Here's the list of my currently available commands:" + '\n'
            reply_message += "- hello" + '\n'
            reply_message += "- sup"

            await message.reply(reply_message, mention_author=True)

        if message.content.startswith('!hello'):
            reply_message = 'Hello, fool!'
            await message.reply(reply_message, mention_author=True)

        if message.content.startswith('!sup'):
            reply_message = 'Did you just tried chit - chatting with a bot? Are you that bored, fool?'
            await message.reply(reply_message, mention_author=True)

        if message.content.startswith('!meme'):
            meme_fetcher_url = 'https://meme-api.com/gimme'
            filename = 'meme.jpg'
            reply_message = "Here's a meme for you, fool"

            meme = requests.get(meme_fetcher_url).json()
            raw_meme_picture = requests.get(meme['url']).content
            meme_picture = io.BytesIO(raw_meme_picture)
            file = discord.File(meme_picture, filename=filename)

            await message.reply(reply_message, mention_author=True, file=file)
            return


load_dotenv()
token = os.getenv('DISCORD_BOT_TOKEN')

client = MyClient(intents=intents)
client.run(token)
