from phone.phone_interface import PhoneInterface
from util import constants


def read_input(input_file, phone: PhoneInterface) -> str:
    input_text = ''
    output_text = []

    use_phone = {
        constants.PRESS_BUTTON_CALL: phone.press_button_call(),
        constants.PRESS_BUTTON_DISMISS: phone.press_button_dismiss(),
        constants.FLAG_AVATAR_DISPLAYED: phone.flag_avatar_displayed(),
        constants.FLAG_POPUP_NO_NETWORK: phone.flag_popup_no_network(),
        constants.FLAG_POPUP_CALL_DISMISSED: phone.flag_popup_call_dismissed(),
        constants.FLAG_POPUP_ENDING_CALL: phone.flag_popup_ending_call(),
    }

    with open(input_file, 'r') as i:
        input_text = i.read()

    for input_line in input_text.splitlines():
        next_entry = input_line.lower()
        if next_entry in use_phone:
            output_text.append(use_phone[next_entry])
        else:
            output_text.append(constants.NONEXISTENT_INPUT)
        output_text.append('\n')

    return ''.join(output_text)


def write_output(output_file, output_text) -> None:
    with open(output_file, 'w') as o:
        o.truncate(0)
        o.write(output_text)
