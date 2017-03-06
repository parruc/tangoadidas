from django import forms


class JoinTeamForm(forms.Form):
    hash = forms.CharField(label='Inserisci il codice squadra',
                           max_length=32,
                           min_length=32,
                           required=True)


class RemoveFromTeamForm(forms.Form):
    hash = forms.CharField(label='Inserisci il codice squadra',
                           max_length=32,
                           min_length=32,
                           required=True)


class JoinWithdrawEventForm(forms.Form):
    hash = forms.CharField(label='Inserisci il codice dell\'evento',
                           max_length=32,
                           min_length=32,
                           required=True,
                           widget=forms.HiddenInput(),)
