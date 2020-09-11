from phone.phone_interface import PhoneInterface


def main():
    my_phone = PhoneInterface()
    my_phone.press_button_call()
    my_phone.press_button_dismiss()
    my_phone.flag_popup_call_dismissed()
    my_phone.flag_avatar_displayed()
    my_phone.press_button_call()
    my_phone.flag_avatar_displayed()
    my_phone.flag_avatar_displayed()


if __name__ == "__main__":
    main()
