# -*- coding: utf-8 -*-
from json import loads

from matterhook import Webhook

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from core.models import Bridge
from core.hook.card import Hook as HookCard
from core.hook.list import Hook as HookList
from core.hook.checklist import Hook as HookChecklist


@method_decorator(csrf_exempt, name='dispatch')
class TrelloCallbacksView(View, HookCard, HookList, HookChecklist):

    def __init__(self, *args, **kwargs):
        self.supported_action = HookCard.actions() + HookList.actions() + HookChecklist.actions()
        return super(TrelloCallbacksView, self).__init__(*args, **kwargs)

    def head(self, request, board_id):
        return HttpResponse()

    def post(self, request, board_id):
        json_data = loads(request.body)

        action = json_data['action']
        action_type = action['type']
        board = slugify(json_data['model']['name'])

        bridges = Bridge.objects.filter(board__id=board_id)
        if not bridges:
            print("no configuration for this board :: board={}".format(board))
            return HttpResponse()

        if action_type not in self.supported_action:
            print("trello action not implemented :: action={}".format(action_type))
            return HttpResponse()

        action_parser = getattr(self, action_type)
        payload = action_parser(action=action)

        for bridge in bridges:
            if action_type not in bridge.events:
                print("no subscribe for this action :: board={} :: action={}".format(board, action_type))
                continue

            try:
                print("subscribe for this action :: board={} :: action={}".format(board, action_type))
                mwh = Webhook(*bridge.webhook.incoming_webhook_url.split("/hooks/"))
                mwh.username = bridge.webhook.username
                mwh.icon_url = bridge.webhook.icon_url
                mwh.send(payload)
            except Exception as e:
                print("unable to send mattermost message :: {}".format(e))
            continue

        return HttpResponse()
