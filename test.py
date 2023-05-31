# import requests

# class GitHubConnector:
#     def __init__(self, repository_url):
#         self.repository_url = repository_url

#     def check_for_updates(self):
#         try:
#             response = requests.get(f"{self.repository_url}/config.txt")
#             if response.status_code == 200:
#                 return True
#             else:
#                 return False
#         except requests.exceptions.RequestException:
#             return False

# connector = GitHubConnector("https://raw.githubusercontent.com/ErniedM/agent-framework/main")
# print(connector.check_for_updates())
from modules.system_info import SystemInfoModule
print(SystemInfoModule().collect_data())