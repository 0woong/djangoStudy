from django.shortcuts import render

# Create your views here.
def start2(request):
    print('start2')

    context = {
        'subject' : 'python',
        'class' : 2100
    }
    return render(request, 'app2/start2.html', context)