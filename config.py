# Copyright (c) 2022 - 2024 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("APP_ID", "4857766"))
    API_HASH = os.environ.get("API_HASH", "6c3c6facf5598a4b318e138f8c407028")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6810524462:AAFveJiCanlqCrQiAMvQKWGxsAM6VuCE_Vk")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1001963446260"))
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://FILE-TO-LINK:FILE-TO-LINK@cluster0.chpurvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1596559467"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(file)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(file)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    MAX_MESSAGE_LENGTH = 4096
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    BOT_THUMB = f"{os.path.dirname(file)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 75
    MAX_TASK_DURATION_EXTRACT = 45 * 60  # 45 minutes (in seconds)
    MAX_TASK_DURATION_MERGE = 90 * 60  # 1 hour 30 minutes (in seconds)
