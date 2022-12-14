import queue
import time
import threading
import random


def data_sender(q: queue.Queue, identifier):
    while True:
        q.put({'identifier': identifier,
               'temperature': random.randint(22, 32),
               'humidity': random.randint(45, 55),
               'timestamp': int(time.time())})

        time.sleep(1)


def main():
    q = queue.Queue()

    data_senders_count = 2

    for identifier in range(data_senders_count):
        threading.Thread(target=data_sender, args=(q, identifier)).start()

    while True:
        print(q.get())

        q.task_done()


if __name__ == '__main__':
    main()