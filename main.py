# Пример вызова функции
import cv2
from TextAligner import TextAligner

'''
Определяем и поворачиваем изображения
'''
# Путь к изображению
image_path = "foto/01.jpg"

# Загружаем изображение
image = cv2.imread(image_path)

if image is None:
    print("Ошибка: изображение не найдено. Проверьте путь.")
else:
    # Печать оригинального изображения
    print("Оригинальное изображение:")
    cv2.imshow("Original Image", image)

    # Создание экземпляра класса и выравнивание текста
    aligner = TextAligner()
    aligned_image = aligner.align_text(image)

    # Печать выровненного изображения
    print("Выровненное изображение:")
    cv2.imshow("Aligned Image", aligned_image)

    # Сохранение результата
    output_path = "pred_foto/aligned_image.jpg"  # Укажите корректный путь
    cv2.imwrite(output_path, aligned_image)
    print(f"Результат сохранен по пути: {output_path}")

    cv2.waitKey(0)  # Ожидание клавиши
    cv2.destroyAllWindows()
