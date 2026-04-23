import numpy as np

def extract_sequence(df, window_size=8, step=2):
    sequences = []

    for i in range(0, len(df) - window_size + 1, step):
        window = df.iloc[i:i+window_size]

        times = window["time"].values
        keys = window["key"].values

        # 🔹 Compute delays (in seconds)
        delays = np.diff(times) / 1000.0

        # Skip invalid windows
        if len(delays) < 2:
            continue

        # 🔹 Filter unrealistic values
        delays = delays[(delays > 0.05) & (delays < 2)]

        if len(delays) < 2:
            continue

        # 🔹 Total time
        total_time = (times[-1] - times[0]) / 1000.0

        # 🔹 Features
        #wpm = min(120, (len(window)/5) / (total_time/60 + 1e-5))  # capped
        avg_delay = np.mean(delays)
        pause = np.sum(delays > 0.5)
        #error = np.sum(keys == "Backspace") / len(window)
        variance = np.var(delays)

        sequences.append([
            avg_delay,
            pause,
            variance
        ])

    return np.array(sequences)