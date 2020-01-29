from django.shortcuts import render
from .forms import Registerform
# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = Registerform(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'registration/register_done.html' , {"new_user":new_user})
    else:
        user_form = Registerform()

    return render(request,'registration/register.html',{'form': user_form})