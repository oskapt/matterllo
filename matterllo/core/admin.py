from django.contrib import admin

from matterllo.core.models import Board, Webhook, Bridge

admin.site.register(Board)
admin.site.register(Bridge)
admin.site.register(Webhook)
