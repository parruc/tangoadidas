from django import forms


class JoinTeamForm(forms.Form):
    hash = forms.CharField(label='Inserisci il codice squadra',
                           max_length=32,
                           min_length=32,
                           required=True)
