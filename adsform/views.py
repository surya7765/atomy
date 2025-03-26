from django.shortcuts import render
from .forms import MessageForm
from django.http import JsonResponse
from .models import Message
# Create your views here.


def Home(request):
    form = MessageForm(request.POST)

    data = {}

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = MessageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['status'] = 'ok'

        return JsonResponse(data)

    return render(request,"index.html",{'form': form})

# from django.contrib.auth.models import User
#
#
# superusers = User.objects.filter(is_superuser=True).values_list('username')
#
# print(superusers)
