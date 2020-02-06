import platform
import time
import sys

if platform.system() == "Windows":
    import msvcrt

    def input_with_timeout(timeout, prompt="", timer=time.monotonic):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        endtime = timer() + timeout
        result = []
        while timer() < endtime:
            if msvcrt.kbhit():
                endtime = timer() + timeout
                result.append(msvcrt.getwche())
                if result[-1] == '\n' or result[-1] == '\r':
                    print("")
                    return ''.join(result[:-1])
            time.sleep(0.04)
        print("")
        return ""
elif platform.system() == "Linux":
    import select

    def input_with_timeout(timeout, prompt=""):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            return sys.stdin.readline().rstrip('\n')
        else:
            print("")
        return ""
