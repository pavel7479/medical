import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

'''
Детекция границ с помощью Canny: Применяется алгоритм Canny для нахождения границ изображения, 
на основе которых будет работать преобразование Хафа.

Нахождение линий: cv2.HoughLinesP() используется для поиска линий на изображении. 
Линии представлены как координаты двух точек: (x1, y1) и (x2, y2).

Вычисление углов наклона: Для каждой найденной линии с помощью np.arctan2() вычисляется угол наклона, 
который затем конвертируется в градусы с помощью np.degrees(). Если угол наклона равен 90° или -90°, 
то этот угол исключается из дальнейших вычислений.
'''

class TextAligner:
    def __init__(self):
        pass

    def calculate_average_angle(self, image):
        # Преобразование в оттенки серого
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Применение Canny для детекции границ
        edges = cv2.Canny(gray_image, 50, 150)

        # Нахождение линий с помощью HoughLinesP
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

        # Список для хранения углов наклона
        angles = []

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]

                # Вычисление угла наклона линии
                angle_rad = np.arctan2(y2 - y1, x2 - x1)
                angle_deg = np.degrees(angle_rad)

                # Исключаем углы 90° и -90°
                if abs(angle_deg) != 90:
                    angles.append(angle_deg)

                # Рисуем линии на изображении (красные)
                # cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

            if angles:
                avg_angle = np.mean(angles)
                print(f"Средний угол наклона: {avg_angle:.2f}°")
                return avg_angle
            else:
                print("Не найдено подходящих линий.")
                return 0
        else:
            print("Линии не обнаружены.")
            return 0

    def rotate_image(self, image, angle):
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)

        # Матрица поворота
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, rotation_matrix, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

        return rotated

    def align_text(self, image):
        angle = self.calculate_average_angle(image)
        print(f"Определенный угол наклона: {angle:.2f}°")
        if angle != 0:
            return self.rotate_image(image, angle)
        else:
            return image


