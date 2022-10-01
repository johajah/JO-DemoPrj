from lib.Daemon.Daemon import Daemon
import sys
import atexit


class Event(Daemon):
    def find_actions(self):
        pass


@atexit.register
def finished():
    print("Daemon shutting down")


def main():
    args = sys.argv[1:]
    Daemon(args).run_daemon()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
