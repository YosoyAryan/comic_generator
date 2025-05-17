from django import forms

class StoryForm(forms.Form):
    topic = forms.CharField(label='Story Topic', max_length=200)
    style = forms.ChoiceField(choices=[
        ('Disney Princes', 'Disney Princes'),
        ('Marvel', 'Marvel'),
        ('Anime', 'Anime'),
        ('DC Comics', 'DC Comics'),
        ('Observable Universe', 'Observable Universe'),
    ])
    language = forms.ChoiceField(choices=[
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('hi', 'Hindi'),
        ('ar', 'Arabic'),
        ('bn', 'Bengali'),
        ('te', 'Telugu'),
        ('mr', 'Marathi'),
        ('ta', 'Tamil'),
        ('ur', 'Urdu'),
        ('gu', 'Gujarati'),
        ('kn', 'Kannada'),
        ('or', 'Odia'),
        ('pa', 'Punjabi'),
    ])
