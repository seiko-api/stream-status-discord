import discord, os , alive , asyncio , datetime ,pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='!',
  self_bot=True
)



# name = for your status and url = for your twitch link
@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = 
  "JASA MAPPING SA-MP | MURAH - MERIAH | ORDER DM AJA", url = "https://discord.gg/ckfdGT734R"))



alive.alive()
client.run(os.getenv("OTc2NDQ4NDQyNTQzMDA1Njk2.GyAUli.O7Umzf0_iHOj-BVtbCi5ZX2QDZlTdd-Zm3-7dM"), bot=False)
