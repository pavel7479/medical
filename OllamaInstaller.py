import subprocess
import time

class OllamaInstaller:
    """Класс для установки и запуска Ollama."""

    def install_ollama(self):
        """Устанавливает Ollama."""
        print("Устанавливаем Ollama...")
        try:
            # Используем shell=True для корректной работы с пайпом
            subprocess.run("curl -fsSL https://ollama.ai/install.sh | sh", shell=True, check=True)
            print("Ollama установлен успешно.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при установке Ollama: {e}")

    def start_ollama(self):
        """Запускает Ollama в фоновом режиме."""
        print("Запускаем Ollama в фоновом режиме...")
        subprocess.Popen(["nohup", "ollama", "serve", ">", "ollama.log", "2>&1", "&"], shell=True)
        time.sleep(10)  # Ожидание запуска
        print("Ollama запущен и работает.")

    def pull_model(self, model_name="mistral"):
        """Загружает модель Ollama."""
        print(f"Загружаем модель {model_name}...")
        subprocess.run(["ollama", "pull", model_name], check=True)
        print(f"Модель {model_name} загружена успешно.")