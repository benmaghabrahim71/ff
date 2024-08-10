
import discord
from discord.ext import commands

TOKEN = 'MTI3MTc4NzcxMDAyMDg0NTYwMA.GJ58Hl.dwc_TQV57NU2F4f3p_feBKGEMu0yQWNUznVAps'
SOURCE_CHANNEL_ID = 1271507968348786699  # Replace with your source channel ID
DEST_CHANNEL_ID = 1271507840686883038  # Replace with your destination channel ID
ROLE_ID = 1149400246447771819  # Replace with your role ID

intents = discord.Intents.default()
intents.message_content = True  # Required for accessing message content
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Ignore bot messages
    if message.author.bot:
        return
    
    # Check if the message is from the source channel
    if message.channel.id == SOURCE_CHANNEL_ID:
        dest_channel = bot.get_channel(DEST_CHANNEL_ID)
        if dest_channel:
            try:
                # Transfer the message to the destination channel
                await dest_channel.send(f'Message from {message.author}: {message.content}')
                
                # Add the specified role to the message author
                role = discord.utils.get(message.guild.roles, id=ROLE_ID)
                if role:
                    await message.author.add_roles(role)
                else:
                    print('Role not found')
            except Exception as e:
                print(f'Error transferring message: {e}')
        else:
            print('Destination channel not found')
    
    # Process other commands if you have any
    await bot.process_commands(message)

bot.run(TOKEN)
