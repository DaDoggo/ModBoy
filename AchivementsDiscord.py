import disnake
from disnake.ext import commands

client = disnake.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


bot = commands.Bot(
    command_prefix="/",
    sync_commands_debug=True,
    sync_commands=False
)

@bot.slash_command(description="Makes your message capslock")
async def yell(inter, msg: str):
    await inter.response.send_message(msg.upper())

client.run(
    "MTAyNzc5NDMyMDU4MzAzNjk1OA.GOIkWY.RXA7IT3p7gUfy0rJHf-95ivpajmYsyBdtzc5uE")
