from abc import ABC, abstractmethod
from util import constants


class PhoneActions(ABC):

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def button_call(self, phone) -> str: pass

    @abstractmethod
    def button_dismiss(self, phone) -> str: pass

    @abstractmethod
    def avatar_displayed(self, phone) -> str: pass

    @abstractmethod
    def popup_no_network(self, phone) -> str: pass

    @abstractmethod
    def popup_call_dismissed(self, phone) -> str: pass

    @abstractmethod
    def popup_ending_call(self, phone) -> str: pass


class InitialScreen(PhoneActions):
    def button_call(self) -> str:
        self.context.switch_state(IntermediateScreen())
        return constants.INTERMEDIATE_SCREEN

    def button_dismiss(self) -> str:
        return constants.INPUT_ERROR

    def avatar_displayed(self) -> str:
        return constants.INPUT_ERROR

    def popup_no_network(self) -> str:
        return constants.INPUT_ERROR

    def popup_call_dismissed(self) -> str:
        return constants.INPUT_ERROR

    def popup_ending_call(self) -> str:
        return constants.INPUT_ERROR


class IntermediateScreen(PhoneActions):
    def button_call(self) -> str:
        return constants.INPUT_ERROR

    def button_dismiss(self) -> str:
        self.context.switch_state(InitialScreen())
        return constants.INITIAL_SCREEN

    def avatar_displayed(self) -> str:
        self.context.switch_state(CallScreen())
        return constants.CALL_SCREEN

    def popup_no_network(self) -> str:
        self.context.switch_state(InitialScreen())
        return constants.INITIAL_SCREEN

    def popup_call_dismissed(self) -> str:
        self.context.switch_state(InitialScreen())
        return constants.INITIAL_SCREEN

    def popup_ending_call(self) -> str:
        return constants.INPUT_ERROR


class CallScreen(PhoneActions):
    def button_call(self) -> str:
        return constants.INPUT_ERROR

    def button_dismiss(self) -> str:
        self.context.switch_state(InitialScreen())
        return constants.INITIAL_SCREEN

    def avatar_displayed(self) -> str:
        return constants.INPUT_ERROR

    def popup_no_network(self) -> str:
        self.context.switch_state(InitialScreen())
        return constants.INITIAL_SCREEN

    def popup_call_dismissed(self) -> str:
        self.context.switch_state(InitialScreen())
        return constants.INITIAL_SCREEN

    def popup_ending_call(self) -> str:
        self.context.switch_state(InitialScreen())
        return constants.INITIAL_SCREEN
