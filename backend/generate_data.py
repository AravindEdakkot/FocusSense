import csv
import random

def generate_session(session_id, label):
    rows = []
    time = 1000

    for i in range(30):  # 30 keystrokes per session
        key = random.choice(list("abcdefghijklmnopqrstuvwxyz "))

        # ✅ Focused: fast + smooth (NO spikes)
        if label == "Focused":
            r = random.random()

            if r < 0.4:
                delay = random.uniform(70, 120)   # ultra fast
            elif r < 0.8:
                delay = random.uniform(120, 200)  # normal fast
            else:
                delay = random.uniform(200, 300)  # slightly slower

            delay += random.uniform(-15, 15)

        # 😵 Distracted: medium + irregular spikes
        elif label == "Distracted":
            delay = random.uniform(250, 500)
            if random.random() < 0.3:
                delay += random.uniform(300, 800)  # pause spike

        # 😴 Fatigued: slow + heavy delays
        else:
            delay = random.uniform(600, 1200)
            if random.random() < 0.4:
                delay += random.uniform(500, 1200)

        # Ensure delay is positive
        delay = max(50, delay)

        time += int(delay)

        rows.append([session_id, key, time, label])

    return rows


def generate_dataset(filename="real_data.csv", sessions_per_class=100):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["session_id", "key", "time", "label"])

        session_id = 1

        for label in ["Focused", "Distracted", "Fatigued"]:
            for _ in range(sessions_per_class):
                rows = generate_session(session_id, label)
                writer.writerows(rows)
                session_id += 1

    print("✅ Dataset generated successfully!")


if __name__ == "__main__":
    generate_dataset()