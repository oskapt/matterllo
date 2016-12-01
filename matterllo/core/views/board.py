# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator

from trello import TrelloClient

from matterllo.core.models import Board, Webhook


trello_client = TrelloClient(api_key=settings.TRELLO_APIKEY, token=settings.TRELLO_TOKEN)


@method_decorator(login_required, name='dispatch')
class BoardView(ListView):
    """ List boards from Trello and create each board into database.
        Create the trello Hook also.
        Then returns the board template.
    """
    model = Board
    template_name = "core/board.html"

    def get(self, request):
        try:
            boards = trello_client.list_boards()
            if boards:
                result = [h.delete() for h in trello_client.list_hooks()]
                print("delete trello hook :: result={}".format(result))

            for board in boards:
                slug_board = slugify(board.name, allow_unicode=False)
                b, created = Board.objects.get_or_create(name=slug_board)
                url = "{}://{}/callback/{}/".format(request.scheme, request.get_host(), b.id)
                result = trello_client.create_hook(url, board.id)
                print("create trello hook :: callback={} :: board={} :: result={}".format(url, slug_board, result))
            return super(BoardView, self).get(request)
        except Exception as e:
            print("unable to display board :: {}".format(e))
            return super(BoardView, self).get(request)

    def get_context_data(self, **kwargs):
        """ Fishy way to ensure trello_client is configured.
        """
        try:
            context = super(BoardView, self).get_context_data(**kwargs)
            trello_client.list_boards()
            context['trello_error'] = None
        except Exception as e:
            context['trello_error'] = e
        finally:
            return context


class BoardDetailView(DetailView):
    model = Board

    def get_context_data(self, **kwargs):
        context = super(BoardDetailView, self).get_context_data(**kwargs)
        context['webhook_list'] = Webhook.objects.filter(board=self.kwargs['pk'])
        return context
