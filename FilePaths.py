

class FilePaths:
    """Класс для хранения путей к файлам."""

    def __init__(self, image_path, easyocr_output_path, csv_output_path, keywords_file_path,
                 prompt_file_path):
        self.image_path = image_path
        self.easyocr_output_path = easyocr_output_path
        self.csv_output_path = csv_output_path
        self.keywords_file_path = keywords_file_path
        self.prompt_file_path = prompt_file_path