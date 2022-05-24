import discord
from discord.ext import commands
import os, time
from dotenv import load_dotenv

# Load token

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

chihiro = commands.Bot(command_prefix=".", intents=intents)

@chihiro.command(name="ping")
async def ping(ctx: commands.Context):
    before = time.monotonic()
    msg = await ctx.send("Ping...")
    await msg.edit(content=f"Ping: `{int((time.monotonic() - before) * 1000)}ms`")

@chihiro.event
async def on_ready():
    status_ch = chihiro.get_channel(978613069976588298)
    await status_ch.send(f"Bot {chihiro.user.name} activo")
    print(f"Bot ({chihiro.user.name} - [{chihiro.user.id}])")

TOKEN = os.getenv("DISCORD_TOKEN") 
chihiro.run(TOKEN)

