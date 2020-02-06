import platform
import time
import sys

if platform.system() == "Windows":
    import msvcrt

    def input_with_timeout(prompt, timeout, timer=time.monotonic):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        endtime = timer() + timeout
        result = []
        while timer() < endtime:
            if msvcrt.kbhit():
                result.append(msvcrt.getwche())
                if result[-1] == '\n' or result[-1] == '\r':
                    return ''.join(result[:-1])
            time.sleep(0.04)
        print("")
        return ""
elif platform.system() == "Linux":
    import select

    def input_with_timeout(prompt, timeout):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            return sys.stdin.readline().rstrip('\n')
        else:
            print("")
        return ""


def read(in_stream=sys.stdin):
    result = []
    c = in_stream.read(1)
    while c != "\t" and c != " " and c != "\n" and c != "\r" or len(result) == 0:
        if c != "\t" and c != " " and c != "\n" and c != "\r":
            result.append(c)
        c = in_stream.read(1)
    return "".join(result)
