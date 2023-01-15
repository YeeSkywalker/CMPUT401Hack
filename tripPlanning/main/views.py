from tokenize import triple_quoted
from django.shortcuts import render, redirect
from .models import Trip

# Create your views here.
def index(req):
    trip = Trip.objects.all()
    print(trip)
    if req.method == 'POST':
        trip = Trip(origin = req.POST['origin'], destination=req.POST['destination'], departureDate=req.POST['date'])
        trip.save()
        return redirect('/')

    return render(
        req,
        'index.html',
        {'trips': trip}
    )

def delete(req, pk):
    trip = Trip.objects.get(id=pk)
    trip.delete()
    return redirect('/')