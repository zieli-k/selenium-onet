import json


class Config:
    def __init__(self, env):
        self.env = env

    def get_env(self):
        with open("configuration/configuration.json") as json_file:
            env_data = json.load(json_file)
            return env_data[self.env]


class Url(Config):
    def get_urls(self):
        return super().get_env()["urls"]

    def get_main_url(self):
        return self.get_urls()["main_url"]

    def get_about_url(self):
        return self.get_urls()["about_url"]


class Database(Config):
    def get_database(self):
        return super().get_env()["database"]


class Service(Config):
    def get_endpoint(self):
        return super().get_env()["service"]
