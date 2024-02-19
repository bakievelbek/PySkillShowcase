"""

A generator in Python is a special type of iterator, a function that enables you to declare a kind of iterator, known
as a generator object. It allows you to write a function that can yield multiple values over time, returning a value
each time it's paused and resumed. Generators are implemented using functions that use the yield statement.

Key Characteristics of Generators:

    Lazy Evaluation: Generators generate values on the fly and do not store them in memory. This means they are very
    memory efficient when dealing with large datasets.

    Stateful: They remember where they left off between executions.

    yield Statement: Instead of returning a value and exiting like a normal function, a generator function uses yield
    to provide a value to the code that has called the generator. After yielding the value, the generator's state is
    paused, and it can be resumed later to continue from where it left off.

    Iterable: Generators are a kind of iterable, like lists or tuples. However, you can only iterate over their
    elements once.

    End of Iteration: When a generator function runs out of values to yield, or if a return statement is executed
    (without a value), it raises a StopIteration exception, signaling that the iteration should end.

The example below show that decorator can be useful where we do not have enough memory, it can increase execution
time but in case where it is required to save the memory in reads the long file line by line instead of uploading
it in memory fully

"""

import time
from memory_profiler import profile

start_time = time.time()


def log_entries_gen(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line


@profile
def count_login_per_day(filename):
    log_entries = log_entries_gen(filename)
    login_counts = {}

    for entry in log_entries:
        parts = entry.strip().split()
        date, user_id, action = parts[0], parts[1], parts[2]
        if action == "LOGIN":
            if date not in login_counts:
                login_counts[date] = 0
            login_counts[date] += 1

    return login_counts


# Example Usage
log_file = "./large_log_file.log"
result = count_login_per_day(log_file)
for date, count in result.items():
    print(f"On {date}, there were {count} logins.")

end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")

# Python code to
# demonstrate readlines()


# Using readlines()
file1 = open('./large_log_file.log', 'r')
Lines = file1.readlines()

count = 0


# Strips the newline character
@profile()
def strips():
    for line in Lines:
        global count
        count += 1
        # print(line.split())
        # print("Line{}: {}".format(count, line.strip()))


start_time = time.time()
strips()
end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")

"""
Result:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    14     19.2 MiB     19.2 MiB           1   @profile
    15                                         def count_login_per_day(filename):
    16     19.2 MiB      0.0 MiB           1       log_entries = log_entries_gen(filename)
    17     19.2 MiB      0.0 MiB           1       login_counts = {}
    18                                         
    19     19.5 MiB -21676.4 MiB     1000001       for entry in log_entries:
    20     19.5 MiB -21676.6 MiB     1000000           parts = entry.strip().split()
    21     19.5 MiB -21676.6 MiB     1000000           date, user_id, action = parts[0], parts[1], parts[2]
    22     19.5 MiB -21676.6 MiB     1000000           if action == "LOGIN":
    23                                                     if date not in login_counts:
    24                                                         login_counts[date] = 0
    25                                                     login_counts[date] += 1
    26                                         
    27     19.4 MiB     -0.1 MiB           1       return login_counts


Time taken: 102.1939742565155 seconds
Filename: E:\Pycharm Projects\PySkillShowcase\generators.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    52    108.9 MiB    108.9 MiB           1   @profile()
    53                                         def strips():
    54    108.9 MiB  -9338.5 MiB     1000001       for line in Lines:
    55                                                 global count
    56    108.9 MiB  -9338.5 MiB     1000000           count += 1


Time taken: 48.37473201751709 seconds

"""
