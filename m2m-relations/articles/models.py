from django.db import models

class Tag(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name='Название тега')
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.tag_name
    
class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    # scopes = models.ManyToManyField(Tag, through='Scope', related_name='articles', verbose_name='Теги')
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
    
class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes',verbose_name='Стаья')
    tag =  models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tags', verbose_name='Тег')
    is_main = models.BooleanField(verbose_name='Основной тег')
    
    class Meta:
        ordering = ['-is_main', 'tag']