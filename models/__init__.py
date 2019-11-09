#!/usr/bin/python3
""" Creates a unique FileStorage instance for the application """
from models.engine.file_storage import file_storage


storage = FileStorage()
storage.reload()
