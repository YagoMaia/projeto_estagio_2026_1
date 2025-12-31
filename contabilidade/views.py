from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .content import DATA
from .forms import MessageForm
from .models import Message


@login_required(login_url="login")
def panel_messages(request: HttpRequest):
	"""
	Function that responsible for render a panel messages page.
	"""
	messages = Message.objects.all().order_by("-created_at")
	return render(request, "panel.html", {"contact_messages": messages})


def landing_page(request: HttpRequest):
	"""
	Function that responsible for render a landing page and received message from form.
	"""
	if request.method == "POST":
		form = MessageForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, "Mensagem enviada com sucesso !!!")
			return redirect("landing_page")
		else:
			messages.error(request, "Erro ao enviar. Verifique os campos abaixo.")
	else:
		form = MessageForm()

	context = DATA.copy()
	context["form"] = form

	return render(request, "landpage.html", context)
