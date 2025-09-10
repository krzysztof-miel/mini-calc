from locust import HttpUser, task, between

class JsonPlaceholderUser(HttpUser):
    # delikatne tempo, żeby nie męczyć publicznego API
    wait_time = between(1, 2)
    host = "https://jsonplaceholder.typicode.com"  # domyślny host

    @task(3)
    def list_posts(self):
        self.client.get("/posts")

    @task(1)
    def post_detail(self):
        self.client.get("/posts/1")

    @task(1)
    def list_comments(self):
        self.client.get("/comments")
