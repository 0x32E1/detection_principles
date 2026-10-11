from pynput import keyboard
import time
import statistics

def record_keystroke_intervals(expected_text):
    timestamps = []
    typed_chars = []

    def on_press(key):
        nonlocal timestamps, typed_chars

        try:
            char = key.char
        except AttributeError:
            return

        timestamps.append(time.time())
        typed_chars.append(char)

        if ''.join(typed_chars) == expected_text:
            return False  
            
    print(f"Введите строку: {expected_text}")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    intervals = [
        timestamps[i + 1] - timestamps[i]
        for i in range(len(timestamps) - 1)
    ]

    return intervals


def main():
    text = input("Введите любую строку для анализа: ")

    print("\nПервый ввод (эталон)")
    intervals_1 = record_keystroke_intervals(text)

    print("\nВторой ввод (проверка)")
    intervals_2 = record_keystroke_intervals(text)

    min_len = min(len(intervals_1), len(intervals_2))
    diffs = [
        abs(intervals_1[i] - intervals_2[i])
        for i in range(min_len)
    ]

    if len(diffs) < 2:
        print("Недостаточно данных для анализа")
        return

    deviation = statistics.mean(diffs)

    print(f"\nСреднее отклонение: {deviation:.3f}")

    if deviation > 0.1:
        print("Обнаружены отклонения в поведении. Возможно, вводил другой человек")
    else:
        print("Ввод соответствует исходному пользователю")


if __name__ == "__main__":
    main()
