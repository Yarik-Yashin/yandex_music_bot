from yandex_music.client import Client
from TOKEN import mail, password
import discord

user = Client.from_credentials(mail, password)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run('my token goes here')
