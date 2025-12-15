from django.shortcuts import render


def index(request):
    """Homepage View"""
    return render(request, 'website/index.html')


def preise(request):
    """Preise View"""
    return render(request, 'website/preise.html')


def oeffnungszeiten(request):
    """Öffnungszeiten View"""
    return render(request, 'website/oeffnungszeiten.html')


def kontakt(request):
    """Kontakt View"""
    if request.method == 'POST':
        # Hier kann später die Formular-Logik hinzugefügt werden
        pass
    return render(request, 'website/kontakt.html')


def booking(request):
    """SumUp Booking View"""
    return render(request, 'website/booking.html')
