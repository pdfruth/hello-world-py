from flask import Flask, render_template, request, make_response, g
from redis import Redis
import os
import platform
import socket
import random
import json

#  This is a comment

hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
proc = platform.processor()

# may have to have env variable for Z

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    resp = make_response(render_template(
        'index.html',
        hostname=hostname,
        ipaddr=ipaddr,
        proc=proc,
    ))
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
