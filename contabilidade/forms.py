from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Message


class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ["name", "email", "phone", "message"]

	def clean_phone(self):
		"""
		Function responsible for validating the phone number.
		"""
		phone = self.cleaned_data.get("phone")

		if phone:
			phone = "".join(filter(str.isdigit, phone))

			if len(phone) < 10:
				raise forms.ValidationError("O telefone parece incompleto.")

		return phone

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		base_classes = "w-full px-4 py-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-600 focus:border-transparent outline-none transition-all"

		self.fields["name"].widget.attrs.update({
			"class": base_classes,
			"placeholder": "Seu Nome *",
		})
		self.fields["email"].widget.attrs.update({
			"class": base_classes,
			"placeholder": "Endereço de E-mail *",
		})
		self.fields["phone"].widget.attrs.update({
			"class": base_classes,
			"placeholder": "Número de Telefone",
			"type": "tel",
		})
		self.fields["message"].widget.attrs.update({
			"class": f"{base_classes} resize-none",
			"placeholder": "Conte-nos sobre suas necessidades *",
			"rows": 4,
		})


class CustomLoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		base_classes = "appearance-none rounded-lg relative block w-full px-3 py-3 border border-slate-300 placeholder-slate-500 text-slate-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"

		self.fields["username"].widget.attrs.update({
			"class": base_classes,
			"placeholder": "Nome de Usuário",
		})
		self.fields["password"].widget.attrs.update({
			"class": base_classes,
			"placeholder": "Senha",
		})
