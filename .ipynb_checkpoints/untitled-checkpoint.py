import threading
from queue import Queue
import random

write_queue = Queue()

def writer(output_file):
    with open(output_file, "a") as f:
        while True:
            item = write_queue.get()
            if item is None:  # shutdown signal
                break
            f.write(item + "\n")
            f.flush()

def worker(work_id):
    # simulate work
    result = f"Work {work_id} done"
    delay = random.uniform(0.01, 1.12)
    time.sleep(delay)
    write_queue.put(result)

# Start the writer thread
t_writer = threading.Thread(target=writer, args=("done.txt",), daemon=True)
t_writer.start()

# Start workers
threads = [threading.Thread(target=worker, args=(i,)) for i in range(100000)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# Stop writer
write_queue.put(None)
t_writer.join()
