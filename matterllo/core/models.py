from __future__ import unicode_literals
from ast import literal_eval

from django.db import models


class Board(models.Model):

    name = models.CharField(max_length=100)
    webhook_activate = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "boards"

    def __str__(self):
        return self.name


class Webhook(models.Model):

    name = models.CharField(max_length=50)
    incoming_webhook_url = models.CharField(max_length=300, unique=True)

    icon_url = models.CharField(max_length=250, default='http://maffrigby.com/wp-content/uploads/2015/05/trello-icon.png')
    username = models.CharField(max_length=30, default='Matterllo')

    board = models.ManyToManyField(Board)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["name"]
        verbose_name_plural = "webhooks"

    def __str__(self):
        return "{} :: {}".format(self.name, self.incoming_webhook_url)


class Bridge(models.Model):
    EVENT_CHOICES = (
        # card
        ('addAttachmentToCard', 'addAttachmentToCard'),
        ('addLabelToCard', 'addLabelToCard'),
        ('addMemberToCard', 'addMemberToCard'),
        ('archiveCard', 'archiveCard'),
        ('commentCard', 'commentCard'),
        ('copyCard', 'copyCard'),
        ('createCard', 'createCard'),
        ('moveCardFromBoard', 'moveCardFromBoard'),
        ('moveCardToBoard', 'moveCardToBoard'),
        ('removeLabelFromCard', 'removeLabelFromCard'),
        ('removeMemberFromCard', 'removeMemberFromCard'),
        ('renameCard', 'renameCard'),
        ('renameCardDesc', 'renameCardDesc'),
        ('unarchiveCard', 'unarchiveCard'),
        ('updateCard', 'updateCard'),
        ('updateCardDueDate', 'updateCardDueDate'),
        # checklist
        ('addChecklistToCard', 'addChecklistToCard'),
        ('createCheckItem', 'createCheckItem'),
        ('updateCheckItemStateOnCard', 'updateCheckItemStateOnCard'),
        # list
        ('archiveList', 'archiveList'),
        ('createList', 'createList'),
        ('moveListFromBoard', 'moveCardFromBoard'),
        ('moveListToBoard', 'moveListToBoard'),
        ('renameList', 'renameList'),
        ('updateList', 'updateList'),
    )

    webhook = models.ForeignKey(Webhook, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    events = models.CharField(max_length=700)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "bridges"

    def __str__(self):
        return '{}::{}'.format(self.board, self.webhook)

    def events_as_list(self):
        return literal_eval(self.events)
