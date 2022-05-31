from flask import Flask
import subprocess
from waitress import serve

app = Flask(__name__)

COFFEE_MACHINE_ADDR = "F7:02:B7:8E:E2:A0"

@app.route("/press_coffeemachine")
def hello_world():
    subprocess.run(["python3", "switchbot_py3.py", "-c", "press", "-d", COFFEE_MACHINE_ADDR])
    return "Success"

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
