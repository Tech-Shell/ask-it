from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('form', views.form, name="form"),
    path('link', views.link, name="link"),
    path('<str:admin_code>/admin_panel', views.admin_panel, name="admin_panel"),
    path('<str:admin_code>/admin_panel/mail_cloud', views.mail_cloud, name="mail_cloud"),
    path('<str:admin_code>/admin_panel/end_meeting', views.end_meeting, name="end_meeting"),
    path('<str:user_code>', views.user_panel, name="user_panel"),
]