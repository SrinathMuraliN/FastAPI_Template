from locust import HttpUser, task, between

class DashboardAPI(HttpUser):
    wait_time = between(1, 4)

    @task
    def create_userAPI(self):
        self.client.post(
            "/user/",
            json={
                "name": "John Doe",
                "email": "johndoe@example.com"
                
            },
        )

    @task
    def update_userAPI(self):
        user_id = 1  
        self.client.put(
            f"/user/{user_id}",
            json={
                "name": "Jane Doe",
                "email": "janedoe@example.com"
               
            },
        )

    @task
    def delete_userAPI(self):
        user_id = 1  
        self.client.delete(f"/user/{user_id}")
