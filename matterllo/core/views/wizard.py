# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from formtools.wizard.views import SessionWizardView

from matterllo.core.forms import BridgeCreateForm, WebhookCreateForm


@method_decorator(login_required, name='dispatch')
class MatterlloWizard(SessionWizardView):
    form_list = [WebhookCreateForm, BridgeCreateForm]
    template_name = 'core/wizard.html'

    def done(self, form_list, **kwargs):
        return HttpResponseRedirect('/')
