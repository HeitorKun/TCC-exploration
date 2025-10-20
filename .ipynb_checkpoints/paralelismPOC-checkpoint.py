import time
import random
from concurrent.futures import ProcessPoolExecutor

def ml_task(i):
    print(f"Running task {i}")
    time.sleep(random.uniform(0.12, 3.2))
    return f"Task {i} done"

def main():
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(ml_task, range(102)))

    with open("done.txt", "a") as f:
        for r in results:
            f.write(r + "\n")

    print("All tasks completed!")

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # especially for macOS/Windows safety
    main()
