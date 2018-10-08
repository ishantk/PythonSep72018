import requests
import threading

"""
class FetchBooksTask:

    # Predict Time in which data will come back ??
    # Its all dependent on the Network
    def fetchBooks(self):
        response = requests.get("http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2")
        print(response.text)
"""

class FetchBooksTask(threading.Thread): # IS-A Relation

    # Predict Time in which data will come back ??
    # Its all dependent on the Network
    def run(self):

        for i in range(1, 11):
            print("FetchBooksTask", i)

        response = requests.get("http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2")
        print(response.text)

print("Python App Started")

task = FetchBooksTask();
# task.fetchBooks()
task.start() # start method will internally execute run method

for i in range(1,11):
    print("App",i)

print("Python App Finished")

# Main and FetchBooksTask are executed Asynchronously i.e. Concurrently or Parallely
# ALWAYS PUT A LONG RUNNING OPERATION IN A CHILD THREAD