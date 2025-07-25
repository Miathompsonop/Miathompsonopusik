import datetime
import random

def generate_fake_log():
    verbs = ["Fix", "Add", "Update", "Refactor", "Remove"]
    objects = ["RPC handler", "CLI argument", "token logic", "output format", "validator check"]
    context = ["flow", "support", "logic", "path", "branch"]

    verb = random.choice(verbs)
    obj = random.choice(objects)
    ctx = random.choice(context)

    return f"{verb} {obj} in {ctx}"

if __name__ == "__main__":
    now = datetime.datetime.now().isoformat()
    log_entry = f"[AUTO LOG] {now} — {generate_fake_log()}"
    print(log_entry)

    with open("log.txt", "a") as f:
        f.write(log_entry + "\n")
