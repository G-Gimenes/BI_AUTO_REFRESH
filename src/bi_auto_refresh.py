import requests
import urllib3
import json
import os

urllib3.disable_warnings()
VERIFY_SSL = False

# Carregar credenciais de arquivo JSON ou variáveis de ambiente
with open("config/settings.json") as f:
    config = json.load(f)

TENANT_ID = config["TENANT_ID"]
CLIENT_ID = config["CLIENT_ID"]
CLIENT_SECRET = config["CLIENT_SECRET"]
USERNAME = config["USERNAME"]
PASSWORD = config["PASSWORD"]
GROUP_ID = config["GROUP_ID"]
DATASET_ID = config["DATASET_ID"]

print("=== 🏁 INÍCIO DO PROCESSO DE ATUALIZAÇÃO DO DATASET POWER BI 🏁 ===")

token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

token_data = {
    "grant_type": "password",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "username": USERNAME,
    "password": PASSWORD,
    "scope": "https://analysis.windows.net/powerbi/api/.default"
}

token_response = requests.post(token_url, data=token_data, verify=VERIFY_SSL)

if token_response.status_code != 200:
    print("❌ Falha na Autenticação token")
    print(token_response.text)
    raise SystemExit("⭕Processo interrompido por falha de autenticação.⭕")

access_token = token_response.json()["access_token"]
print("✅ Token Autenticado")

refresh_url = f"https://api.powerbi.com/v1.0/myorg/groups/{GROUP_ID}/datasets/{DATASET_ID}/refreshes"
headers = {"Authorization": f"Bearer {access_token}"}

print("🚀 Disparando refresh...")
response = requests.post(refresh_url, headers=headers, verify=VERIFY_SSL)

print(f"🔄️ Código de resposta HTTP: {response.status_code}")
if response.status_code == 202:
    print("✅ Refresh disparado com sucesso!!")
else:
    print("⭕ Falha ao solicitar atualização do dataset ⭕")
    print(response.text)