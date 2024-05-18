import time


class Engine:
    def __init__(self):
        pass

    def my_task_loop(self) -> str:
        BIG_NUMBER = 1_000_000_000
        for i in range(BIG_NUMBER):
            if i % (BIG_NUMBER // 20) == 0:
                print(f"{i / BIG_NUMBER * 100:.0f}%")
        print("Done!")
        return "Loop task done!"

    def my_task_sleep(self, seconds: int) -> str:
        print(f"Sleeping for {seconds} seconds...")
        time.sleep(seconds)
        print("Done sleeping!")
        return "Sleep task done!"


if __name__ == "__main__":
    task = Engine()
    task.my_task_sleep()
