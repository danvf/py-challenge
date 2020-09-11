from .phone_actions import PhoneActions
from .util import constants


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
