import argparse
from colorama import Fore, Back, Style
import colorama
import sys

class TerminalHandler:

    __passed = 1
    __test_pass = 0

    def __init__(self):
        colorama.init()
        pass

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--username",dest ="username", help="User name", default=argparse.SUPPRESS, required=True)
        parser.add_argument("-p", "--password",dest = "password", help="Password", default=argparse.SUPPRESS, required=True)
        parser.add_argument("-i", "--ip",dest = "ip", help="IP address", default=argparse.SUPPRESS, required=True)
        args = parser.parse_args()
        return args

    def test_print(self, results):
        if self.__passed == 1:
            print('{}/{}:Tests Count                  '.format(self.__passed, results["count"]))
            print(Fore.BLUE + '{}/{}:Tests passed             '.format(self.__test_pass,results["count"])+Style.RESET_ALL )
            print('{}:The command under the test                '.format(results['name']))
            if results['status'] == True:
                print(Fore.GREEN + 'Passed:Test            '+Style.RESET_ALL , end="")
                self.__test_pass = self.__test_pass + 1
            else:
                print(Fore.RED + 'Failed:Test               '+Style.RESET_ALL , end="")
            sys.stdout.flush()
            self.__passed = self.__passed + 1

        else:
            if results['status'] == True:
                print(Fore.GREEN + '\rPassed:Test             '+Style.RESET_ALL )
                self.__test_pass = self.__test_pass + 1
            else:
                print(Fore.RED + '\rFailed:Test                    '+Style.RESET_ALL )
            print('\033[F\033[F{}:The command under the test                '.format(results['name']))
            print('\033[F\033[F{}/{}:Tests Passed/Count                     '.format(self.__passed, results["count"]))
            print(Fore.BLUE + '\033[F\033[F{}/{}:Tests passed                      '.format(self.__test_pass,results["count"])+Style.RESET_ALL )
            print()
            print()
            self.__passed = self.__passed + 1
            
        if self.__passed == results["count"]+1:
            print()