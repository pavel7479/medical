import cv2
import numpy as np
import os

class ImageProcessor:
    def __init__(self, output_dir="images"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def align_image(self, image):
        """
        Выравнивает изображение с использованием методов гомографии.
        :param image: Входное изображение (numpy array).
        :return: Выровненное изображение.
        """
        # Преобразуем изображение в оттенки серого
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Применяем детектор краев (например, Canny)
        edges = cv2.Canny(gray, 50, 150)

        # Находим контуры на изображении
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Находим наибольший контур (предполагаем, что это текст)
        largest_contour = max(contours, key=cv2.contourArea)

        # Находим прямоугольник, ограничивающий контур
        rect = cv2.minAreaRect(largest_contour)
        box = cv2.boxPoints(rect)
        box = np.int32(box)

        # Вычисляем углы для гомографии
        src_points = box.astype("float32")
        dst_points = np.array([[0, 0], [image.shape[1], 0], [image.shape[1], image.shape[0]], [0, image.shape[0]]], dtype="float32")

        # Вычисляем матрицу гомографии
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)

        # Применяем гомографию
        aligned_image = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))

        return aligned_image

    def save_image(self, image, filename):
        """
        Сохраняет изображение в папку.
        :param image: Изображение для сохранения.
        :param filename: Имя файла.
        """
        output_path = os.path.join(self.output_dir, filename)
        cv2.imwrite(output_path, image)
        return output_path