from abc import ABC, abstractmethod
from .phone import PhoneInterface


class PhoneActions(ABC):

    @property
    def context(self) -> PhoneInterface:
        return self._context

    @context.setter
    def context(self, context: PhoneInterface) -> None:
        self._context = context

    @abstractmethod
    def button_call(self, phone): pass

    @abstractmethod
    def button_dismiss(self, phone): pass

    @abstractmethod
    def avatar_displayed(self, phone): pass

    @abstractmethod
    def popup_no_network(self, phone): pass

    @abstractmethod
    def popup_call_dismissed(self, phone): pass

    @abstractmethod
    def popup_ending_call(self, phone): pass
