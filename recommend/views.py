from django.shortcuts import render, redirect, get_object_or_404
from .forms import SurveyForm, SurVeyPre
from .models import SurveyResponse

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            survey = SurveyResponse.objects.get_or_create(category=category)
            id = survey.id
            return redirect('preference', id=id)  # Redirect to the next survey step
    else:
        form = SurveyForm()
    return render(request, 'survey.html', {'form': form})

def survey_view_pre(request, id):
    survey = get_object_or_404(SurveyResponse, id=id)
    if request.method == 'POST':
        form = SurVeyPre(request.POST)
        if form.is_valid():
            preference = form.cleaned_data['preference']
            survey.preference = preference
            survey.save()
            return redirect('home')  # Redirect to the home page or the final step
    else:
        form = SurVeyPre()
    return render(request, 'preference.html', {'form': form})

def home_view(request):
    return render(request, 'index.html')
