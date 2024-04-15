from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home, name='home'),
    path('notice/', views.notice, name='notice'),
    path('register/', views.register, name='register'),
    path('login/', views.loginform, name='login'),
    path('profileview/', views.view_profile, name='profile'),
    path('profileform/', views.profile_form, name='profile_form'),
    path('logout/', views.user_logout, name='logout'),
    path('test/', views.upload_image, name='upload_image'),
    path('test2/', views.personal, name='personal'),
    path('personaldetailform/', views.personalforms, name='personalform'),
    path('academicdetailform/', views.academicforms, name='academicform'),
    path('categorydetailform/', views.categoryforms, name='categoryforms'),
    path('documentdetailform/', views.documentforms, name='documentforms'),
    path('all_detail_view/', views.all_detail_view, name='all_detail_view'),
    path('all_detail_view/paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('admissionprocess/', views.admissionprocess, name='admissionprocess'),
    path('bms/', views.bms, name='bms'),
    path('baf/', views.baf, name='baf'),
    path('bsccs/', views.bsccs, name='bsccs'),
    path('bscit/', views.bscit, name='bscit'),
    # path('change_1/',views.)

    # forget password code
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'baseapp/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'baseapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'baseapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'baseapp/password_reset_complete.html'), name='password_reset_complete'),
    

    



    
]