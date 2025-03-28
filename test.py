from simpledemotivators import Demotivator
from simpledemotivators import Quote
from simpledemotivators import TextImage


folder_name = "citgen/итог/"
avatar_name = '123.jpg'
avatar_url = 'https://img.booru.org/rm//images/125/39c666e7e7baab8e39789f1d7089f4b390ee6505.jpg'
result_filename = 'Цитата_локал'
result_url = 'Цитата_юрл'
text = """
Текст цитаты. Он может быть большим
и в несколько строк!
    """
author_name = 'Hinaichigo-fox'
quote = Quote(text, author_name)
success = quote.create(
	folder_name=folder_name,
	avatar_name=avatar_name,
	result_filename=result_filename,
	use_url=False  # Если True, будет скачано фото по URL
)

success = quote.create(
	folder_name=folder_name,
	avatar_name=avatar_url,
	result_filename=result_url,
	use_url=True  # Если True, будет скачано фото по URL
)

# Проверяем успешность операции
if success:
	print(f"Изображение с цитатой успешно создано и сохранено в папке {folder_name}")
else:
	print("Произошла ошибка при создании изображения.")




# Тест анекдота
text = """
Бал в офицерском собрании. Некий корнет подходит к поручику
Ржевскому:
- Господин поручик - вы, говорят, большой специалист в
этих делах. Скажите, вон та дама в рот берет?
- Которая? - переспрашивает Ржевский.
- Вон та, в желтом платье.
- Ну, я со спины сказать не могу, - пожимает плечами поручик.
В этот момент дама поворачивается, поручик Ржевский пристально
смотрит ей в лицо и говорит:
- Эта - берет.
Корнет подходит к даме, они о чем-то беседуют и удаляются.
Через некоторое время корнет возвращается, довольный:
- Действительно, берет! Но как вы определили, поручик?!
- Послушайте, корнет, - веско произносит поручик Ржевский, -
РОТ ЕСТЬ - ЗНАЧИТ БЕРЕТ.
"""
text_image = TextImage(
    folder="citgen/итог/",  # Путь к папке для сохранения изображения
    text=text,  # Текст
    filename="Анекдот",  # Имя файла без расширения
    text_color=(0, 0, 0),  # Цвет текста (черный)
    bg_color=(255, 255, 255),  # Цвет фона (белый)
    font_name="Formular-BlackItalic.ttf",  # Шрифт
    max_width=1080,  # Максимальная ширина изображения
    max_height=1080,  # Максимальная высота изображения
    padding=10  # Отступы от краев
)
# Создание изображения с текстом
result = text_image.create_image_with_text()
if result:
    print("Анекдот успешно создан!")
else:
    print("Произошла ошибка при создании изображения.")


#тест демотиватора
folder_name = "citgen/итог/"
avatar_name = "123.jpg"
avatar_url = 'https://img.booru.org/rm//images/125/39c666e7e7baab8e39789f1d7089f4b390ee6505.jpg'
result_filename_local = "локал"
result_filename_url = "юрл"
watermark = "Тест"


demotivator = Demotivator(top_text="Верхний текст", bottom_text="Нижний текст")
result = demotivator.create(folder_name=folder_name, avatar_name=avatar_name, result_filename=result_filename_local, watermark=watermark)

demotivator = Demotivator(top_text="Верхний текст", bottom_text="Нижний текст")
result = demotivator.create(folder_name=folder_name, avatar_name=avatar_url, result_filename=result_filename_url, watermark=None, use_url=True)

# Проверяем результат
if result:
    print("Демотиватор успешно создан!")
else:
    print("Произошла ошибка при создании демотиватора.")

