from django.db import models

# Create your models here.


class Categories(models.Model):  # как отображается в админ панели
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"  # как отображается в базе данных
        verbose_name = "Категорию"  # переименовали в админ панеле
        verbose_name_plural = "Категории"  # переименовали в админ панеле
