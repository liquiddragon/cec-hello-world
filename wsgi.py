import datetime
import socket
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    ts = time.time()
    with open('/mnt/ceclivinontheedge/cec.log', mode='w') as outfile:
        outfile.write(socket.gethostname())
        outfile.write('\t')
        outfile.write(datetime.datetime.fromtimestamp(ts).strftime('%d.%m.%Y %H:%M:%S'))
        outfile.write('\n')

    return "Hello World! Greetings from "+socket.gethostname()+"\n"


if __name__ == "__main__":
    application.run()
