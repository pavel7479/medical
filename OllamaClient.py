import requests
import json

class OllamaClient:
    """Класс для взаимодействия с Ollama API."""

    def __init__(self, model="mistral", host="http://localhost:11434"):
        self.model = model
        self.host = host

    def ask_ollama(self, prompt, temperature=0.1):
        """Отправляет запрос к Ollama API и возвращает ответ."""
        url = f"{self.host}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {  # Добавляем температуру модели
                "temperature": temperature
            }
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Ошибка: {response.status_code}"

