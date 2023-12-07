import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk

def filter():
    # Получение введенных пользователем значений
    size = int(size_entry.get())
    kernel_type = kernel_combobox.get()
    image_choice = image_combobox.get()

    # Определение формы ядра
    if kernel_type == 'Прямоугольник':
        kernel_shape = cv2.MORPH_RECT
    elif kernel_type == 'Эллипс':
        kernel_shape = cv2.MORPH_ELLIPSE
    elif kernel_type == 'Крест':
        kernel_shape = cv2.MORPH_CROSS

    # Создание ядра
    kernel = cv2.getStructuringElement(kernel_shape, (size, size))

    # Загрузка выбранной картинки
    selected_image = cv2.imread(image_choice)

    # Морфологическая обработка изображения
    dilated_image = cv2.dilate(selected_image, kernel, iterations=1)
    eroded_image = cv2.erode(dilated_image, kernel, iterations=1)

    # Применение высокочастотного фильтра (увеличение резкости)
    high_pass_filtered_image = cv2.filter2D(selected_image, -1, np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]))

    # Отображение результатов
    cv2.imshow('Morphology', eroded_image)
    cv2.imshow('High Pass Filtered Image', high_pass_filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Создание графического интерфейса
root = tk.Tk()
root.title('Морфологическая обработка')

# Создание и размещение элементов интерфейса
size_label = ttk.Label(root, text='Размер ядра:')
size_label.pack()

size_entry = ttk.Entry(root)
size_entry.pack()

kernel_label = ttk.Label(root, text='Тип ядра:')
kernel_label.pack()

kernel_combobox = ttk.Combobox(root, values=['Прямоугольник', 'Эллипс', 'Крест'])
kernel_combobox.pack()

image_label = ttk.Label(root, text='Выберите картинку:')
image_label.pack()

# Создание комбо-бокса для выбора картинки
image_combobox = ttk.Combobox(root, values=['derevo.png', 'ded.png', 'sanyochek.jpg'])
image_combobox.pack()

apply_button = ttk.Button(root, text='Применить', command=filter)
apply_button.pack()

root.mainloop()