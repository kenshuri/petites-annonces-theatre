from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from blogApp.models import Offer
from blogApp.forms import OfferForm, SignUpForm

# Create your views here.
def index(request):
    all_offers = Offer.objects.filter(filled=False).order_by('-created_on')
    return render(request, 'blogApp/index.html', {'all_offers': all_offers})


def offer(request, offer_id: int):
    offer = get_object_or_404(Offer, pk=offer_id)
    return render(request, 'blogApp/offer.html', {'offer': offer})


@login_required
def add_offer(request):
    if request.method == 'POST':
        print(request.POST)
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            # You can set additional fields here if needed
            # For example: offer.author = request.user
            offer.author = request.user
            offer.save()
            return redirect('index')
    else:
        form = OfferForm()
    return render(request, 'blogApp/add_offer.html', {'form': form})


@login_required
def delete_offer(request, offer_id: int):
    if request.user.id == Offer.objects.get(pk=offer_id).author.id:
        Offer.objects.get(pk=offer_id).delete()
        return redirect('index')
    else:
        return redirect('index')

@login_required
def fill_offer(request, offer_id: int):
    if request.user.id == Offer.objects.get(pk=offer_id).author.id:
        offer = get_object_or_404(Offer, pk=offer_id)
        offer.filled = True
        offer.save()
        return redirect('index')
    else:
        redirect('index')


def offer_search(request):
    search_query = request.POST.get('search')
    if search_query:
        results = Offer.objects.filter(filled=False).filter(title__icontains=search_query) | Offer.objects.filter(filled=False).filter(summary__icontains=search_query) | Offer.objects.filter(city__icontains=search_query)
    else:
        # If no query is provided, return all books
        results = Offer.objects.filter(filled=False)

    context = {
        'all_offers': results.order_by('-created_on')
    }

    return render(request, 'blogApp/partials/offers_partials.html', context)



def about(request):
    return render(request, 'blogApp/about.html')

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