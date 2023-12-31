from PIL import Image
# Открываем изображение
image=Image.open('shashlyk.png')
image1_27=image
# Выводим информацию о нём
print(image1_27.size, image1_27.format, image1_27.mode)
# Сохраняем изображение
image1_27.save('image1_27.png')
# Выводим изображение
image1_27.show()