from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .content import DATA
from .models import Message


@login_required(login_url="login")
def panel_messages(request: HttpRequest):
	"""
	Function that responsible for render a panel messages page.
	"""
	messages = Message.objects.all().order_by("-created_at")
	return render(request, "panel.html", {"messages": messages})


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

		messages.success(request, "Mensagem enviada com sucesso !!!")
		return redirect("landing_page")

	return render(request, "landpage.html", context=DATA)
