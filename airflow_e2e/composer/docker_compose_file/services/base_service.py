import typing
from abc import ABC, abstractmethod


class BaseService(ABC):
    @property
    @abstractmethod
    def data(self) -> typing.Dict:
        raise NotImplementedError("to be implemented")
