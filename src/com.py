import discord
from discord import app_commands
from discord.ext import commands
import logging

from views import SettingSelectView
#from api import NotificationSetting

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        logging.debug("successfully loaded : post forum")
        await self.bot.tree.sync()
        logging.debug("sync")
    
    #@app_commands.command(name="ping", description="this is ping command.")
    #async def pingpong_bot(self, ctx: discord.Interaction):
    #    await ctx.response.send_message("called new ping command.")
    #
    #@app_commands.command(name="set_notification", description="this is setting")
    #async def setting_get_notification(self, ctx: discord.Interaction, flg: bool):
    #    logging.debug("flg:{}".format(flg))
    #    logging.debug(ctx)
    #    logging.debug(dir(ctx))
    #    logging.debug(ctx.user)
    #    await ctx.user.send("{name}はコマンドで{result}を選びました".format(name=ctx.user.name,result=flg))
    #    
    #    await ctx.response.send_message("あなたは{flg}を選びました")
    
    @app_commands.command(name="select_chan", description="通知を受け取るチャンネルを追加・削除します。")
    async def select_channel(self, ctx: discord.Interaction):
        view = SettingSelectView()
        await ctx.response.send_message("menu",view=view)
    
#    @app_commands.command(name="watch_setting",description="現在の通知を受け取るチャンネルを表示します。")
#    async def watch_setting(self, ctx: discord.Interaction):
#        userid = ctx.user.id
#        notification_setting = NotificationSetting()
#        settings = notification_setting.get_channels_by_userid(userid)
#        msg = ""
#        if settings:
#            msg = "あなたが監視先に設定しているボイスチャンネルは以下のチャンネルです。\n"
#            for s in settings:
#                msg += "* {}\n".format(s)
#        else:
#            msg = "あなたはまだ監視先を設定していません。"
#        await ctx.response.send_message(msg)
        
        
    

