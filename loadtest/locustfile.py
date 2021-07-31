#!/usr/bin/env python
# -*- coding: utf-8 -*-

from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(weight=10)
    def home(self):
        self.client.get("/home")

    @task(weight=10)
    def root(self):
        self.client.get("/")

    @task(weight=100)
    def goods(self):
        self.client.get("/goods")

    @task(weight=50)
    def create(self):
        self.client.get("/good-create")

    @task(weight=10)
    def add_good(self):
        self.client.post("/api/goods", json={"name": "locust"})

    @task(weight=1)
    def delete_all_goods(self):
        self.client.delete("/api/goods")

    @task(weight=1)
    def trigger_exception(self):
        self.client.get("/api/exceptions")
