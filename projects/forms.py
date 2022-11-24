from django.forms import ModelForm
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 
                  'featured_image',
                  'description', 
                  'demo_link', 
                  'source_link', 
                  'tags',
                 ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

        def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)

            # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Add title'})

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})
                field['description'].widget.attrs.update({'class': 'custom-scroll'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        # Adding labels to change render on a frontend  
        labels = {
            'value': 'Please vote here',
            'body': 'Add some details',
        }

        # widgets = {
        #     'value': forms.CheckboxSelectMultiple(),
        # }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        self.fields['body'].widget.attrs.update({'id': 'id_description'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'dropdown'})

