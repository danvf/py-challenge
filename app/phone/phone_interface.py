from phone.phone_states import InitialState

from util import constants


class PhoneInterface:
    def __init__(self):
        self._state = InitialState()
        self._state.context = self

    def switch_state(self, new_state):
        self._state = new_state
        self._state.context = self

    def press_button_call(self) -> str:
        return self._state.button_call()

    def press_button_dismiss(self) -> str:
        return self._state.button_dismiss()

    def flag_avatar_displayed(self) -> str:
        return self._state.avatar_displayed()

    def flag_popup_no_network(self) -> str:
        return self._state.popup_no_network()

    def flag_popup_call_dismissed(self) -> str:
        return self._state.popup_call_dismissed()

    def flag_popup_ending_call(self) -> str:
        return self._state.popup_ending_call()
