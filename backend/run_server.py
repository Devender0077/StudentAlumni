import os
import sys
import subprocess

os.environ['MONGO_URL'] = 'mongodb+srv://studentalumni_db_user:hJUOjxtkUwoaHXsA@student-alumni.kvxcqc2.mongodb.net/?appName=Student-Alumni'
os.environ['DB_NAME'] = 'studentalumni_db_user'
os.environ['JWT_SECRET'] = '743d0ed197b40ebe5e8a6fb3951c3ab05a4226639add2306f6cae31c32f42f07'
os.environ['FERNET_KEY'] = 'Mc3cw17oS5j43SoqziBCPu6yyQlpqm2dHG9zX8rMgqk='

os.chdir(os.path.dirname(os.path.abspath(__file__)))

proc = subprocess.Popen(
    [sys.executable, '-m', 'uvicorn', 'server:app', '--host', '0.0.0.0', '--port', '8000'],
    env=dict(os.environ)
)

print(f"Server started with PID: {proc.pid}")
proc.wait()