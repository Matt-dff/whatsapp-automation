import time
import pandas as pd
import urllib.parse
import re  # Para limpar números de telefone
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Caminho do ChromeDriver
caminho_driver = r"C:/Users/XXXXXX/XXXXXXX/XXXXXXXXXXXX/chromedriver.exe"

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Iniciar ChromeDriver
service = Service(caminho_driver)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abrir WhatsApp Web
driver.get("https://web.whatsapp.com")


# Carregar TODAS as abas do Excel
file_path = "C:/Users/XXXXXXXX/XXXXXX/XXXXXX/XXXXX/XXXX_XXXX.xlsx"
sheets = pd.read_excel(file_path, sheet_name=None, engine='openpyxl')  # Lê todas as abas

def send_message(phone_number, message):
    """Envia mensagem para o número especificado pelo WhatsApp Web."""
    encoded_message = urllib.parse.quote(message)  # Codificar URL
    url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
    driver.get(url)

    try:
        # Esperar botão de envio e clicar
        send_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
        )
        send_button.click()
        time.sleep(11)  # Aguarda envio da mensagem
        print(f"✅ Mensagem enviada para {phone_number}")
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem para {phone_number}: {e}")

# Loop para processar todas as abas do Excel
for sheet_name, df in sheets.items():
    print(f"📌 Processando aba: {sheet_name}")

    for _, row in df.iterrows():
        try:
            name = row["Aluno"]
            class_name = row["Turma"]
            location = row["Local"]
            professor = row["Professor"]
            start_date = row["Data de Inicio"]

            # 🔹 Ajustar formato da data para DD-MM-YYYY
            if isinstance(start_date, str):
                start_date = pd.to_datetime(start_date, errors='coerce')
            if isinstance(start_date, pd.Timestamp):
                start_date = start_date.strftime("%d-%m-%Y")

            # 🔹 Ajustar número de telefone (removendo caracteres desnecessários)
            phone_number = str(row["Telefone"]).strip()
            phone_number = re.sub(r"\D", "", phone_number)  # Remove tudo que não for número

            if not phone_number.startswith("55"):  # Adiciona +55 se não tiver
                phone_number = "55" + phone_number

            # 🔹 Remover "*" da mensagem
            class_name = str(class_name).replace("*", "")
            professor = str(professor).replace("*", "")
            location = str(location).replace("*", "")
            start_date = str(start_date).replace("*", "")

            # 🔹 Ajustar horário para evitar negrito no WhatsApp
            if '-' in class_name:
                parts = class_name.rsplit('-', 1)  # Divide no último hífen
                turma_name = parts[0].strip()
                horario = parts[1].strip()
                horario = horario.replace(":", "h")  # Substituir ":" por "h"

                formatted_class_name = f"{turma_name} - {horario}"
            else:
                formatted_class_name = class_name

            # 🔹 Mensagem formatada (Mensagem para receber no WHATSAPP)
            message = (
                "*XXXXXXXXXXXXXXXXX*\n\n"
                "VXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.\n\n"
                f"XXXXXXXXXXXXXXXXXXXXX\n\n"
            )
            send_message(phone_number, message)

        except Exception as e:
            print(f"⚠️ Erro ao processar aluno na aba {sheet_name}: {e}")

# Fechar navegador após envio de mensagens
driver.quit()

print("✅ Mensagens enviadas para todas as abas!")
