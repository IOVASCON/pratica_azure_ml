# scripts/connect_workspace.py

from azureml.core import Workspace

def main():
    # Ajuste o caminho se necessário, caso seu config.json esteja em outro local
    ws = Workspace.from_config(path="./azureml_config/config.json")
    print(f"Conectado ao workspace: {ws.name}")
    print(f"Resource Group: {ws.resource_group}")
    print(f"Localização: {ws.location}")

if __name__ == "__main__":
    main()
