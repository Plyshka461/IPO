from PIL import Image, ImageDraw, ImageFont
# Открываем старое изображение
image5_27 = Image.open('image1_27.png')
# Создаём объект ImageDraw для рисования
draw = ImageDraw.Draw(image5_27)
# Задайте шрифт и размер (вы можете выбрать свой шрифт)
font = ImageFont.truetype('arial.ttf', 16)
# Задаём текст и его позицию
text = 'Тополь'
text_position = (40, 10)
# Добавляем текст на изображение
draw.text(text_position, text, fill='black', font=font)
# Сохраняем изображение
image5_27.save('image5_27.png')
# Выводим изображение
image5_27.show()

