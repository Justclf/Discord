import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!spin'):
        options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']
        selected_option = random.choice(options)
        await message.channel.send('The wheel lands on: ' + selected_option)

client.run('1099383349153378394')
