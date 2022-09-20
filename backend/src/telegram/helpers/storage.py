from contextvars import ContextVar
from contextlib import contextmanager

from aiogram.contrib.fsm_storage.redis import RedisStorage2


class RedisStorage(RedisStorage2):
    _ctx_prefix = ContextVar('StorageDifferentPrefix', default=('fsm',))

    @property
    def _prefix(self):
        return self._ctx_prefix.get()

    @_prefix.setter
    def _prefix(self, value):
        pass

    @contextmanager
    def with_prefix(self, prefix: str):
        token = self._ctx_prefix.set((prefix,))
        try:
            yield
        finally:
            self._ctx_prefix.reset(token)
