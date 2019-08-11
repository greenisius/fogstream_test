from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse  
from django.core.mail import mail_admins
#from smtplib import SMTPException
from django.contrib.auth.decorators import login_required

import json
import urllib.request

from .forms import MessageForm
from .models import UserMessage

def index(request):
    '''
    Функция занимается перенаправлением на страницу формы для зарегистрированных пользователей
    либо на страницу авторизации/регистрации для неавторизованных.
    '''
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('message_form'))
    else:
        return HttpResponseRedirect(reverse('login'))

'''
Реализация формы отправки сообщения. Парсит веб страницу и при необходимости
добавляет порцию информации из нее.
'''
@login_required
def message_form(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            #Получаем JSON из ссылки и добавляем к письму, если нужно
            web_data = urllib.request.urlopen('http://jsonplaceholder.typicode.com/users').read().decode('utf-8')
            web_data = json.loads(web_data)
            res_data = ''
            for data_unit in web_data:
                if form.cleaned_data['email'] == data_unit['email']:
                	res_data = json.dumps(data_unit)

            #На самом деле следовало бы сохранить файл локально и обращаться к нему 
            #Тем не менее, допустим, что информация по url изменяется
            message = UserMessage(
                email = form.cleaned_data['email'],
                text = form.cleaned_data['text'] + '\n\n' + res_data,
            )
            try:
            	mail_admins('Сообщение от пользователя', message.text)
            except BaseException as e:
        	    message.status = False
        	    result_message = e
            else:
        	    message.status = True
        	    result_message = 'Сообщение успешно отправлено'
            message.save()
            return render(request, 'mysiteapp/form_sending.html', {'form': form, 'result_message': result_message})
    else:
        form = MessageForm()
    return render(request, 'mysiteapp/form_sending.html', {'form': form})

