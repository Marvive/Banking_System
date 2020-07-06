import random


class Bank:
    def __init__(self):
        self.account_dict = {}
        self.major_industry_id = "4"
        self.bank_id_num = "400000"

    # Must be 16 chars long
    # card_num = "5304464212345678"

    # Must 4
    # major_industry_id = card_num[0]

    # must be 400000
    # bank_id_num = card_num[0:6]

    # must be 9 digits
    # account_id = card_num[7:15]
    # account_id = random.randrange()
    # any num
    # checksum = card_num[15]
    # checksum = random.randrange()
    @staticmethod
    def _print_new_card_details(card_number, pin_code):
        print(f"""
Your card has been created
Your card number:
{card_number}
Your card PIN:
{pin_code}
""")

    @staticmethod
    def _print_open_screen():
        print("""1. Create an account
2. Log into account
0. Exit""")

    @staticmethod
    def _print_validated_options():
        print("""
1. Balance
2. Log out
0. Exit""")

    @staticmethod
    def _gen_checksum():
        return str(random.randrange(0, 9))

    @staticmethod
    def _gen_pin_code():
        return "".join(map(str, random.sample(range(0, 10), 4)))

    @staticmethod
    def _gen_account_id():
        return "".join(map(str, random.sample(range(0, 10), 9)))

    def generate_card_number(self):
        account_id = self._gen_account_id()
        checksum = self._gen_checksum()
        return "".join([self.bank_id_num, account_id, checksum])

    def bank_menu(self):
        choice_1 = None
        while choice_1 != 0:
            self._print_open_screen()
            choice_1 = int(input())

            if choice_1 == 1:
                new_card_num = self.generate_card_number()
                new_pin_code = self._gen_pin_code()
                self.account_dict[new_card_num] = new_pin_code
                self._print_new_card_details(new_card_num, new_pin_code)
            elif choice_1 == 2:
                print()
                card_num = input("Enter your card number:").strip()
                card_pin = input("Enter your PIN:").strip()
                if card_num in self.account_dict.keys() and card_pin == self.account_dict[card_num]:
                    validated = True
                else:
                    validated = False

                if validated:
                    print("You have successfully logged in!")

                    validated_choice = None
                    while validated_choice != 0 and validated_choice != 2:
                        self._print_validated_options()
                        validated_choice = int(input())
                        print()
                        if validated_choice == 1:
                            print("Balance: 0")
                        elif validated_choice == 2:
                            print("You have successfully logged out!")
                        else:
                            choice_1 = 0
                else:
                    print("Wrong card number or PIN!")
                    print()
            if choice_1 == 0:
                print()
                print("Bye!")
                break


main_bank = Bank()
main_bank.bank_menu()
