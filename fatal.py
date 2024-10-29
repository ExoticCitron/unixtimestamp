import discord,os, asyncio
from discord import app_commands
 # Unfinished draft [1] for https://exo-devs.tech/ unix compatibility
client = commands.Bot(
    command_prefix = commands.when_mentioned,
    intents = discord.Intents.all()
)

@client.event
async def on_ready():
    print(f"{client.user} is online")


def convert_to_unix_time(date: datetime.datetime, days: int, hours: int, minutes: int, seconds: int) -> str:
    end_date = date + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    date_tuple = (end_date.year, end_date.month, end_date.day, end_date.hour, end_date.minute, end_date.second)
    return f'<t:{int(time.mktime(datetime.datetime(*date_tuple).timetuple()))}:R>'

@client.tree.command(name="notification", descrption = "notification")
async def notification(interaction: discord.Interaction, channel: discord.VoiceCHannel, time: convert_to_unix_time(date, days, hours, minutes, seconds)):
    timestampembed = discord.Embed(
        tite="New meeting!",
        descrption=f"At: {time}\nChannel: {channel.mention}",
        color = 0x000000
    )
    timestampEmbed.set_footer(text=f"Requested by {interaction.user.name}")


if __name__ == '__main__':
    client.run('')
