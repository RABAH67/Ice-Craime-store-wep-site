from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm ,MyPaaswordResetForm,MyPaaswordResetForm

urlpatterns = [
    
    path('',views.home,name="home"),
    path('abouteUs/',views.aboute,name="aboute"),
    path('contactUs/',views.contact,name="contact"),
    path('Category/<slug:val>',views.CategoryView.as_view(),name="category"),
    path('Cart/',views.cart,name="cart"),
    path('Cart/delete',views.cart_delete,name="cart_delete"),
    path('Category/Product-Detail/<int:pk>',views.DetailView.as_view(),name="detail"),
    path('Category/Product-Detail/<int:pk>/like',views.LikeView,name="like_post"),
    path('Category/Product-Detail/<int:pk>/add-to-cart/',views.add_to_cart,name="add_to_cart"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path('address/',views.address,name="address"),
    path('UpdateAddress/<int:pk>',views.UpdateAddress.as_view(),name="UpdateAddress"),

    
    
    # Authontication 
        #login && SingUp
    path('registration/',views.CustemRegistrationView.as_view(),name="registration"),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='site/login.html',authentication_form=LoginForm),name="login"),
        #Pssword_reset
    path('accounts/password-reset/',auth_view.PasswordResetView.as_view(template_name='site/password-reset.html',form_class=MyPaaswordResetForm),name="password-reset"),
       #Pssword_change
    path('accounts/password-change/',auth_view.PasswordChangeView.as_view(template_name='site/change-password.html',success_url='/accounts/password-change-done/',form_class=MyPaaswordResetForm),name="change-password"),
       #Pssword_change_done
    path('accounts/password-change-done/',auth_view.PasswordChangeDoneView.as_view(template_name='site/PasswordChangeDone.html'),name="change-password-done"),
        #Logout
    path('logout',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
