import datetime
import socket
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    ts = time.time()
    with open('/mnt/ceclivinontheedge/cec.log', mode='a') as outfile:
        outfile.write(socket.gethostname())
        outfile.write('\t')
        outfile.write(datetime.datetime.fromtimestamp(ts).strftime('%d.%m.%Y %H:%M:%S'))
        outfile.write('\n')

    output = '<a href="/accesslog">Log</a><br/>'
    output += 'Hello World! Greetings from '+socket.gethostname()+'\n <br/>'

    return output

@application.route("/accesslog")
def viewlog():
    output = ""
    with open('/mnt/ceclivinontheedge/cec.log', mode='r') as infile:
        for line in infile:
            output += output + line + "<br/>"

    return output

if __name__ == "__main__":
    application.run()
