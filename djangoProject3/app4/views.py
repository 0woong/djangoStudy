from django.shortcuts import render

# Create your views here.
def start4(request):
    n1 = int(request.POST['n1'])
    n2 = int(request.POST['n2'])
    subject = int(request.POST['subject'])
    print('start4 함수 호출')
    result = n1+n2
    context = {"result": result, 'n1': n1, 'n2': n2, 'subject': subject}
    return render(request, 'app4/start4.html', context)