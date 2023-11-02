import random
import datetime


def generate_log_file(filename, num_entries):
    actions = ["LOGIN", "LOGOUT", "ERROR", "INFO"]
    with open(filename, 'w') as f:
        for _ in range(num_entries):
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            user_id = random.randint(1000, 9999)
            action = random.choice(actions)
            f.write(f"{date} {user_id} {action}\n")


# Usage
generate_log_file("large_log_file.log", 1000000)
