from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "1393092521"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://i.ibb.co/tKTKd2G/photo-2024-11-11-19-11-10-7436101514944315408.jpg")
API_ID = int(getenv("API_ID", "14680661"))
API_HASH = str(getenv("API_HASH", "166f6e394021081c5cdb41c92344deb7"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7933899088:AAELTXuyGTHPdrK6zuEYMRgMOqEZWP3CG6Y"))
FORCE_SUB = os.environ.get("FORCE_SUB", "sb_botz_update") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://raj94626:autocaptionbot@cluster0.wqaujtm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
