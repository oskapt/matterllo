class BaseHook(object):

    @classmethod
    def actions(cls):
        """ Returns all supported actions.
        """
        return [m for m in cls.__dict__ if not '__' in m]
