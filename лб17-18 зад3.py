from PIL import Image
# Открываем изображение
image=Image.open('image1_27.png')
# Обрезаем изображение
image3_27=image.crop((10, 10, 300, 360 ))
# Сохраняем изображение
image3_27.save('image3_27.png')
# Выводим изображение
image3_27.show()