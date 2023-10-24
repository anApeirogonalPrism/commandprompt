import sys
from time import sleep
from random import uniform
from datetime import datetime
from typing import Literal


class cmdp(object):
    def __init__(self) -> None:
        self.__cmdUseCount = 0
        self.__commands = sorted(
            [
                "pc version info",
                "change pc version info",
                "pc version",
                "pc platform",
                "time",
            ]
        )
        self.now = datetime.now()

        self.cr_counter = 0

    def copyright(self):
        print(
            "\n\033[0mCopyright (c) 2023-____ Torrez's Command Prompt Software Foundation."
        )
        print("All Rights Reserved.\n")
        sleep(1)

    def tips(self):
        print(
            "We recommend you to run this in the command prompt to enhance you experience\ninto Torrez's command prompt.\n"
        )
        sleep(1)

    def load(self, reason: str | Literal["s"]) -> None:
        if reason == "s":
            sleep(uniform(0, 1.5))
            print("\033[34m[\033[32m| \033[34m]\033[0m Fetching data...")
            sleep(uniform(0, 1.25))
            print("\033[34m[\033[32m||\033[34m]\033[0m Preparing results...\n")

    def addUseCount(self, amount: int | None = 1, /):
        self.__cmdUseCount += amount

    def resetUseCount(self, /):
        self.__cmdUseCount = 0

    def reqcmd(self, /):
        if self.cr_counter == 0:
            self.copyright()
            self.tips()
            self.cr_counter += 1

        reqd_cmd = input("PS C:\\Users\\user>").strip()
        if reqd_cmd in self.__commands:
            self.load("s")
            if reqd_cmd == self.__commands[0]:
                print(
                    f"version info: \n\tmajor: {_version_info.major}\n\tminor: {_version_info.minor}\n\tmicro: {_version_info.micro}\n"
                )
            if reqd_cmd == self.__commands[1]:
            if reqd_cmd == self.__commands[2]:
                print(f"Version: {_version()}")
            if reqd_cmd == self.__commands[3]:
                print(f"Platform: {sys.platform}")
            if reqd_cmd == self.__commands[4]:
                print(Time())
        else:
            print(
                "Sorry, it looks like you have entered something that the computer can't understand or identify.\n Please try again.\n"
            )


class Time:
    def __new__(self):
        cmd = cmdp()
        return f"Time: {cmd.now:%Y-%m-%d %H:%M:%S.%f}"


class _version:
    def __new__(self):
        vi = _version_info()
        return "{}.{}.{}".format(vi.major, vi.minor, vi.micro)


class _version_info:
    def __init__(self) -> None:
        self._major = 0
        self._minor = 0
        self._micro = 1

    @property
    def major(self) -> int:
        return self._major

    @property
    def minor(self) -> int:
        return self._minor

    @property
    def micro(self) -> int:
        return self._micro

    @major.setter
    def major(self, value: int):
        self._major = value

    @minor.setter
    def minor(self, value: int):
        self._minor = value

    @micro.setter
    def micro(self, value: int):
        self._micro = value


cmd = cmdp()


def main():
    cmd.reqcmd()


if __name__ == "__main__":
    main()
