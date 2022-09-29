from contextvars import ContextVar
from contextlib import contextmanager
from typing import ContextManager

from aiogram.contrib.fsm_storage.redis import RedisStorage2


class RedisStorage(RedisStorage2):
    _ctx_prefix = ContextVar('StorageDifferentPrefix', default=('fsm',))
    __prefix = None

    @property
    def _prefix(self) -> tuple[str]:
        return self._ctx_prefix.get(self.__prefix)

    @_prefix.setter
    def _prefix(self, value: str) -> None:
        self.__prefix = (value,)

    @contextmanager
    def with_prefix(self, prefix: str) -> ContextManager[None]:
        token = self._ctx_prefix.set((prefix,))
        try:
            yield
        finally:
            self._ctx_prefix.reset(token)
