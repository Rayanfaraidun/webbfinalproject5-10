from django.shortcuts import render


from .forms import NameForm

def name_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # process the data as needed
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            return render(request, 'formapp/success.html', {'first': first, 'last': last})
    else:
        form = NameForm()
    return render(request, 'formapp/name_form.html', {'form': form})
