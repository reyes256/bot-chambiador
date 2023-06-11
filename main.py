from dotenv import load_dotenv
import os, subprocess, discord

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

    if message.content.startswith('>cmd'):
        message_array = user_message.split()

        if len(message_array) == 1:
            await message.channel.send('Faltan argumentos')
            return

        message_array.pop(0)

        cmd = ""
        for arg in message_array:
            cmd += arg + " "
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(result.stdout)

        await message.channel.send(result.stdout)

    if message.content.startswith('>hola'):
        await message.channel.send('qp perro')

    if message.content.startswith('>help'):
        await message.channel.send('Todavia no hay comandos amigo')

client.run(os.getenv("DISCORD_TOKEN"))