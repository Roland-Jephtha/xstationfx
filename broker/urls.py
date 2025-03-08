from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import CustomSetPasswordForm, CustomPasswordResetForm


urlpatterns = [
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('about', about, name='about'),
    path('deposit', deposit, name='deposit'),
    path('copy_trade', copy_trade, name='copy_trade'),
    path('withdraw_crypto', withdraw_btc, name='withdraw_btc'),
    path('withdraw_bank', withdraw_bank, name='withdraw_bank'),
    path('withdraw', withdraw, name='withdraw'),
    path('profile', Update_profile, name='profile'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('signout', signout, name='signout'),
    path('contact', contact, name='contact'),
    path('faq', faq, name='faq'),
    path('terms', terms, name='terms'),
    path('assets', assets, name='assets'),
    path('chart', chart, name='chart'),
    path('transaction', transactions, name='transaction'),
    path('online_training', training, name='online_training'),
    path('get-filtered-payment-options/', get_filtered_payment_options, name='get_filtered_payment_options'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm,
        template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class=CustomSetPasswordForm,
        template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_confirm.html'), name='password_reset_complete')

    
    # path('forgotPassword/', forgotPassword, name="forgotPassword"),
    # path('resetpassword_validate/<uidb64>/<token>/', resetpassword_validate, name="resetpassword_validate"),
    # path('resetPassword/',resetPassword, name="resetPassword"),
    
]
