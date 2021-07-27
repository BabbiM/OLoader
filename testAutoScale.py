import requests
#This is to import the Python HTTP library to facilitate HTTP requests
import OLoader
#This is to import my Oloader package
import threading
#This is to import threading package to handle 2000 HTTP request tasks in a second
from random import randint
# This is to generate random number of HTTP request to flood the HAProxy on the manager node.
url = "https://github.com/BabbiM/LIDIWarehouseMgmt/"
#This is the url of the manage node in the Docker Swarm of HighPerformanceTiles.com
maximum_request_per_second = 2000

def sendHTTPRequest():
    no_of_request = randint(1, maximum_request_per_second)
    r = requests.get(url)
    while (response.raise_for_status()==None and no_of_request <= maximum_request_per_second):
    # Whenver there is no any  error encountered through the HTTP request process and doesn't reach maximum threshold value
    # This often sends a continuous traffic of HTTP request to the node where I install the HAProxy until it become overloaded
        floodRequest()
        if (response.status_code==503):
        #The manager node that is running HAProxy is overlaoded (servers often generate 503 error when they can not handle requests)
        # and facing difficulties to handle request
            scaleExecutor()
            #I have called the funciton sacleExecutor found in my Loader package to handle Overloading.

def floodRequest():
    sendHTTPRequest()
    threading.Timer(1,floodRequest).start()
