import requests

class GitHubConnector:
    def __init__(self, repository_url):
        self.repository_url = repository_url

    def check_for_updates(self):
        try:
            response = requests.get(f"{self.repository_url}/config.txt")
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False

    def get_config(self):
        try:
            response = requests.get(f"{self.repository_url}/config.txt")
            if response.status_code == 200:
                return response.text
            else:
                return None
        except requests.exceptions.RequestException:
            return None

    def download_module_code(self, module_name):
        try:
            response = requests.get(f"{self.repository_url}/modules/{module_name}.py")
            if response.status_code == 200:
                return response.text
            else:
                return None
        except requests.exceptions.RequestException:
            return None

    def log_data(self, data):
        try:
            response = requests.post(f"{self.repository_url}/logs/log.txt", data=data)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False
