from PIL import Image
# Открываем изображение
image=Image.open('image1_27.png')
# Поварачиваем изображение против часовой стрелки
image2_27=image.rotate(30, 0, expand=True)
# Сохраняем изображение
image2_27.save('image2_27.png')
# Выводим изображение
image2_27.show()