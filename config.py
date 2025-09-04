import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    IPMI_IP = os.getenv("IPMI_IP")
    IPMI_USER = os.getenv("IPMI_USER")
    IMPI_PASS = os.getenv("IMPI_PASS")
