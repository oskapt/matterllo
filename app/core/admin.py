# -*- coding: utf-8 -*-
from django.contrib import admin

from core.models import Board, Webhook, Bridge

admin.site.register(Board)
admin.site.register(Bridge)
admin.site.register(Webhook)
