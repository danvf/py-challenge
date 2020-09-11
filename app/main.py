import sys
from phone.phone_interface import PhoneInterface
from io_manager import read_input
from io_manager import write_output


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    my_phone = PhoneInterface()
    output_text = read_input(input_file, my_phone)
    write_output(output_file, output_text)


if __name__ == "__main__":
    main()
