# WhatsApp Automation with Selenium

Este projeto automatiza o envio de mensagens no WhatsApp usando **Python, Selenium e WebDriver**. Ele lê os números de telefone de um arquivo **Excel** e envia mensagens personalizadas de uma agenda para cada contato.

## 📌 Funcionalidades
- 📤 Envio automatizado de mensagens para múltiplos contatos.
- 🗂️ Leitura de dados de um arquivo **Excel**.
- 🏷️ Personalização da mensagem com informações do contato.
- ✅ Manutenção da sessão do WhatsApp Web usando **cookies**.

## 🛠️ Pré-requisitos
Antes de executar o projeto, você precisa ter:

- Python **3.8+**
- Google Chrome **instalado**
- ChromeDriver **compatível com a versão do seu Chrome**
- Biblioteca Selenium instalada
- Biblioteca Pandas instalada
- Biblioteca OpenPyXL instalada (para ler arquivos Excel)

## 🔧 Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências:
   ```bash
   pip install selenium pandas openpyxl
   ```

3. Baixe o **ChromeDriver** compatível com sua versão do Chrome e coloque-o no diretório do projeto.

4. Edite o caminho do arquivo Excel no código para apontar para sua planilha.

## 🚀 Como usar
1. **Execute o script:**
   ```bash
   python main.py
   ```

2. **Faça login no WhatsApp Web** (se for a primeira vez).

3. O código enviará automaticamente as mensagens para os contatos listados no Excel.

## 📂 Estrutura do Projeto
```
📂 seu-repositorio/
├── 📄 main.py  # Código principal
├── 📄 README.md  # Documentação
├── 📄 requirements.txt  # Lista de dependências
├── 📄 whatsapp_cookies.pkl  # Cookies do WhatsApp Web (gerado automaticamente)
└── 📄 planilha.xlsx  # Arquivo Excel com os contatos
```

## 📝 Formato do Arquivo Excel
O arquivo **planilha.xlsx** deve conter as seguintes colunas:
```
ALUNO | TURMA | POLO | DATA_INICIO | CELULAR
```

## ⚠️ Aviso
- O WhatsApp pode bloquear contas que fazem **envio em massa**.
- Este projeto é apenas para **uso pessoal ou educacional**.

## 📜 Licença
Este projeto é de código aberto e distribuído sob a licença **MIT**.

