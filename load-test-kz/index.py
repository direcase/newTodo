import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    #wait_time = between(1, 2)

    @task
    def getNews(self):
         with self.client.get("/api/news", catch_response=True) as response:
            if response.status_code == 200:
                response.success()

            else:
                response.failure(f'status code is {response.status_code}')
    
        #self.client.get("//api/news/4")

    @task(2)
    def search(self):
        with self.client.get("/api/news?search=турция", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f'status code is {response.status_code}')

        