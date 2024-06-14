from django.shortcuts import render, redirect
from blogApp.models import Offer
from blogApp.forms import OfferForm

# Create your views here.
def index(request):
    all_offers = Offer.objects.all()
    return render(request, 'blogApp/index.html', {'all_offers': all_offers})



def add_offer(request):
    if request.method == 'POST':
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
