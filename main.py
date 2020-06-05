import sys
import work_with_users
import instructions
import test
import file_instruction


def main():
    try:
        test.tests()
    except AssertionError:
        print('Problem with tests')
        sys.exit()
    instructions.instructions()
    file_instruction.file_instruction()
    flag = True
    while flag:
        work_with_users.cli_interface()
        k = input("\nWant to continue?\n(yes/no/help me): ")
        if k == 'yes':
            flag = True
        elif k == 'no':
            flag = False
        elif k == 'help me':
            instructions.instructions()
            flag = True


if __name__ == '__main__':
    main()
