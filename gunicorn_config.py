from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
command = os.path.join(BASE_DIR,'bin/gunicorn')
pythonpath = BASE_DIR
bind = '0.0.0.0:8000'
workders =3