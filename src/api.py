from db_control import DBControl
from config import SETTING_TABLE
from models import DMTarget

"""
db:modelメモ
* setting_table
id int 主キー
userid int ユーザーid
json json データ。チャンネルIDのリスト
"""
class NotificationSetting:
    def __init__(self, bot):
        self.bot = bot
        
    def get_channels_by_userid(self, userid):
        setting = DMTarget.get_by_userid(userid).json
        
        if setting:
            channels = self.get_all_voice_channel()
            result = [channels[d] for d in setting]
        else:
            result = []
        return result
    
    def update_setting(self, userid, channel, toggle):
        all_channel = self.get_all_voice_channel()
        channel_id = ""
        for id, name in all_channel.items():
            if channel == name:
                channel_id = id
                break
        if channel_id:
            setting = DMTarget.get_by_userid(userid)
            if setting:
                # 元々データあり
                data = setting.json
                if toggle:
                    # 追加
                    data.append(channel_id)
                else:
                    # 削除
                    data.remove(channel_id)
                setting.update(data)
            else:
                # 元々データなし
                
                data = [channel_id]
                setting = DMTarget.create(userid,data)
                
    def get_all_voice_channel(self):
        result = {}
        for channel in self.bot.get_all_channels():
            if channel.type == "voice":
                result[channel.id] = channel.name
        return result