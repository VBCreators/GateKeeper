import threading
import time

stopper = False


def thread_function(name):
    count = 0
    while stopper is not True:
        count += 1
        print(f"{name} : {count}")
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=thread_function, args=("thread-1",))
    t2 = threading.Thread(target=thread_function, args=("thread-2",))
    t1.start()
    t2.start()
    print("Press enter when you want to stop the threads")
    input()
    stopper = True
