import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("소주봇이다. &명령어로 할수 있는 것들을 알아보자")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("&안녕"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("&잘가"):
        await message.channel.send("안녕히가세요")
    if message.content.startswith("&명령어"):
        await message.channel.send("쓸 수 있는 명령어 : ```&안녕, &잘가, &help(노래명령어)```")
    if message.content.startswith("&추가"):
        await message.channel.send("추가")
    if message.content.startswith("&추가"):
        await message.channel.send("추가")

access_token = os.environ[ "BOT_TOKEN" ]
client.run(acess_token)

