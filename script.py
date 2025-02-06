import os

def get_project_structure(root_dir, exclude_folders=None, exclude_files=None):
    """Сканирует папку и возвращает структуру проекта без кешей и лишних данных."""
    if exclude_folders is None:
        exclude_folders = {".git", "__pycache__", ".idea", ".vscode"}
    if exclude_files is None:
        exclude_files = {".DS_Store"}

    project_structure = {}

    for root, dirs, files in os.walk(root_dir, topdown=True):
        # Удаляем ненужные папки из обхода
        dirs[:] = [d for d in dirs if d not in exclude_folders]

        # Относительный путь к корневой директории
        rel_path = os.path.relpath(root, root_dir)
        if rel_path == ".":
            rel_path = os.path.basename(root_dir)  # Корневая папка

        # Фильтруем файлы
        filtered_files = [f for f in files if f not in exclude_files and not f.endswith(".pyc")]

        if filtered_files:
            project_structure[rel_path] = filtered_files

    return project_structure

def print_project_structure(structure):
    """Выводит структуру проекта красиво."""
    for folder, files in structure.items():
        print(f"📂 {folder}")
        for file in files:
            print(f" ├── {file}")

# Укажите путь к вашему проекту (или оставьте текущую директорию)
project_path = os.getcwd()
structure = get_project_structure(project_path)

print("\n📁 Очищенная структура проекта:\n")
print_project_structure(structure)
