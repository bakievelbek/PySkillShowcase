"""

An iterator in Python is an object that can be iterated upon, meaning that you can traverse through all the values. Technically, in Python, an iterator is an object which implements the iterator protocol, which consists of the methods __iter__() and __next__().
Key Characteristics of Iterators:

    Iterable: An object is called iterable if we can get an iterator from it. Most built-in containers in Python like lists, tuples, strings etc. are iterables.

    Iteration: The process of looping through the objects or items is known as iteration.

    __iter__() method: This method returns an iterator from an iterable. It is implemented by an iterable object.

    __next__() method: This method returns the next item from the iterator. When there are no more items to return, it raises a StopIteration exception.

How Iterators Work:

    First, the __iter__() method is called on the iterable object to create an iterator.
    Then, the __next__() method is repeatedly called on the iterator object to get each item until the StopIteration exception is raised.

"""


import time
from memory_profiler import profile

start_time = time.time()


class LogEntry:
    def __init__(self, date, time, user_id, action):
        self.date = date
        self.time = time
        self.user_id = user_id
        self.action = action

    @classmethod
    def from_line(cls, line):
        parts = line.strip().split()
        return cls(parts[0], parts[1], parts[2], parts[3])


class LogFileIterator:
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        return self

    def __next__(self):
        if not hasattr(self, '_file'):
            self._file = open(self.filename, 'r')
        line = self._file.readline()
        if line:
            return LogEntry.from_line(line)
        else:
            self._file.close()
            raise StopIteration


def count_login_per_day_with_iterator(filename):
    log_entries = LogFileIterator(filename)
    login_counts = {}
    for entry in log_entries:
        if entry.action == "LOGIN":
            if entry.date not in login_counts:
                login_counts[entry.date] = 0
            login_counts[entry.date] += 1

    return login_counts


# Example Usage
log_file = "./large_log_file.log"
result = count_login_per_day_with_iterator(log_file)
for date, count in result.items():
    print(f"On {date}, there were {count} logins.")

end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")
