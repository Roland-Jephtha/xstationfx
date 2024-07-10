from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import authenticate, login as log, logout
from django.contrib import messages
from .forms import *
from django.shortcuts import get_object_or_404

# from django.contrib.sites.models import Site

from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.views import PasswordResetView







@login_required(login_url="signin")
def get_filtered_payment_options(request):
    currency = request.GET.get('currency')
    paymentOptions = Payment.objects.filter(currency=currency).values('logo', 'wallet_address', 'qr_code')

    return JsonResponse(list(paymentOptions), safe=False)


def home(request):
    base_url = request.build_absolute_uri('/')

    context = {
      
        'url': base_url,


    }  
    return render(request, 'index.html', context)


def about(request):
    base_url = request.build_absolute_uri('/')

    context = {
      
        'url': base_url,
    }  
    return render(request, 'about.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        contacts = Contact(
            name = name,
            email = email,
            message = message,
            number = subject,
        )
        contacts.save()
        messages.success(request, 'We received your Message we will get back to you soon!!!')
    contact = Contact.objects.all() 
    context = {
        "contacts":contact
    }  
        
    return render(request, 'contact.html', context)





















@login_required(login_url="signin")
def dashboard(request):
    user_profile = Profile.objects.get(user = request.user)
    # user_profile.balance += user_profile.profit
    user_profile.save()
    
    context = {
        'profile': user_profile,
    }

    return render(request, "dashboard_new.html", context)






@login_required(login_url="signin")

def deposit(request):

    user_profile = Profile.objects.get(user = request.user)
    initial_data = {'user': user_profile.id}  


  
    if request.method == "POST":
        deposit_form = DepositForm(request.POST, request.FILES)
        if deposit_form.is_valid():
            user = request.user
            currency = deposit_form.cleaned_data.get("currency")
            amount = deposit_form.cleaned_data.get("amount")
            user = request.user

         
            
            deposit_form.save()
            
            profile = Profile.objects.get(user = request.user)
            profile.balance += int(amount)
            profile.save()


            transaction = Transaction.objects.create(
            user = request.user,
            price = amount,
            action = "Deposit"
            
        )

       
            messages.success(request, 'Deposit was successful')
            return redirect( 'deposit',)
    else:
        deposit_form = DepositForm(initial=initial_data)

    
   
    user_profile = Profile.objects.get(username = request.user.username)
    payment = Payment.objects.all()

 
    base_url = request.build_absolute_uri('/')

    

    context = {
        "deposit_form": deposit_form,
        'profile': user_profile,
        'payment': payment,
        'url': base_url,


    }  
    
    return render(request, 'deposit.html', context)

@login_required(login_url="signin")

def withdraw_btc(request):

    
    user_profile = Profile.objects.get(user = request.user)
    initial_data = {'user': user_profile.id}  

    if request.method == "POST":
        withdraw_form = WithdrawForm(request.POST)
        if withdraw_form.is_valid():
            currency = withdraw_form.cleaned_data.get("currency")
            # withdraw_from = withdraw_form.cleaned_data.get("withdraw_from")
            amount = withdraw_form.cleaned_data.get("amount")
            qr_code = withdraw_form.cleaned_data.get("qr_code")
            wallet_address = withdraw_form.cleaned_data.get("wallet_address")
         
            

            profile = Profile.objects.get(user = request.user)
            
            if int(profile.balance) >= int(amount) and int(amount) >= 10:
                profile.balance -= int(amount)
                profile.withdrawal += int(amount)

                withdraw_form.save()
                
                transaction = Transaction.objects.create(
                user = request.user,
                price = amount,
                action = "withdrawal"
            
            )

                profile.save()
                messages.success(request, 'Withdrawal was successful')
            elif int(amount) < 10:
                messages.error(request, "The Minimum withdrawal is $10 ")
            else:
                messages.error(request, "Insufficient Funds")

    
            

            return redirect( 'withdraw_btc',)
    else:
        withdraw_form = WithdrawForm(initial=initial_data)

    payment = Payment.objects.all()

 
   
    
    context = {
        "withdraw_form": withdraw_form,
        'profile': user_profile,
        'payment': payment,

    }  
    
    return render(request, 'withdraw_btc.html', context)




@login_required(login_url="signin")
def withdraw_bank(request):

    user_profile = Profile.objects.get(user = request.user)
    initial_data = {'user': user_profile.id}  


    if request.method == "POST":
        withdraw_form = Withdraw_bankForm(request.POST)

        if withdraw_form.is_valid():
            user = request.user
            account_number = withdraw_form.cleaned_data.get("account_number")
            amount = withdraw_form.cleaned_data.get("amount")
            bank_name = withdraw_form.cleaned_data.get("bank_name")
         
            
            withdraw_form.save()


            profile = Profile.objects.get(user = request.user)
            profile.balance -= int(amount)
            profile.withdrawal += int(amount)
            profile.save()


            transaction = Transaction.objects.create(
            user = request.user,
            price = amount,
            action = "withdrawal"
            
        )

            messages.success(request, 'Withdrawal was successful')

            return redirect( 'withdraw_bank',)
    else:
        withdraw_form = Withdraw_bankForm(initial=initial_data)

    payment = Payment.objects.all()

 
   
    
    context = {
        "withdraw_form": withdraw_form,
        'profile': user_profile,
        'payment': payment,

    }  
    
    return render(request, 'withdraw_bank.html', context)




def transactions(request):
    transaction = Transaction.objects.filter(user = request.user) 
    user_profile = Profile.objects.get(user = request.user)

    context = {
        'profile': user_profile,
        'transactions': transaction,
    }  


    return render(request, 'transaction.html', context)





@login_required(login_url="signin")

def withdraw(request):
    user_profile = Profile.objects.get(user = request.user)

 
   
    
    context = {
        'profile': user_profile,

    }  
    
    
    return render(request, 'withdraw.html', context)


@login_required(login_url="signin")

def chart(request):
    user_profile = Profile.objects.get(user = request.user)
    
    context = {
        'profile': user_profile,

    }  
    
    
    return render(request, 'chart.html', context)

    




def signup(request):
    if request.user.is_anonymous:

        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email'].lower()
            full_name = request.POST['full_name']
            # ref_id = request.POST['referral']
            country = request.POST['country']
            phone = request.POST['phone']
      
            password = request.POST['password1']
            password2 = request.POST['password2']

            if password == password2:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already Used ')
                    return redirect('signup')
                elif CustomUser.objects.filter(username=username).exists():
                    messages.error(request, "Username Already Used")
                    return redirect('signup')
                else:
                    user = CustomUser.objects.create_user(username=username, email=email, password=password)
                    user.save()



                    
                    profile = Profile.objects.create(
                        user = user,
                        full_name = full_name,
                        username = username,
                        email = email,
                        ref_id = 0,
                        phone = phone,
                        country = country,
                        balance = 0,
                        profit = 0,
                        referral = 0
                        
                    )

                    subject = 'Welcome to Heritage Finance Network'
                    email_from = settings.EMAIL_HOST_USER
                    msg_html = render_to_string('email.html', {"username":username})
                    message = f'''Hi {username}, thank you for registering On Heritage Finance Network. Your Account Has Been Successful Created. Please Do Not Share Your Details With Anyone'''
                    send_mail( "Heritage Finance Network", message, email_from, [email], html_message=msg_html)
                    
                    

                    messages.success(request, 'Account Created successfully')
                    return redirect('password_reset_done')
            else:
                messages.error(request, "Password Not Thesame")
                return redirect('signup')
        else:
            return render(request, 'register.html')
    else:
        return redirect("dashboard")




def signin(request):
    if request.user.is_anonymous:

        if request.method == "POST":
            email = request.POST["email"].lower()
            password = request.POST["password"]
            try:
                customuser = CustomUser.objects.get(email=email)
                user = authenticate(username=customuser.username, password=password)  # Authenticate with email
                if user is not None:
                    log(request, user)
                    messages.success(request, "Login successful!")
                    return redirect("dashboard")  # Redirect to home page or any other desired page
                else:
                    messages.error(request, "Invalid email or password")
            except :
                messages.error(request, "Invalid email or password")
        
        return render(request, 'login.html',)
    else:
        return redirect("dashboard")




@login_required(login_url="signin")

def Update_profile(request):
    profile = get_object_or_404(Profile, user = request.user)

    if request.method == 'POST':
        # avatar = request.FILES['image']
        # fname = request.POST['fname']
        # lname = request.POST['lname']
        # email = request.POST['email']
        
        
        # profile = Profile.objects.get(username = request.user.username)
        
        # profile.avatar = avatar,
        # profile.first_name = fname,
        # profile.last_name = lname,
        # profile.email = email
        
        # profile.save()
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=profile)

        
            
    user_profile = Profile.objects.get(user = request.user)
    
    context = {
        'profile': user_profile,
        'form': profile_form
    }

    return render(request, "profile.html", context)





    
    




# def signin(request):
#     if request.user.is_anonymous:
#         if request.method == "POST":
#                 username = request.POST["username"]
#                 password = request.POST["password"]
#                 user = authenticate(username = username, password = password)
#                 if user is not None:
#                     login(request, user)
#                     return redirect("dashboard")
#                 else:
#                     messages.error(request, "Invalid Credentials")
#                     return redirect('signin')
#     else:
#         return redirect("dashboard")
#     return render(request, 'signin.html')




@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')


# Site.objects.create(domain = 'http://127.0.0.1:8000/rest_password', name = "epic")


class CustomResetPasswordView(PasswordResetView):
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'email_subject.txt'
    success_url = 'password_reset/done'
    form_class = CustomPasswordResetForm
    
    
    # print("site url", Site.objects.all())



def faq(request):
    return render(request, 'faq.html')



def terms(request):
    return render(request, 'Terms.html')

def assets(request):
    return render(request, 'Assets.html')

 

