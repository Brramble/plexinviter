import yaml
import os

with open("config.yaml", "r") as yaml_file:
    config = yaml.safe_load(yaml_file)

PLEX_TOKEN = config.get("CONFIG", {}).get("PLEX_TOKEN", "")
PLEX_SERVER_URL = config.get("CONFIG", {}).get("PLEX_SERVER_URL", "")
SMTP_USERNAME = config.get("CONFIG", {}).get("SMTP_USERNAME", "")
SMTP_PASSWORD = config.get("CONFIG", {}).get("SMTP_PASSWORD", "")
SMTP_SERVER = config.get("CONFIG", {}).get("SMTP_SERVER", "")
SMTP_PORT = config.get("CONFIG", {}).get("SMTP_PORT", 587)
EMAIL_SENDER = config.get("CONFIG", {}).get("EMAIL_SENDER", "")
EMAIL_DISPLAYNAME = config.get("CONFIG", {}).get("EMAIL_DISPLAYNAME", "")
EMAIL_SUBJECT = config.get("CONFIG", {}).get("EMAIL_SUBJECT", "Your invite is here")
EMAIL_MESSAGE = config.get("CONFIG", {}).get("EMAIL_MESSAGE", "")
WEBPAGE_TITLE = config.get("CONFIG", {}).get("WEBPAGE_TITLE", "Invitation Dashboard")
