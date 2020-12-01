import discord

intent = discord.Intents(messages=True, guilds=True, members=True)
client = discord.Client(intents=intent)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    categories = member.guild.categories 
    for category in categories:
        if category.name == "Text Channels":
            for channel in category.channels:
                if channel.name == "general":
                    print("Hola" + str(member))
                    file = discord.File("Hola.gif", filename = "hola.gif")
                    await channel.send("Hola " + str(member.mention))
                    await channel.send(file=file)

client.run('Your token here')