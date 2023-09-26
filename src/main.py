
import discord
from discord.ext import commands
from discord import app_commands
import com
from config import DISCORD_BOT_TOKEN,KOMEPI_USERID
import logging
# Discordクライアントを初期化
intents = discord.Intents.default()
intents.voice_states = True  # ボイス状態のイベントを受信するために必要
bot = commands.Bot(command_prefix="h!",intents=intents)
user = ""
dm_channel = ""

# ボットが起動したときに実行されるイベント
@bot.event
async def on_ready():
    
    global user
    user = await bot.fetch_user(KOMEPI_USERID)
    logging.debug("user find:{}".format(user))
    logging.debug(f'Logged in as {bot.user.name}')
    #user = client.get_user(KOMEPI_USERID)
    print(bot.voice_clients)
    for channel in bot.get_all_channels():
        print("----------")
        print("チャンネル名：" + str(channel.name))
        print("チャンネルID：" + str(channel.id))
       
        print(dir(channel))
        #print(channel.voice_states)
        print(channel.type)
        print("----------")

# ボイスチャンネル入室イベント
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        # 誰かがボイスチャンネルに入室した場合
        if before.channel is not None:
            await user.send(f'{member.display_name}が{before.channel.name}から退室')
        if after.channel is not None:
            await user.send(f'{member.display_name}が{after.channel.name}に入室')
        #await member.send(f'{member.display_name}がボイスチャンネルに入室しました！')
        
# ボットを実行
@bot.event
async def setup_hook():
    logging.debug(type(bot))
    await bot.add_cog(com.MyCog(bot))

logging.basicConfig(level=logging.DEBUG)
bot.run(DISCORD_BOT_TOKEN)
