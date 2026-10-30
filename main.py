import urllib.request
import time
import csv
from datetime import datetime


def check_website(url):

    print("Checking website:", url)

    try:
        # Start timer
        start_time = time.time()

        # Run request to access URL. Timeout is the max amount of time it is given to access (in s)
        response = urllib.request.urlopen(url, timeout = 10)

        # End timer
        end_time = time.time()

        # Exact time when the request finishes
        timestamp = datetime.now()

        # Calculate the amount of time it took to respond
        response_time = (end_time - start_time) * 1000

        health = check_status(response.status)

        print("Status code:", response.status)
        print("Response time:", round(response_time, 2), "ms")

        if health:
            print("Website is healthy\n")

        else:
            print("Website is unhealthy\n")


        # Saving the results
        save_results(url, response.status, response_time, health, timestamp)
        

    # If we got a 403 response i.e Forbidden
    except urllib.error.HTTPError as error:

        print("HTTP status code:", error.code)
        print("Website is unhealthy\n")

        save_results(url, error.code, response_time, health, timestamp)

    # If we got an error
    except Exception as error:

        print("Request failed:", error,"\n")

        save_results(url, error.code, response_time, health, timestamp)



def check_status(status_code):

    # Checks the code to determine the health
    if 200 <= status_code <= 299:
        return True

    else:   
        return False


def save_results(url, status_code, response_time, health, timestamp):

    # Creating the file and the CSV writer
    with open("monitor_results.csv", "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([url, status_code, response_time, health, timestamp])



websites = [

    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.github.com"
]


for url in websites:

    check_website(url)

