import discord
from dotenv import load_dotenv
import os

load_dotenv()

bot = discord.Client()

@bot.event
async def on_ready():
    print('what\'s crackalackin')

@bot.event
async def on_message(msg):
    prefix = 'f;'

    if msg.content.startswith(prefix):
        cmd = msg.content[len(prefix):].split(' ')[0]
        
        if cmd == 'ping':
            await msg.channel.send('pong!')

        if cmd == 'pong':
            await msg.channel.send('ping!')

bot.run(os.getenv('BOT_TOKEN'))
