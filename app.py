from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = os.getenv("USER", "codespace-user") 

    # Get Server Time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")

    # Get 'top' command output
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <html>
    <head><title>HTOP Output</title></head>
    <body>
        <h2>Name: Syed Ubaid </h2>
        <h3>Username: {username}</h3>
        <h3>Server Time: {formatted_time}</h3>
        <h3>Top Output:</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
