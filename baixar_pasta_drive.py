import os
import gdown

# === Configurações ===
# 🔗 link da pasta pública do Google Drive (compartilhado com "qualquer pessoa com o link")
# Exemplo: "https://drive.google.com/drive/folders/1AbCdEfGhIjKlMnOpQrStUvWxYz?usp=sharing"
FOLDER_URL = "https://drive.google.com/drive/folders/1HHAHY4cNQxXUKbb4XK5Z1vdvk4e88FA-?usp=sharing"#movie_genre_model
LOCAL_DIR = "teste"  # nome da pasta local

# === Passo 1: cria a pasta se não existir ===
os.makedirs(LOCAL_DIR, exist_ok=True)

# === Passo 2: verifica se está vazia ===
if len(os.listdir(LOCAL_DIR)) == 0:
    print(f"📂 Pasta '{LOCAL_DIR}' está vazia. Iniciando download do Google Drive...")

    # === Passo 3: baixar todo o conteúdo da pasta ===
    # gdown reconhece automaticamente o link de pasta e baixa tudo
    gdown.download_folder(
        url=FOLDER_URL,
        output=LOCAL_DIR,
        quiet=False,
        use_cookies=False
    )

    print("✅ Download concluído!")
else:
    print(f"✅ A pasta '{LOCAL_DIR}' já contém arquivos. Nenhum download necessário.")
