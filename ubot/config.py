import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    6743589204,
]

KYNAN = list(map(int, os.getenv("KYNAN", "6743589204 1575890355 5796301484").split()))

API_ID = int(os.getenv("API_ID", "22576593"))

API_HASH = os.getenv("API_HASH", "58dc5b6dc6b5408ff95dadb84ba148f4")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7127041603:AAH4NjPaCAxsI9yFf7KzlCVZWPN8aJ-giqM")

OWNER_ID = int(os.getenv("OWNER_ID", "6743589204"))

USER_ID = list(map(int, os.getenv("USER_ID", "6743589204").split()))

LOG_UBOT = int(os.getenv("LOG_UBOT", "-1002036716057"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002036716057 -1001876092598 -1001864253073 -1001451642443 -1001825363971 -1001797285258 -1001927904459 -1001287188817 -1001812143750 -1001608701614 -1001473548283 -1001608847572 -1001982790377 -1001538826310 -1001861414061").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://bc:123@cluster0.s5fu81s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
