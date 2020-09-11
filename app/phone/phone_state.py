from abc import ABC, abstractmethod
from ..util import constants


class PhoneActions(ABC):

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
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


class InitialScreen(PhoneActions):
    def button_call(self):
        print(constants.INTERMEDIATE_SCREEN)
        self.context.switch_state(IntermediateScreen)

    def button_dismiss(self):
        print(constants.INPUT_ERROR)

    def avatar_displayed(self):
        print(constants.INPUT_ERROR)

    def popup_no_network(self):
        print(constants.INPUT_ERROR)

    def popup_call_dismissed(self):
        print(constants.INPUT_ERROR)

    def popup_ending_call(self):
        print(constants.INPUT_ERROR)


class IntermediateScreen(PhoneActions):
    def button_call(self):
        print(constants.INPUT_ERROR)

    def button_dismiss(self):
        print(constants.INITIAL_SCREEN)
        self.context.switch_state(InitialScreen)

    def avatar_displayed(self):
        print(constants.CALL_SCREEN)
        self.context.switch_state(CallScreen)

    def popup_no_network(self):
        print(constants.INITIAL_SCREEN)
        self.context.switch_state(InitialScreen)

    def popup_call_dismissed(self):
        print(constants.INITIAL_SCREEN)
        self.context.switch_state(InitialScreen)

    def popup_ending_call(self):
        print(constants.INPUT_ERROR)


class CallScreen(PhoneActions):
    def button_call(self):
        print(constants.INPUT_ERROR)

    def button_dismiss(self):
        print(constants.INITIAL_SCREEN)
        self.context.switch_state(InitialScreen)

    def avatar_displayed(self):
        print(constants.INPUT_ERROR)

    def popup_no_network(self):
        print(constants.INITIAL_SCREEN)
        self.context.switch_state(InitialScreen)

    def popup_call_dismissed(self):
        print(constants.INITIAL_SCREEN)
        self.context.switch_state(InitialScreen)

    def popup_ending_call(self):
        print(constants.INITIAL_SCREEN)
        self.context.switch_state(InitialScreen)
