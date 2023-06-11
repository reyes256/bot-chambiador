from dotenv import load_dotenv
import os, discord

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is now running')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} dijo: {user_message} en {channel}')

    if message.content.startswith('>hola'):
        await message.channel.send('qp perro')

    if message.content.startswith('>help'):
        await message.channel.send('Todavia no hay comandos amigo')

client.run(os.getenv("DISCORD_TOKEN"))