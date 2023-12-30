# users/forms.py
from django import forms
from .models import LoveTest
from django.forms import ValidationError

class LoveCalculatorForm(forms.ModelForm):
    class Meta:
        model = LoveTest
        fields = ['girl_name', 'boy_name']

    def clean_girl_name(self):
        girl_name = self.cleaned_data['girl_name']
        self.validate_names(girl_name)
        return girl_name

    def clean_boy_name(self):
        boy_name = self.cleaned_data['boy_name']
        self.validate_names(boy_name)
        return boy_name


    def is_valid_name(self, name):
        prohibited_words = [
            'arse',
    'sex',
    'sexy',
    'beautiful',
    'handsome',
    'arsehead',
    'arsehole',
    'ass',
    'asshole',
    'B',
    'bastard',
    'bitch',
    'bloody',
    'bollocks',
    'brotherfucker',
    'bugger',
    'bullshit',
    'C',
    'child-fucker',
    'Christ on a bike',
    'Christ on a cracker',
    'cock',
    'cocksucker',
    'crap',
    'cunt',
    'cyka blyat',
    'D',
    'damn',
    'damn it',
    'dick',
    'dickhead',
    'dyke',
    'F',
    'fatherfucker',
    'frigger',
    'fuck',
    'fucker',
    'G',
    'geda',
    'goddamn',
    'godsdamn',
    'H',
    'hell',
    'holy shit',
    'horseshit',
    'I',
    'in shit',
    'J',
    'Jesus Christ',
    'Jesus fuck',
    'Jesus H. Christ',
    'Jesus Harold Christ',
    'Jesus, Mary and Joseph',
    'Jesus wept',
    'K',
    'kike',
    'M',
    'motherfucker',
    'machikne',
    'muji',
    'N',
    'nigga',
    'nigra',
    'P',
    'pigfucker',
    'piss',
    'prick',
    'pussy',
    'S',
    'shit',
    'sala',
    'masala',
    'randi',
    'shit ass',
    'shite',
    'sisterfucker',
    'slut',
    'son of a whore',
    'son of a bitch',
    'spastic',
    'sweet Jesus',
    'T',
    'turd',
    'twat',
    'W',
    'wanker',
    'mugi',
        ]

        lower_case_name = name.lower()
        is_prohibited = any(word in lower_case_name for word in prohibited_words)

        return (
            name.strip() != '' and
            not any(char.isdigit() for char in name) and
            len(name) > 2 and
            not is_prohibited
        )

    def has_consecutive_same_characters(self, name):
        for i in range(len(name) - 2):
            if name[i] == name[i + 1] == name[i + 2]:
                return True
        return False

    def validate_names(self, name):
        if not self.is_valid_name(name):
            raise forms.ValidationError("Please enter a valid name.")
        elif self.has_consecutive_same_characters(name):
            raise forms.ValidationError("Please enter valid names")