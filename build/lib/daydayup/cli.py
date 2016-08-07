
import sys
from daydayup.core import DayDayUp
from daydayup.exception import DayDayUpException


def CLI():
    try:
        DayDayUp()
    except DayDayUpException as e:
        sys.stderr.write(str(e))
        return e.code
    return 0


if __name__ == "__main__":
    sys.exit(CLI())
