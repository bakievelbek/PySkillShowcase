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
