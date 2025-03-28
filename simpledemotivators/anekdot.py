import os
from PIL import Image, ImageDraw, ImageFont

class TextImage:
    def __init__(self, folder, text, filename, text_color=(0, 0, 0), bg_color=(255, 255, 255), font_name="Formular-BlackItalic.ttf", max_width=1080, max_height=1080, padding=10):
        self.folder = folder  # Папка для сохранения изображения
        self.text = text
        self.filename = filename
        self.text_color = text_color
        self.bg_color = bg_color
        self.font_path = os.path.join(os.path.dirname(__file__), font_name)
        self.max_width = max_width
        self.max_height = max_height
        self.padding = padding

    def create_image_with_text(self):
        font_size = 100
        font = ImageFont.truetype(self.font_path, font_size)

        def wrap_text(text, font, max_width):
            lines = []
            words = text.split()
            line = ""

            for word in words:
                test_line = f"{line} {word}".strip()
                line_width = font.getbbox(test_line)[2]

                if line_width <= max_width - 2 * self.padding:
                    line = test_line
                else:
                    lines.append(line)
                    line = word

            if line:
                lines.append(line)

            return lines

        while font_size > 10:
            font = ImageFont.truetype(self.font_path, font_size)

            paragraphs = self.text.strip().split("\n")
            wrapped_text = []
            for paragraph in paragraphs:
                wrapped_text.extend(wrap_text(paragraph, font, self.max_width))
                wrapped_text.append("")

            text_height = sum(font.getbbox(line)[3] for line in wrapped_text) + len(wrapped_text) * 5

            if text_height <= self.max_height - 2 * self.padding:
                break
            font_size -= 2

        actual_height = min(text_height + 2 * self.padding + 10, self.max_height)

        img = Image.new('RGB', (self.max_width, actual_height), color=self.bg_color)
        draw = ImageDraw.Draw(img)

        y_offset = self.padding
        for line in wrapped_text:
            if line:
                draw.text((self.padding, y_offset), line, font=font, fill=self.text_color)
            y_offset += font.getbbox(line)[3] + 5

        # Убедимся, что указанная папка существует
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        save_path = os.path.join(self.folder, f"{self.filename}.png")
        
        # Сохранение изображения синхронно
        img.save(save_path)

        return True
