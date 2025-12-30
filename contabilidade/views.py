from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .content import DATA
from .models import Message


def landing_page(request: HttpRequest):
	"""
	Function that responsible for render a landing page and received message from form.
	"""
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		content = request.POST.get("message")
		phone = request.POST.get("phone")

		Message.objects.create(name=name, email=email, message=content, phone=phone)

		messages.success(request, "Message sent successfully!")
		return redirect("landing_page")

	return render(request, "contabilidade/landpage.html", context=DATA)
