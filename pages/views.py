from django.shortcuts import render
import random
from pages.db import db
from pages.main_dict import dict1

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
        
        admin_code = random.sample(range(111111,555555),1)[0]
        user_code = random.sample(range(555556,999999),1)[0]
        dict1[admin_code] = user_code

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
                    })
        
        admin_url = "http://ask-it.gq/"+ str(admin_code) + "/admin_panel"
        local_admin_url = "http://localhost:8000/"+ str(admin_code) + "/admin_panel"

        user_url = "http://ask-it.gq/"+ str(user_code)
        local_user_url = "http://localhost:8000/"+ str(user_code)

        context = {
            'user_code':user_code,
            'admin_url':admin_url,
            'local_admin_url':local_admin_url,
            'user_url':user_url,
            'local_user_url':local_user_url,
        }
        return render(request, 'pages/generate.html', context)
    else:
        print('CC Error')