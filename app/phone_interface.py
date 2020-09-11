from .phone_screens import InitialScreen


class PhoneInterface:
    def __init__(self):
        self.state = InitialScreen

    def switch_state(self, new_state):
        self.state = new_state
        self.state.context = self

    def press_button_call(self): self.state.button_call()

    def press_button_dismiss(self): self.state.button_dismiss()

    def flag_avatar_displayed(self): self.state.avatar_displayed()

    def flag_popup_no_network(self): self.state.popup_no_network()

    def flag_popup_call_dismissed(self): self.state.popup_call_dismissed()

    def flag_popup_ending_call(self): self.state.popup_ending_call()
