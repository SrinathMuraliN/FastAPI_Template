from locust import HttpUser, task, between

class DashboardAPI(HttpUser):
    wait_time = between(1, 4)

    @task
    def create_userAPI(self):
        self.client.get(
            "api/dashboard/chocolate/predicted/dropdown?Manufacturer=FERRERO&region=UK"
        )

    @task
    def update_userAPI(self):
        self.client.get(
            "api/dashboard/chocolate/predicted/output?EB=EQ%20Lbs&Manufacturer=BLISS&Brand=BLISS&Super%20Variant=100KCAL%20OR%20LESS&Variant=95KCAL&Sub%20Segment=BOXED&Type=AFTER%20DINNER&Type%20of%20Launch=A&region=UK"
        )

    @task
    def delete_userAPI(self):
        self.client.get(
            "api/dashboard/chocolate/historical/alldata?time_period=&level=&EB=EQ%20Lbs&region=UK"
        )
