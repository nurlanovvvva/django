from django import forms
from posts.models import Post, Tag


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()
    rate = forms.IntegerField()


def clean(self):
    cleaned_data = super().clean()
    title = cleaned_data.get('title')
    content = cleaned_data.get('content')

    if title and content and title.lower() == content.lower():
        raise forms.ValidationError('Заголовок и текст не должны совпадать')
    return cleaned_data

def clean_title(self):
    title = self.cleaned_data['title']
    if 'python' in title.lower():
        raise forms.ValidationError('Слово "python" недопустимо в зоголовке')
    return title


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'rate', 'content', 'image')
        widgets = {
            'title': forms.TextInput
                (attrs={
                'class': 'form-control',
                'placeholder': "Заголовок поста",
                "rows": 2,
                "cols": 15,
            }),
            'content': forms.Textarea
            (attrs={
                "placeholder": "Текст поста",
                "class": "form-control",}),
            "rate": forms.NumberInput(
                attrs={"class": "form-control","placeholder": "Оценка"})
        }

class SearchForm(forms.Form):
    search = forms.CharField(required=False,
                             max_length=100,
                             min_length=1,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Поиск...'

                              }
                             ))
    tag = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    orderings = (
        ("title", "Заголовок"),
        ("-title, ", "Заголовок в обратном порядке"),
        ("created_at", "Дата создания"),
        ("-created_at", "Дата создания  в обратном порядке"),
        ("updated_at", "Дата обновления"),
        ("-updated_at", "Дата обновления в обратном порядке"),
        ("rate", "Рейтинг"),
        ("-rate", "Рейтинг в обратном порядке"),
    )
    orderings = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class PostUpdateForm(forms.ModelForm):
    model = Post
    fields = ('title', 'rate', 'content', 'image')







