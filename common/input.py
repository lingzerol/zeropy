import platform
import time
import sys

if platform.system() == "Windows":
    import msvcrt
elif platform.system() == "Linux":
    import select


class PlatFormError(RuntimeError):
    """PlatForm error that present code cannot run in this platform"""

    def __init__(self, args):
        self.args = args


def input_with_timeout(timeout):
    if platform.system() == "Windows":
        endtime = time.time() + timeout
        result = []
        while time.time() < endtime:
            if msvcrt.kbhit():
                endtime = time.time() + timeout
                result.append(msvcrt.getwche())
                if result[-1] == '\n' or result[-1] == '\r':
                    print("")
                    return ''.join(result[:-1])
            time.sleep(0.04)
        print("")
    elif platform.system() == "Linux":
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            return sys.stdin.readline().rstrip('\n')
        else:
            print("")
    else:
        raise PlatFormError("unsuitable platform.")
    return ""
