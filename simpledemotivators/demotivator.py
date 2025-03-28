import os
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests

class Demotivator:
    def __init__(self, top_text='', bottom_text=''):
        self._top_text = top_text
        self._bottom_text = bottom_text

    def _download_image(self, url, local_path):
        """
        Загружает изображение синхронно.
        """
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_path, 'wb') as out_file:
                out_file.write(response.content)

    def create(self, folder_name: str, avatar_name: str, result_filename: str, watermark=None, font_color='white', 
               fill_color='black', font_name='Impact.ttf', top_size=80, bottom_size=60,
               arrange=False, use_url=False) -> bool:
        """
        Создает демотиватор с именем файла, основанным на переданном параметре `result_filename`.
        
        :param folder_name: Папка для сохранения файла и загрузки изображения.
        :param avatar_name: Имя изображения, которое будет использовано.
        :param result_filename: Имя итогового файла.
        :param watermark: Текст водяного знака, если None, то не будет добавлен.
        :param font_color: Цвет шрифта.
        :param fill_color: Цвет фона.
        :param font_name: Путь к файлу шрифта.
        :param top_size: Размер шрифта для верхнего текста.
        :param bottom_size: Размер шрифта для нижнего текста.
        :param arrange: True, если фотография должна быть вставлена в рамку.
        :param use_url: True, если `avatar_name` - это URL.
        :return: True, если метод выполнен успешно.
        """
        # Путь к изображению (если это локальный файл или URL)
        avatar_path = os.path.join(folder_name, avatar_name)

        # Если используется URL, скачиваем изображение
        if use_url:
            local_file = os.path.join(folder_name, 'downloaded_image.jpg')
            self._download_image(avatar_name, local_file)
            avatar_path = local_file  # Теперь используем локальный путь

        # Загружаем изображение
        user_img = Image.open(avatar_path).convert("RGBA")
        (width, height) = user_img.size
        
        # Создаем изображение для демотиватора с рамкой
        if arrange:
            img = Image.new('RGB', (width + 250, height + 260), color=fill_color)
            img_border = Image.new('RGB', (width + 10, height + 10), color='#000000')
            border = ImageOps.expand(img_border, border=2, fill='#ffffff')
            img.paste(border, (111, 96))
            img.paste(user_img, (118, 103))
            drawer = ImageDraw.Draw(img)
        else:
            img = Image.new('RGB', (1280, 1024), color=fill_color)
            img_border = Image.new('RGB', (1060, 720), color='#000000')
            border = ImageOps.expand(img_border, border=2, fill='#ffffff')
            user_img = user_img.resize((1050, 710))
            (width, height) = user_img.size
            img.paste(border, (111, 96))
            img.paste(user_img, (118, 103))
            drawer = ImageDraw.Draw(img)

        # Работа с шрифтами и текстом
        font_1 = ImageFont.truetype(font=os.path.join(os.path.dirname(__file__), font_name), size=top_size, encoding='UTF-8')
        text_width = font_1.getsize(self._top_text)[0]

        while text_width >= (width + 250) - 20:
            font_1 = ImageFont.truetype(font=os.path.join(os.path.dirname(__file__), font_name), size=top_size, encoding='UTF-8')
            text_width = font_1.getsize(self._top_text)[0]
            top_size -= 1

        font_2 = ImageFont.truetype(font=os.path.join(os.path.dirname(__file__), font_name), size=bottom_size, encoding='UTF-8')
        text_width = font_2.getsize(self._bottom_text)[0]

        while text_width >= (width + 250) - 20:
            font_2 = ImageFont.truetype(font=os.path.join(os.path.dirname(__file__), font_name), size=bottom_size, encoding='UTF-8')
            text_width = font_2.getsize(self._bottom_text)[0]
            bottom_size -= 1

        size_1 = drawer.textsize(self._top_text, font=font_1)
        size_2 = drawer.textsize(self._bottom_text, font=font_2)

        if arrange:
            drawer.text((((width + 250) - size_1[0]) / 2, ((height + 190) - size_1[1])),
                        self._top_text, fill=font_color,
                        font=font_1)
            drawer.text((((width + 250) - size_2[0]) / 2, ((height + 235) - size_2[1])),
                        self._bottom_text, fill=font_color,
                        font=font_2)
        else:
            drawer.text(((1280 - size_1[0]) / 2, 840), self._top_text, fill=font_color, font=font_1)
            drawer.text(((1280 - size_2[0]) / 2, 930), self._bottom_text, fill=font_color, font=font_2)

        # Добавление водяного знака, если нужно
        if watermark is not None:
            (width, height) = img.size
            idraw = ImageDraw.Draw(img)
            idraw.line((1000 - len(watermark) * 5, 817, 1008 + len(watermark) * 5, 817), fill=0, width=4)

            font_2 = ImageFont.truetype(font=os.path.join(os.path.dirname(__file__), font_name), size=20, encoding='UTF-8')
            size_2 = idraw.textsize(watermark.lower(), font=font_2)
            idraw.text((((width + 729) - size_2[0]) / 2, ((height - 192) - size_2[1])),
                       watermark.lower(), font=font_2)

        # Сохраняем результат
        result_filename = f"{result_filename}_dem.jpg"
        result_filepath = os.path.join(folder_name, result_filename)
        img.save(result_filepath)

        # Удаляем файл, если он был загружен по URL
        if use_url:
            os.remove(avatar_path)

        return True
