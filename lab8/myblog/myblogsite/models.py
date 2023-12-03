from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to="images", verbose_name="Изображение")
    dt = models.DateTimeField(verbose_name="Дата и время")

    CATEGORIES = [
        ("SPORTS", "Спорт"),
        ("IT", "IT"),
        ("ANIMALS", "Животные"),
        ("OTHER", "Другое"),
    ]

    category = models.CharField(
        choices=CATEGORIES, default="IT", verbose_name="Категория", max_length=64
    )

    def __str__(self):
        return self.title, self.image
