from flask import Flask
from .config import Config

app = Flask(
    __name__,
    static_url_path=Config.STATIC_URL_PATH,
    static_folder=Config.STATIC_FOLDER,
    template_folder=Config.TEMPLATE_FOLDER
)

from app import routes