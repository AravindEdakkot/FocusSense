import numpy as np

def extract_features(df):
    times = df["time"].values

    # Convert ms → seconds properly
    delays = np.diff(times) / 1000.0  

    if len(delays) == 0:
        return [0, 0, 0, 0, 0]

    total_time_sec = (times[-1] - times[0]) / 1000.0

    # ✅ FIXED WPM (use words, not characters)
    words = len(df) / 5  # standard rule
    wpm = words / (total_time_sec / 60 + 1e-5)

    avg_delay = np.mean(delays)
    variance = np.var(delays)

    # Better pause threshold
    pause_count = np.sum(delays > 1.0)

    backspaces = sum(1 for k in df["key"] if k == "Backspace")
    backspace_rate = backspaces / len(df)

    return [wpm, avg_delay, pause_count, backspace_rate, variance]