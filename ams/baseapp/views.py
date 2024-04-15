from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import logout
from .forms import *
import re
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.http import HttpResponseBadRequest

# Create your views here.

def home(request):

    change = change_1.objects.all()

    context = {
            'change': change,
    }

    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        message = request.POST['message']

        contact = Contact.objects.create(name = name,number = number , message = message)
        contact.save()
        messages.success(request,'Enquiry has been submitted')  #enquiry

       

    return render(request, 'baseapp/home.html',context)




def notice(request):
    bsccs = bsccsnotice.objects.all()
    bscit = bscitnotice.objects.all()
    bms = bmsnotice.objects.all()
    baf = bafnotice.objects.all()

    context = {
        'bsccs':bsccs,
        'bscit': bscit,
        'bms': bms,
        'baf': baf 
                }
    return render(request, 'baseapp/notice.html', context)

def register(request):
    
    if request.method == 'POST':
        
        username = request.POST['username'] 
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        def is_valid_password(password):
    # Check the length of the password (minimum 8 characters).
            if len(password) < 8:
                return False

    # Check for at least one uppercase letter.
            if not any(char.isupper() for char in password):
                return False

    # Check for at least one lowercase letter.
            if not any(char.islower() for char in password):
                return False

    # Check for at least one digit.
            if not any(char.isdigit() for char in password):
                return False

    # Check for at least one special character (e.g., !@#$%^&*()).
            if not re.search(r'[!@#$%^&*()]', password):
                return False

    # All conditions passed; the password is valid.
            return True

    
        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, f"The user already exist")
            elif User.objects.filter(email = email).exists():
                messages.error(request, f"The email already exist")
            elif is_valid_password(password) == False:
                messages.error(request, f"The password is not so strong.")
            else:
                data = User.objects.create_user(username = username, email = email, password = password)  
                data.save()
                return redirect('login')    
        else:
            messages.error(request, f"The passwords doesnt match.")
            return redirect('register')
 

    return render(request, 'baseapp/register.html')


def loginform(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None :
            auth.login(request , user )
            return redirect('profile')
        else:
            messages.error(request, f"The User doesn't exist")
    return render(request, 'baseapp/login.html')

@login_required(login_url='login')    
def user_logout(request):
    logout(request)
    return redirect('home')  


# def profile_form(request):
#     form = UserProfileForm(request.POST, request.FILES, )
#     context = {'form': form}
#     return render(request, 'profileform.html', context)


@login_required(login_url='login')
def profile_form(request):
    userprofile = UserProfile.objects.get(user = request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES,instance=userprofile)
        if form.is_valid():
            form.save() # Save the form data to the database
            return redirect('profile')  # Redirect to a success page
    else:
        form = UserProfileForm(instance= userprofile)
   

    context = {
        'form': form,
        'userprofile': userprofile,
    }

    return render(request, 'baseapp/profileform.html',context)

@login_required(login_url='login')
def view_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'baseapp/profileview.html', {'profile': profile})


@login_required(login_url='login')
def personalforms(request):
    userprofile = UserProfile.objects.get(user = request.user)
    personaldetails = PersonalDetails.objects.get(user = request.user)
    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST,instance=personaldetails)
        if form.is_valid():
            form.save() # Save the form data to the database
            return redirect('academicform')  # Redirect to a success page
    else:
        form = PersonalDetailsForm(instance= personaldetails)
   

    context = {
        'form': form,
        'personaldetails': personaldetails,
        'userprofile': userprofile,
    }

    return render(request, 'baseapp/personaldetailform.html', context )


@login_required(login_url='login')
def academicforms(request):
    academicdetails = AcademicDetails.objects.get(user = request.user)
    if request.method == 'POST':
        form = AcademicDetailsForm(request.POST,instance=academicdetails)
        if form.is_valid():
            form.save() # Save the form data to the database
            return redirect('categoryforms')  # Redirect to a success page
    else:
        form = AcademicDetailsForm(instance= academicdetails)
   


    context = {
        'form': form,
        'academicdetails': academicdetails,

    }

    return render(request, 'baseapp/academicdetailform.html', context )


@login_required(login_url='login')
def categoryforms(request):
    categorydetail = CategoryDetails.objects.get(user = request.user)
    if request.method == 'POST':
        form = CategoryDetailsForm(request.POST,instance=categorydetail)
        if form.is_valid():
            form.save() # Save the form data to the database
            return redirect('documentforms')  # Redirect to a success page
    else:
        form = CategoryDetailsForm(instance= categorydetail)
   

    context = {
        'form': form,
        'categorydetail': categorydetail
    }

    return render(request, 'baseapp/categorydetailform.html', context )

@login_required(login_url='login')
def documentforms(request):
    documentdetail = DocumentDetails.objects.get(user = request.user)
    if request.method == 'POST':
        form = DocumentDetailsForm(request.POST,request.FILES, instance=documentdetail)
        if form.is_valid():
            form.save() # Save the form data to the database
            return redirect('all_detail_view')  # Redirect to a success page
    else:
        form = DocumentDetailsForm(instance= documentdetail)
   

    context = {
        'form': form,
        'documentdetail': documentdetail
    }

    return render(request, 'baseapp/documentdetailform.html', context )



def personal(request):
    personaldetail = PersonalDetails.objects.get(user = request.user)
    userprofile = UserProfile.objects.get(user = request.user)
    context = {
        'personaldetail': personaldetail,
        'userprofile': userprofile,
    }
    return render(request, 'baseapp/test2.html',context )

#test views
from .forms import ImageUploadForm
from .models import ImageModel

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            ImageModel.objects.create(title=title, image=image)
            return redirect('profile')  # Redirect to a success page
    else:
        form = ImageUploadForm()


    
    return render(request, 'baseapp/test.html', {'form': form},)





@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 10000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'baseapp/paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'baseapp/paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'baseapp/paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()


# payment gateway/

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

@login_required(login_url='login')
def all_detail_view(request):
    userprofile = UserProfile.objects.get(user = request.user)
    personaldetail = PersonalDetails.objects.get(user = request.user)
    academicdetail = AcademicDetails.objects.get(user = request.user)
    categoryDetail = CategoryDetails.objects.get(user = request.user)
    documentdetail = DocumentDetails.objects.get(user = request.user)

    currency = 'INR'
    amount = 10000  # Rs. 100
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    context = {

        'userprofile': userprofile,
        'personaldetail': personaldetail,
        'academicdetail': academicdetail,
        'categoryDetail' : categoryDetail,
        'documentdetail': documentdetail,
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': settings.RAZOR_KEY_ID,
        'razorpay_amount' : amount,
        'currency': currency,
        'callback_url': callback_url,

    }



    return render(request, 'baseapp/main_detail_view.html', context)

def admissionprocess(request):
    return render(request, 'baseapp/admissionprocess.html')

def bms(request):
    return render(request, 'baseapp/bms.html')

def baf(request):
    return render(request, 'baseapp/baf.html')

def bscit(request):
    return render(request, 'baseapp/bscit.html')

def bsccs(request):
    return render(request, 'baseapp/bsccs.html')


   



    
   