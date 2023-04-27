from django.db import models
from users.models import User


class Ad(models.Model):
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']

    image = models.ImageField(upload_to='images/', default=None, null=True)
    title = models.CharField(max_length=100, null=False)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000, blank=True, null=True, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def author_first_name(self):
        return self.author.first_name if self.author else None

    @property
    def author_last_name(self):
        return self.author.last_name if self.author else None

    @property
    def phone(self):
        return self.author.phone if self.author else None

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    text = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def author_first_name(self):
        return self.author.first_name if self.author else None

    @property
    def author_last_name(self):
        return self.author.last_name if self.author else None

    @property
    def author_image(self):
        return self.author.image if self.author else None
