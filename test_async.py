import asyncio
import re
from simpledemotivators_asinc import Quote
from simpledemotivators_asinc import TextImage
from simpledemotivators_asinc import Demotivator



async def main():
    text = """
Текст цитаты. Он может быть большим
и в несколько строк!
    """
    quote = Quote(text, "Hinaichigo_fox")
    #quote = Quote("Текст", "Автор")
    folder_name = "citgen/итог/"  # Папка для изображений
    avatar_name = "123.jpg"  # Название файла с аватаром
    avatar_url = "https://img.booru.org/rm//images/125/39c666e7e7baab8e39789f1d7089f4b390ee6505.jpg" #если надо скачать
    result_filename = "ЮРЛ"  # Имя итогового файла
    result_filename_photo = "Фото"  # Имя итогового файла

    # вызываем метод. Первое делает по url второе локально
    success = await quote.create(folder_name=folder_name, avatar_name=avatar_url, result_filename=result_filename, use_url=True)
    success = await quote.create(folder_name=folder_name, avatar_name=avatar_name, result_filename=result_filename_photo)

    if success:
        print("Цитата успешно создана!")
    else:
        print("Не удалось создать цитату.")

#пример демотиватора
    folder_name = "citgen/итог/"
    avatar_name = "123.jpg"
    avatar_url = "https://img.booru.org/rm//images/125/39c666e7e7baab8e39789f1d7089f4b390ee6505.jpg"
    name_local = "Локал"
    name_url  = "Юрл"
    watermark = "Тест"
    demotivator = Demotivator(top_text="Верхний текст", bottom_text="Нижний текст")
    success = await demotivator.create(folder_name=folder_name, avatar_name=avatar_name, result_filename=name_local, watermark=watermark)
    success = await demotivator.create(folder_name=folder_name, avatar_name=avatar_url, result_filename=name_url, watermark=watermark, use_url=True)

    if success:
        print("Демотиватор успешно создан!")
    else:
        print("Не удалось создать демотиватор.")

#пример анекдота!
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

    filename = "Анекдот"
    folder_name = "citgen/итог"  # Папка для изображений
    text_color = (255, 0, 0)  # Красный текст
    bg_color = (0, 0, 0)  # Черный фон)
    text_image = TextImage(folder_name, text, filename)
    success = await text_image.create_image_with_text()
    if success:
        print("Анекдот создан")
    else:
        print("Анекдот не создан")

if __name__ == "__main__":
    asyncio.run(main())
