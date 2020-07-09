# Utility logging functions
class CLRS:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def _log_prompt(string):
    prompt = "#" * 10
    _log(f"\n{prompt} {string} {prompt}", CLRS.BOLD)


def _log_paragraph(data):
    _log(data, CLRS.OKBLUE)


def _log_fail(data):
    _log(data, CLRS.FAIL)


def _log_pass(data):
    _log(data, CLRS.OKGREEN)


def _log(string, clr):
    print(f"{clr} {string} {CLRS.ENDC}")
