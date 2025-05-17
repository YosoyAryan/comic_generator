
# Create your views here.
from django.shortcuts import render
from .forms import StoryForm
from django.conf import settings
import os
from .ai_story_generator import ai_story_generator

def home(request):
    form = StoryForm()
    return render(request, 'generator/home.html', {'form': form})

def generate_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            style = form.cleaned_data['style']
            language = form.cleaned_data['language']

            output_dir, pdf_path = ai_story_generator(topic, style, language)
            pdf_url = pdf_path.replace("C:\\Users\\Asus\\Desktop\\storyscape\\templates", "")

            return render(request, 'generator/result.html', {
                'pdf_url': pdf_url,
                'pdf_path': pdf_path,
            })

    return render(request, 'generator/home.html', {'form': StoryForm()})
