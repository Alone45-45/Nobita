import os
from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "9683694"))
API_HASH = getenv("API_HASH", "c426d9f7087744afdafc961a620b6338")
BOT_TOKEN = getenv("BOT_TOKEN", "5551900409:AAENnaoRPQUHtLlPXkv-umxlfRBxfxD23P0")
SESSION_NAME = getenv("SESSION_NAME", "AQA_Zr-dSuiQzy8JbTlvvDlu_ptag17xcaMFY5pvat--xFgoo04v_GvqKURxgTvYQRw3kUcGb03KERyQkEGWfSQ5HesbdJvlUbiqJnXL6bX_AwA8oPMhFBOYMGJOIdn4D-54pAna_xWqxp5bNanWh8zsz8IHugj5EB8974v_1tMDtp6KKCRqpaC_-br89hoY7fm9dWnxErDfCE7qfezs__3Yl_9rJwmsAMLiQNP9Z7C0OpCCHsFgakUKnWI736DmOXN7hm3bJY057jf79vHrRV1cK1xyhmjqkCTNwYZ7fbQRehktmdR0pI0E9gTseqlGOYOuGVb-8HT3ZdBKI9yYafu9AAAAAUpvbkwA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "TASTRON")
ALIVE_NAME = getenv("ALIVE_NAME", "Tom")
BOT_USERNAME = getenv("BOT_USERNAME", "WMTB_BOT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Alone45-45/Nobita")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "The_Xmenteam")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheJerryNetwork")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://noobyash:noobyash@cluster0.0mptw.mongodb.net/?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5286943475").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5286943475").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/63300139d232dc12452ab.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
