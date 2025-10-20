import time
import random
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
import multiprocessing

def ml_task(task_id: int):
    start = time.time()
    sleep_time = random.uniform(0.3, 2.5)
    time.sleep(sleep_time)  # Simuliert Rechenzeit
    duration = time.time() - start
    return task_id, duration, f"Task {task_id} done after {duration:.2f}s"


def run_parallel_tasks(num_tasks: int = 50, output_file: str = "done.txt"):
    with ProcessPoolExecutor() as executor, open(output_file, "a") as f:
        futures = [executor.submit(ml_task, i) for i in range(num_tasks)]
        for future in tqdm(as_completed(futures),
                           total=num_tasks,
                           desc="Processing tasks",
                           unit="task"):
            task_id, duration, msg = future.result()
            f.write(f"{msg}\n")
            f.flush()

    print("\n✅ All tasks completed successfully!")


if __name__ == "__main__":
    multiprocessing.freeze_support()  # macOS/Windows safety
    run_parallel_tasks(num_tasks=100)
