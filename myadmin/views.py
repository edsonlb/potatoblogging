from django.shortcuts import render
from myadmin.models import Myuser

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/myadmin/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
