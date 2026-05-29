from django import forms
# from django.forms import ModelForm
from events.models import Category,Participant, Event

class styleMixin:

    default_design="w-full mt-2 mx-2 my-2 border-2 border-gray-100 rounded-lg focus:border-red-600"

    def StyleApply(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class':self.default_design,
                    'placeholder':f"Enter {field.label.lower()}"
                }) 
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class':self.default_design,
                    'placeholder':f"Enter {field.label.lower()}"
                })
            else:
                field.widget.attrs.update({
                    'class':self.default_design,
                    'placeholder':f"Enter {field.lablel.lower()}"
                })


class CategoryModelForm(styleMixin,forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','description']


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.StyleApply()
        

class ParticipantModelForm(styleMixin,forms.ModelForm):
    
    class Meta:
        model=Participant
        fields=['name','email']

    def __init___(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.StyleApply()

class EventModelForm(styleMixin,forms.ModelForm):
    class Meta:
        model=Event
        fields=['name','description','date','time','location','category','participants','ticket']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'participants': forms.CheckboxSelectMultiple(),
            }
        def __init__(self, *args,**kwargs):
            super().__init__(*args,**kwargs)
            self.StyleApply()