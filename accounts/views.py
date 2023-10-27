from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.views.generic import CreateView
from .models import *
from .forms import *
from django.contrib.auth import login, update_session_auth_hash
from django.urls import reverse
from .decorators import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView



def index(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('administration_dashboard')
            elif user is not None and user.is_member:
                login(request, user)
                return redirect('member_dashboard')
            elif user is not None and user.is_vendor:
                login(request, user)
                return redirect('vendor_dashboard')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'index.html', {'form': form, 'msg': msg})

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('administration_dashboard')
            elif user is not None and user.is_member:
                login(request, user)
                return redirect('member_dashboard')
            elif user is not None and user.is_vendor:
                login(request, user)
                return redirect('vendor_dashboard')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'index.html', {'form': form, 'msg': msg})

@login_required
@management_required
def administration(request):
    totalgroups = Group.objects.all().count()
    totalfarmers = Member.objects.all().count()
    totalloanproducts = LoanProduct.objects.all().count()
    totalnoloans = Loan.objects.all().count()
    #totalproducts = Product.objects.all().count()
    activepenalties = Penalty.objects.all().count()
    totalvendors = Vendor.objects.all().count()
    context = {
        'totalgroups': totalgroups,
        'totalfarmers': totalfarmers,
        'totalloanproducts': totalloanproducts,
        'totalnoloans':totalnoloans,
        #'totalproducts': totalproducts,
        'activepenalties': activepenalties,
        'totalvendors': totalvendors,
    }

    return render(request,'management/dashboard.html', context)



@login_required
@member_required
def members(request):
    return render(request,'member/dashboard.html')

@login_required
@vendor_required
def vendor(request):
    return render(request,'vendor/dashboard.html')


@login_required
def list_vendors(request):
    vendors = Vendor.objects.all()
    return render(request, 'list_vendors.html', {'vendors': vendors})


@login_required
@management_required
def CreateGroup(request):
    msg = None
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Group created'
            return redirect('list_groups')
        else:
            msg = 'form is not valid'
    else:
        form = CreateGroupForm()
    return render(request,'management/create_group.html', {'form': form, 'msg': msg})

@login_required
@management_required
def UpdateMemberProfile(request):
    msg = None
    if request.method == 'POST':
        form = UpdateMemberProfile(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Group created'
            return redirect('list_members')
        else:
            msg = 'form is not valid'
    else:
        form = UpdateMemberProfile()
    return render(request,'management/update_member_profile.html', {'form': form, 'msg': msg})

@login_required
def ListMembers(request):
    members = Member.objects.all() 
    return render(request, 'management/list_members.html', {'members': members})




@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been successfully changed.')        
        else:
            messages.error(request, 'Password change failed. Please correct the errors below.')  # Add error message if form is not valid
    else:
        form = CustomPasswordChangeForm(request.user)
    
    return render(request, 'password_update.html', {'form': form})

@login_required
def apply_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            # Process the loan application data and save it to the database
            # Redirect to a thank you page or another appropriate page
            return redirect('success')
    else:
        form = LoanForm()
    
    return render(request, 'loans.html', {'form': form})

@login_required
def repay_loan(request):
    if request.method == 'POST':
        form = LoanRepaymentForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., update loan repayment status)
            

            return redirect('loan_repayment_success')  # Redirect to a success 
    else:
        form = LoanRepaymentForm()

    context = {'form': form}
    return render(request, 'repayment.html', context)

def loan_list(request):
    loans = Loan.objects.all()
    return render(request, 'management/loan_list.html', {'loans': loans})

@login_required
def penalty_form(request):
    if request.method == 'POST':
        form = PenaltyForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('penalty_form_success')  # Redirect to a success page
    else:
        form = PenaltyForm()

    return render(request, 'penalty_form.html', {'form': form})

@login_required
def create_group_announcement(request):
    if request.method == 'POST':
        form = GroupAnnouncementForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            group_announcement = form.save()
            # Redirect to a success page or display a success message
            return redirect('success_page') 
    else:
        form = GroupAnnouncementForm()

    return render(request, 'group_announcement_form.html', {'form': form})

@login_required
def create_loan_reminder(request):
    if request.method == 'POST':
        form = LoanReminderForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            loan_reminder = form.save()
            # Redirect to a success page or display a success message
            return redirect('success_page') 
    else:
        form = LoanReminderForm()

    return render(request, 'loan_reminder_form.html', {'form': form})

@login_required
def vendor_form_view(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            # Process form data and save to the database
            form.save()
            # Redirect to a success page or do something else
    else:
        form = VendorForm()

    return render(request, 'vendor_form.html', {'form': form})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a success page or any other desired page
    else:
        form = ProductForm()

    return render(request, 'management/add_product.html', {'form': form})

def display_loan_products(request):
    loan_products = LoanProduct.objects.all()
    return render(request, 'loan_products.html', {'loan_products': loan_products})

def display_loans(request):
    loans = Loan.objects.all()
    return render(request, 'loan_cards.html', {'loans': loans})

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def trainings_page(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainings_page')  # Redirect to the same page after submission
    else:
        form = TrainingForm()

    trainings = Training.objects.all()

    context = {
        'form': form,
        'trainings': trainings,
    }

    return render(request, 'management/trainings_page.html', context)

@login_required
def upload_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_article')  
    else:
        form = ArticleForm()
    
    articles = Article.objects.all().order_by('-publish_date')
    return render(request, 'management/upload_article.html', {'form': form, 'articles': articles})


@login_required
def article_page(request):
    return render(request, 'management/article_page.html')
    
@login_required
def list_groups(request):
    groups = Group.objects.all()  # Fetch all groups from the database
    return render(request, 'management/list_groups.html', {'groups': groups})

def groups(request):
  
    groups = Group.objects.all()
    
    context = {'groups': groups}
    return render(request, 'group_members.html', context)

@login_required
def weather_page(request):
    return render(request, 'management/weather_page.html')

@login_required
def county_list(request):
    counties = County.objects.all()
    return render(request, 'county_list.html', {'counties': counties})

@login_required
def subcounty_list(request):
    subcounties = SubCounty.objects.all()
    return render(request, 'subcounty_list.html', {'subcounties': subcounties})

@login_required
def ward_list(request):
    wards = Ward.objects.all()
    return render(request, 'ward_list.html', {'wards': wards})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    member = get_object_or_404(Member, user=user)
    context = {'member': member}
    return render(request, 'profile.html', context)


def category_list(request):
    categories = Product.objects.values_list('category', flat=True).distinct()
    
    context = {'categories': categories}
    return render(request, 'categories.html', context)


def loan_line_chart(request):
    # Retrieve data from the Loan model
    loans = Loan.objects.all().order_by('create_at')
    dates = [loan.create_at.strftime('%Y-%m-%d') for loan in loans]  # Format dates as needed
    amounts = [loan.amount for loan in loans]

    # Pass the data to the template
    context = {
        'dates': dates,
        'amounts': amounts,
    }

    return render(request, 'loan_line_chart.html', context)