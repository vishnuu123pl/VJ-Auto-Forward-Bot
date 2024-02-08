from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "8cde2475d6b0cb1162b89ebbac71a95d")
      API_ID = int(getenv("API_ID", "13305226"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002019646585:-1001627511660").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
