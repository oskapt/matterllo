from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from matterllo.core.models import Board, Webhook, Bridge
from matterllo.core.forms import BridgeCreateForm


@method_decorator(login_required, name='dispatch')
class BridgeListView(ListView):
    model = Bridge
    template_name = "core/index.html"


@method_decorator(login_required, name='dispatch')
class BridgeDetailView(DetailView):
    model = Bridge


@method_decorator(login_required, name='dispatch')
class BridgeCreateView(SuccessMessageMixin, CreateView):
    model = Bridge
    form_class = BridgeCreateForm
    success_message = "Bridge was created successfully"

    def form_valid(self, form):
        form.instance.board_id = self.kwargs.get('board_id')
        form.instance.webhook_id = self.kwargs.get('webhook_id')
        return super(BridgeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        board_id = self.kwargs.get('board_id')
        webhook_id = self.kwargs.get('webhook_id')

        context = super(BridgeCreateView, self).get_context_data(**kwargs)

        context['board'] = Board.objects.get(id=board_id)
        context['webhook'] = Webhook.objects.filter(id=webhook_id).first()

        return context

    def get_success_url(self):
        return reverse_lazy('bridge_detail', kwargs={'pk': self.object.id})
