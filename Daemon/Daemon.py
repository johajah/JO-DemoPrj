import argparse
import queue
import time
import sys
import atexit


class Daemon:
    def __init__(self, args):
        self.args = self.parse_args(args)
        self.actions = queue.Queue()

    @staticmethod
    def parse_args(args):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--interval", action="store", type=int, default=5, help="Polling Interval")
        return parser.parse_args(args)

    def run_daemon(self):

        while self.okay_to_run():
            self.find_actions()
            if not self.actions.empty():
                while not self.actions.empty():
                    action = self.actions.get()
                    self.perform_actions(action)
                    self.actions.task_done()
            else:
                print(f"Sleeping for {self.args.interval}")
                time.sleep(self.args.interval)


    def okay_to_run(self):
        return True

    def find_actions(self):
        print("Finding Actions")

    def perform_actions(self, action):
        print(f"Performing Action: {action}")


@atexit.register
def finished():
    print("Daemon shutting down")


def main():
    count = 0
    while count < 10:
        args = sys.argv[1:]
        Daemon(args).run_daemon()
        count += 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
