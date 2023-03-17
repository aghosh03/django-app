from pathlib import Path
import os

BASE_DIR = str(Path(__file__).resolve().parent)
command = str(os.path.join(BASE_DIR,'bin/gunicorn'))
pythonpath =str(BASE_DIR)
bind = '0.0.0.0:8000'
workders =3