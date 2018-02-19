from django.shortcuts import render,redirect
from forms import SignUpForm, LogInForm             #, ReviewForm
from django.contrib.auth.hashers import make_password, check_password
from models import UserModel, UserSession               #, Review, ShopAvailable
from django.http import HttpResponseRedirect


def index(request):
	return render(request, "homepage.html", {})

def signup(request):
    signup_form = SignUpForm(request.POST)
    if request.method=='POST':
        print signup_form.is_valid()

        if signup_form.is_valid():
            print True
            firstname = signup_form.cleaned_data['firstname']
            lastname = signup_form.cleaned_data['lastname']
            username = signup_form.cleaned_data['username']
            email = signup_form.cleaned_data['email']
            gender = signup_form.cleaned_data['gender']
            password = signup_form.cleaned_data['password']

            user = UserModel(firstname = firstname, lastname = lastname, username = username, email = email, password = make_password(password), gender = gender)
            user.save()
            return render(request, "success.html")

    return render(request,"signup.html", {'signup_form' : signup_form})


def login(request):

    if request.method == 'POST':
        login_form = LogInForm(request.POST)
        print login_form.is_valid(),"is Valid"

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = UserModel.objects.filter(username=username).first()
            if user:
                if check_password(password, user.password):
                    print "Welcome"
                    SESS = UserSession(user = user)
                    SESS.create_session_token()
                    SESS.save()
                    response = redirect('/gluespark.com/login/login_success')
                    response.set_cookie(key="session_token", value=SESS.session_token)
                    return response
                else:
                    print "Wrong Password"

            print True

    elif request.method == 'GET':
        login_form = LogInForm()

    return render(request, "login.html", {"login_form":login_form})

def check_validation(request):
    if request.COOKIES.get('session_token'):
        session = UserSession.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session:
            return session.user
    else:
        return None



"""
def substore(request):
    if check_validation(request) == None:
        context = {
            "login_or_not" : "You need to LogIn First",
        }
        return HttpResponseRedirect('/gluespark.com/login')
    else:
        context = {
            "login_or_not" : "Welcome",
        }
        review_form = ReviewForm(request.POST)
        if request.method =='POST':
            print "Post"
            if review_form.is_valid():
                print True
        return render(request, "substore2.html", context)
"""
def login_success(request):

    print check_validation(request)
    user = check_validation(request)

    context = {
        "user": user.username,
        "id": user.id,
    }
    return render(request,"login_successful.html",context)


"""
def login(request):
    login_form = LogInForm(request.POST)
    print "in login view"
    if request.method == 'POST':
        print login_form.is_valid(),"login"


        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = UserModel.objects.filter(username=username).first()
            if user:
                if check_password(password,user.password):
                    SESS = UserSession(user=user)
                    SESS.create_session_token()
                    SESS.save()
                    response = redirect('/gluespark.com')
                    response.set_cookie(key='session_token', value=SESS.session_token)
                    return response
                    print "user is valid"
                else:
                    print "password Mismatch"
            else:
                print "user does not Exist"

            return render(request, "success.html")

    return render(request, "login.html", {'login_form': login_form})

"""