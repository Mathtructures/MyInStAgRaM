from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

debug = True
allowed_hosts = [
    '127.0.0.1',
]
db_engine = 'django.db.backends.sqlite3'
db_name = BASE_DIR / 'db.sqlite3'
