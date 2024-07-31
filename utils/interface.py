#!/usr/bin/env python3

"""
Logging and text interface related code.
"""


class bcolors:
    HEADER = "\033[34m"
    OK_YELLOW = "\033[33m"
    OK_BLUE = "\033[94m"
    OK_CYAN = "\033[96m"
    OK_GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class loglevel:
    INFO = ("i", bcolors.OK_CYAN)
    WARN = ("!", bcolors.WARNING)
    INPUT = ("?", bcolors.OK_BLUE)
    DEBUG = ("D", bcolors.OK_BLUE)
    DONE = ("✔︎", bcolors.OK_GREEN)


def color_print(color: bcolors, msg: str):
    """
    Print a string with the selected color.
    """
    print(f"{color}{msg}{bcolors.ENDC}")


def log(level: loglevel, msg: str):
    """
    Print a string with the selected log level.
    """
    print(f"[{level[1]}{level[0]}{bcolors.ENDC}] {msg}")


def log_info(msg: str):
    """
    Print an info string.
    """
    log(loglevel.INFO, msg)


def log_warn(msg: str):
    """
    Print a warning string.
    """
    log(loglevel.WARN, msg)

def log_done(msg: str):
    """
    Print an done string.
    """
    log(loglevel.DONE, msg)


def input_yn(msg: str) -> bool:
    """
    Get a yes/no answer to a prompt.
    """
    log(loglevel.INPUT, msg)
    option = input("[Y/n] ") or "y"
    return option.lower() in ("y", "yes")

"""
BLACK  => "\033[30m",
RED    => "\033[31m",
GREEN  => "\033[32m",
YELLOW => "\033[33m",
BLUE   => "\033[34m",
PURPLE => "\033[35m",
CYAN   => "\033[36m",
WHITE  => "\033[37m",

# background color
BLACKB  => "\033[40m",
REDB    => "\033[41m",
GREENB  => "\033[42m",
YELLOWB => "\033[43m",
BLUEB   => "\033[44m",
PURPLEB => "\033[45m",
CYANB   => "\033[46m",
WHITEB  => "\033[47m",

# bold
B    => "\033[1m",
BOFF => "\033[22m",

# italics
I => "\033[3m",
IOFF => "\033[23m",

# underline
U => "\033[4m",
UOFF => "\033[24m",

# invert
R => "\033[7m",
ROFF => "\033[27m",

# reset
RESET  => "\033[0m",
"""