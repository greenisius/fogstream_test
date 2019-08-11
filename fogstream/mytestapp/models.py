from django.db import models

class UserMessage(models.Model):
    '''
    Модель сообщения с полями: email отправителя, текст сообщения и статус отправки
    '''
    email = models.EmailField(max_length=40)
    text = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.email


