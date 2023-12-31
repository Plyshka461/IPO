from PIL import Image, ImageFilter
# Открываем изображение
image=Image.open('image3_27.png')
# Применяем фильтр к изображению
image4_27=image.filter(ImageFilter.GaussianBlur(radius=2))
# Сохраняем первое изображение
image4_27.save('image4_27.png')
# Применяем добавочно ещё 1 фильтр
image44_27=image4_27.filter(ImageFilter.EMBOSS)
# Сохраняем второе изображение
image44_27.save('image44_27.png')
# Выводим оба изображения
image4_27.show()
image44_27.show()
