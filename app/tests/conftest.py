import pytest
from app import create_app, db
from config import Config
from app.models import Author, Book