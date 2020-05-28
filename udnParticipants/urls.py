"""udnParticipants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from udnParticipants import views as udnViews

urlpatterns = [
    path('', udnViews.IndexPageController, name="index_page"),
    path('login_user/', udnViews.LoginUser, name="login_user"),
    path('do_loginn_user',udnViews.DoLoginUser, name="do_login_user"),
    path('form/', udnViews.ParticipantCreateView.as_view(template_name='form.html'), name='form'),
    path('show_all_data', udnViews.showAllData, name="show_all_data"),
    path('edit_participant', udnViews.editParticipant, name="edit_participant"),
    path('update_participant/<str:participant_id>',udnViews.updateParticipant,name="update_participant"),
    path('delete_participant/<str:participant_id>', udnViews.deleteParticipant, name="delete_participant"),
    path('save_participant', udnViews.saveParticipant, name='save_participant'),
]
