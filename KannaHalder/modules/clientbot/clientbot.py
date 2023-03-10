from pytgcalls import PyTgCalls
from pyrogram import Client as Bot
from KannaHalder.config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION


client = Bot(STRING_SESSION, API_ID, API_HASH, plugins=dict(root="KannaHalder.plugins"))
robot = Bot(":memory:", API_ID, API_HASH, bot_token=BOT_TOKEN)

pytgcalls = PyTgCalls(client, overload_quiet_mode=False)

