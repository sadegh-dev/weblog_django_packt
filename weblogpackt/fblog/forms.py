from django.forms import ModelForm
from .models import Post


class add_post_form (ModelForm):
    class Meta:
        model = Post
        fields = ('context',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['context'].widget.attrs.update({'class':'texterea','placeholder':'Enter your text'})

