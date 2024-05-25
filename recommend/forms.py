from django import forms 

#create your form here
class SurveyForm(forms.Form):
    CATEGORY_CHOICES = [('High School', 'High School'),
                        ('College', 'College'),
                        ('Graduated', 'Graduated'),
                        ]
    

    
    
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.RadioSelect)


class SurVeyPre(forms.Form):
    PREFERENCE_CHOICES = [('Physical', 'Physical'),
                          ('Video', 'Video'),
                          ('Read/Write/Practice Exercise', 'Read/Write/Practice Exercise'),
                          ('Project-based Learning', 'Project-based Leaning'),
                          ]
    preference = forms.ChoiceField(choices=PREFERENCE_CHOICES,widget=forms.RadioSelect)

