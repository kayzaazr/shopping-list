from django.shortcuts import render

mhs_name = 'Pak Bepe'
mhs_class = 'PBP A'
# Create your views here.
def show_main(request):
    context = {
        'name': mhs_name,
        'class': mhs_class,
    }
    
    return render(request, "main.html", context)