from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from .content import DATA
from .forms import MessageForm
from .models import Message


@login_required(login_url="login")
def panel_messages(request: HttpRequest):
	"""
	Render the panel messages page and apply optional filters.

	Retrieves contact messages, applies an optional filter provided via the
	querystring (``filter`` can be "read", "unread" or absent), and computes
	basic statistics (total, read, unread). Renders the ``panel.html``
	template with the appropriate context.

	Args:
		request (HttpRequest): The incoming HTTP request.

	Returns:
		HttpResponse: Rendered response for ``panel.html`` with context keys
		``contact_messages``, ``stats`` and ``current_filter``.
	"""
	messages = Message.objects.all().order_by("-created_at")

	filter_type = request.GET.get("filter", "all")

	if filter_type == "read":
		messages = messages.filter(is_read=True)
	elif filter_type == "unread":
		messages = messages.filter(is_read=False)

	stats = Message.objects.aggregate(
		total=Count("id"),
		read=Count("id", filter=Q(is_read=True)),
		unread=Count("id", filter=Q(is_read=False)),
	)

	return render(
		request,
		"panel.html",
		{
			"contact_messages": messages,
			"stats": stats,
			"current_filter": filter_type,
		},
	)


@login_required(login_url="login")
def mark_read(request: HttpRequest, id: int):
	"""
	Toggle the ``is_read`` flag of a message and redirect to the panel.

	Only accepts POST requests. Locates the ``Message`` instance by the given
	``id``, toggles its ``is_read`` state and saves the change.

	Args:
		request (HttpRequest): The incoming HTTP request (must be POST).
		id (int): Primary key of the message to toggle.

	Returns:
		HttpResponseRedirect: Redirects to the view named "panel".
	"""
	if request.method == "POST":
		message = get_object_or_404(Message, id=id)
		message.is_read = not message.is_read
		message.save()
	return redirect("panel")


@login_required(login_url="login")
def delete_message(request: HttpRequest, id: int):
	"""
	Delete a message when requested via POST and redirect to the panel.

	Only accepts POST requests. Removes the ``Message`` instance matching the
	given ``id`` and adds a success message to Django's messages framework.

	Args:
		request (HttpRequest): The incoming HTTP request (must be POST).
		id (int): Primary key of the message to delete.

	Returns:
		HttpResponseRedirect: Redirects to the view named "panel".
	"""
	if request.method == "POST":
		message = get_object_or_404(Message, id=id)
		message.delete()
		messages.success(request, "Mensagem excluída com sucesso.")
	return redirect("panel")


def landing_page(request: HttpRequest):
	"""
	Render the landing page and handle contact form submissions.

	For GET requests, renders the landing page with an empty ``MessageForm``.
	For POST requests, validates the form, saves the message when valid, and
	provides user feedback via ``django.contrib.messages``.

	Args:
		request (HttpRequest): The incoming HTTP request.

	Returns:
		HttpResponse: Rendered response for ``landpage.html`` with a context
		copied from ``DATA`` and the key ``form``.
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
