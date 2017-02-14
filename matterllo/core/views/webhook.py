# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from matterllo.core.models import Webhook, Board
from matterllo.core.forms import WebhookCreateForm


@method_decorator(login_required, name='dispatch')
class WebhookDetailView(DetailView):
    model = Webhook


@method_decorator(login_required, name='dispatch')
class WebhookCreateView(SuccessMessageMixin, CreateView):
    model = Webhook
    form_class = WebhookCreateForm
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        form.instance.board_id = self.kwargs.get('board_id')
        return super(WebhookCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        board_id = self.kwargs.get('board_id')
        context = super(WebhookCreateView, self).get_context_data(**kwargs)
        context['board'] = Board.objects.get(id=board_id)
        context['webhooks'] = Webhook.objects.filter()
        return context

    def get_success_url(self):
        return reverse_lazy('bridge_create', kwargs={
            'board_id': self.kwargs.get('board_id'),
            'webhook_id': self.object.id})
