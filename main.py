
from MedicalApp import MedicalApp
from StreamlitAPI import StreamlitApp
from TextProcessor import TextProcessor
from TextRecognizer import TextRecognizer


def main():
    """Функция для запуска Streamlit-приложения."""
    app = MedicalApp()
    streamlit_app = StreamlitApp(app)  # Убираем app.file_manager
    streamlit_app.run()

if __name__ == "__main__":
    main()
#=============================================================================
