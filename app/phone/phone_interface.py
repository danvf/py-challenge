from .phone_state import InitialScreen
from ..util import constants


class PhoneInterface:
    def __init__(self):
        self._state = InitialScreen
        print(constants.INITIAL_SCREEN)

    def switch_state(self, new_state):
        self._state = new_state
        self._state.context = self

    def press_button_call(self): self._state.button_call()

    def press_button_dismiss(self): self._state.button_dismiss()

    def flag_avatar_displayed(self): self._state.avatar_displayed()

    def flag_popup_no_network(self): self._state.popup_no_network()

    def flag_popup_call_dismissed(self): self._state.popup_call_dismissed()

    def flag_popup_ending_call(self): self._state.popup_ending_call()
