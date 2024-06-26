from django.shortcuts import render, redirect
import random
from pages.db import db
from pages.st import storage
from pages.main_dict import dict1
import firebase_admin
from firebase_admin import credentials, firestore
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt 
from PIL import Image 
import numpy as np 
from django.core.mail import send_mail, EmailMessage
import email, smtplib, ssl
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import secrets 
import string 
  

def index(request):
    return render(request, 'pages/index.html')

def form(request):
    return render(request, 'pages/form.html')

def link(request):
    if request.method == "POST":
        name = request.POST['name'] 
        email = request.POST['email']
        question = request.POST['question']
        characters = request.POST['characters']
        
        try:
            restricted_words = request.POST['restricted_words']
            try:
                stopwords_new = restricted_words.split(',')
            except:
                stopwords_new = []
        except:
            stopwords_new = []

        alphabet = string.ascii_letters + string.digits 
        ad_password = ''.join(secrets.choice(alphabet) for i in range(200))
        admin_code = ad_password
        user_code = random.sample(range(555556,999999),1)[0]
        doc_ref = db.collection(u'users').document(u'main')
        doc_ref.update({str(admin_code): user_code})

        db.collection(u'users').document(str(user_code)).set({
                u'user_code' : user_code,
                u'admin_code' : admin_code,
                u'name' : name,
                u'email' : email,
                u'question' : question,
                u'characters' : characters,
                u'restricted_words' : stopwords_new,
                u'responses':0,
                u'answers':[],
                u'names':[],
                    })
        
        admin_url = "http://www.ask-it.gq/"+ str(admin_code) + "/admin_panel"
        local_admin_url = "http://localhost:8000/"+ str(admin_code) + "/admin_panel"

        user_url = "http://www.ask-it.gq/"+ str(user_code)
        local_user_url = "http://localhost:8000/"+ str(user_code)

        return redirect(admin_url)
    else:
        print('CC Error')

def admin_panel(request, admin_code):
    if request.method == "POST":
        user_code = db.collection(u'users').document(u'main').get().to_dict()[str(admin_code)]
        user = db.collection(u'users').document(str(user_code)).get().to_dict()
        responses = user['responses']
        answers = user['answers']
        names = user['names']
        res_list = user['restricted_words']
        main_list = db.collection(u'users').document(u'list').get().to_dict()['main_list']
        unique_string=(" ").join(answers)
        stopwords = list(STOPWORDS)
        for i in res_list:
            stopwords.append(i)
        
        for j in main_list:
            stopwords.append(j)
        
        wc = WordCloud(background_color='white',stopwords = stopwords,max_font_size=130,max_words=100,height=1000,width=1500)
        wc.generate(unique_string)
        wc.to_file(f'imgs/{admin_code}.png')
        path_local = f'imgs/{admin_code}.png'
        image_path = f'imgs/{admin_code}.png'
        storage.child(image_path).put(path_local)
        image_url = storage.child(image_path).get_url(None)
        show_wordcloud = True

        user_url = "http://www.ask-it.gq/"+ str(user_code)
        local_user_url = "http://localhost:8000/"+ str(user_code)

        text_path = f'imgs/{admin_code}.txt'
        lst = []
        for i in names:
            for j in i:
                listitem = f'{j} => {i[j]}'
                lst.append(listitem)

        with open(text_path, 'w') as filehandle:
            for jo in lst:
                filehandle.write('%s\n' % jo)

        storage.child(text_path).put(text_path)
        text_url = storage.child(text_path).get_url(None)

        context = {
            'image_url':image_url,
            'image_path':image_path,
            'user_url':user_url,
            'local_user_url':local_user_url,
            'show_wordcloud':show_wordcloud,
            'unique_string':unique_string,
            'responses':responses,
            'admin_code':admin_code,
            'text_url':text_url,
        }
        return render(request, 'pages/admin_area.html', context)
    else:
        user_code = db.collection(u'users').document(u'main').get().to_dict()[str(admin_code)]
        user = db.collection(u'users').document(str(user_code)).get().to_dict()
        responses = user['responses']
        answers = user['answers']
        names = user['names']
        unique_string=(" ").join(answers)
        show_wordcloud = False
        user_url = "http://www.ask-it.gq/"+ str(user_code)
        local_user_url = "http://localhost:8000/"+ str(user_code)

        
        text_path = f'imgs/{admin_code}.txt'
        lst = []
        for i in names:
            for j in i:
                listitem = f'{j} => {i[j]}'
                lst.append(listitem)

        with open(text_path, 'w') as filehandle:
            for jo in lst:
                filehandle.write('%s\n' % jo)

        storage.child(text_path).put(text_path)
        text_url = storage.child(text_path).get_url(None)

        context = {
            'show_wordcloud':show_wordcloud,
            'unique_string':unique_string,
            'responses':responses,
            'local_user_url':local_user_url,
            'user_url':user_url,
            'admin_code':admin_code,
            'text_url':text_url,
        }
        return render(request, 'pages/admin_area.html', context)


def user_panel(request, user_code):
    if request.method == "POST":
        answer = request.POST['answer']
        name = request.POST['name']
        user_code = request.POST['user_code'] 

        user = db.collection(u'users').document(str(user_code))
        try:
            specific_answers = answer.split()
        except:
            specific_answers = []
            specific_answers.append(answer)

        lst = {name : answer}

        user.update({u'names': firestore.ArrayUnion([lst])})

        for i in specific_answers:
            user.update({u'answers': firestore.ArrayUnion([i.lower()])})
        

        user.update({"responses": firestore.Increment(1)})
        return render(request, 'pages/success.html')
    else:
        user = db.collection(u'users').document(str(user_code)).get().to_dict()
        question = user['question']
        characters = user['characters']
        context = {
            'question':question,
            'characters':characters,
            'user_code':user_code,
        }
        return render(request, 'pages/answer.html', context)

def mail_cloud(request, admin_code):
    if request.method == "POST":
        user_code = db.collection(u'users').document(u'main').get().to_dict()[str(admin_code)]
        user = db.collection(u'users').document(str(user_code)).get().to_dict()
        name = user['name']
        email = user['email']
        new_image_path = f'imgs/{admin_code}.png'
        email = EmailMessage(
            'Ask-it Wordcloud',
            'Hey '+ name + '. Thank you for using Ask-it. Check the attachment for your wordcloud.',
            'techshell.noreply@gmail.com',
            [email],
            )
        email.attach_file(new_image_path)
        email.send(fail_silently=False)
        mail_sent = True
        responses = user['responses']
        answers = user['answers']
        res_list = user['restricted_words']
        main_list = db.collection(u'users').document(u'list').get().to_dict()['main_list']
        unique_string=(" ").join(answers)
        stopwords = list(STOPWORDS)
        for i in res_list:
            stopwords.append(i)
        
        for j in main_list:
            stopwords.append(j)
        
        wc = WordCloud(background_color='white',stopwords = stopwords,max_font_size=130,max_words=100,height=1000,width=1500)
        wc.generate(unique_string)
        wc.to_file(f'imgs/{admin_code}.png')
        path_local = f'imgs/{admin_code}.png'
        image_path = f'imgs/{admin_code}.png'
        storage.child(image_path).put(path_local)
        image_url = storage.child(image_path).get_url(None)
        show_wordcloud = True
        context = {
            'mail_sent':mail_sent,
            'image_url':image_url,
            'image_path':image_path,
            'show_wordcloud':show_wordcloud,
            'unique_string':unique_string,
            'responses':responses,
            'admin_code':admin_code,
        }
        return render(request, 'pages/admin_area.html', context)
    
    
def end_meeting(request, admin_code):
    if request.method == "POST":
        user_code = db.collection(u'users').document(u'main').get().to_dict()[str(admin_code)]
        db.collection(u'users').document(str(user_code)).delete()   
        return redirect('index')


