import urllib.request
import time
import csv


def check_website(url):

    print("Checking website:", url)

    try:
        # Start timer
        start_time = time.time()

        # Run request to access URL. Timeout is the max amount of time it is given to access (in s)
        response = urllib.request.urlopen(url, timeout = 10)

        # End timer
        end_time = time.time()

        # Calculate the amount of time it took to respond
        response_time = (end_time - start_time) * 1000

        health = check_status(response.status)

        print("Status code:", response.status)
        print("Response time:", round(response_time, 2), "ms")

        if health:
            print("Website is healthy\n")

        else:
            print("Website is unhealthy\n")


    # If we got a 403 response i.e Forbidden
    except urllib.error.HTTPError as error:
        print("HTTP status code:", error.code)
        print("Website is unhealthy\n")

    # If we got an error
    except Exception as error:
        print("Request failed:", error,"\n")



def check_status(status_code):

    if 200 <= status_code <= 299:
        return True

    else:   
        return False
    

websites = [

    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.github.com"
]


for url in websites:

    check_website(url)

