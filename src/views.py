import discord
from discord import Interaction,ChannelType, ui
from discord.ui import ChannelSelect, View, Button
import logging

#from api import NotificationSetting

class SettingSelectView(View):
    def __init__(self):
        super().__init__()
        self.selected_value=""
        
    @ui.select(
        cls=discord.ui.ChannelSelect,
        placeholder="select setting channel",
        channel_types=[ChannelType.text]
    )
    async def set_channel(self, ctx: Interaction, select: ChannelSelect):
        self.selected_value=select.values[0]
        try:
            await ctx.response.send_message("")
        except:
            logging.debug("raise error")

    @ui.button(label="receive")
    async def receive_button(self, ctx: Interaction, button: Button):
        if self.selected_value:
            await ctx.response.send_message("まずチャンネルを選択してください")
        logging.debug(button)
        #setting = NotificationSetting()
        #result = setting.update_setting(ctx.user.id,self.selected_value,True)
        #if result:
        #    msg = "追加に成功しました。現在の設定: {}".format(",".join(setting.get_channels_by_userid(ctx.user.id)))
        #else:
        #    msg = "追加に失敗しました。現在の設定: {}".format(",".join(setting.get_channels_by_userid(ctx.user.id)))
        #await ctx.response.send_message(msg)
        await ctx.response.send_message("pushed receive.:{}".format(self.selected_value))


    @ui.button(label="not receive")
    async def not_receive_button(self, ctx: Interaction, button: Button):
        if self.selected_value:
            await ctx.response.send_message("まずチャンネルを選択してください")
        #setting = NotificationSetting()
        #result = setting.update_setting(ctx.user.id,self.selected_value,False)
        #if result:
        #    msg = "削除に成功しました。現在の設定: {}".format(",".join(setting.get_channels_by_userid(ctx.user.id)))
        #else:
        #    msg = "削除に失敗しました。現在の設定: {}".format(",".join(setting.get_channels_by_userid(ctx.user.id)))
        #await ctx.response.send_message(msg)
        await ctx.response.send_message("pushed not receive.:{}".format(self.selected_value))
