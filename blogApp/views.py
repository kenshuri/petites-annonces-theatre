from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from blogApp.models import Offer
from blogApp.forms import OfferForm, SignUpForm

# Create your views here.
def index(request):
    all_offers = Offer.objects.all().order_by('-created_on')
    return render(request, 'blogApp/index.html', {'all_offers': all_offers})



def add_offer(request):
    if request.method == 'POST':
        print(request.POST)
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            # You can set additional fields here if needed
            # For example: offer.author = request.user
            offer.save()
            return redirect('index')
    else:
        form = OfferForm()
    return render(request, 'blogApp/add_offer.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect("index")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})