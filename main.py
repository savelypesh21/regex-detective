"""Консольная версия Regex-детектива."""
from rounds import ROUNDS, run_self_tests


def play_round(round_data, number):
    print("\n" + "=" * 60)
    print(f"ДЕЛО № {number}: {round_data.title}")
    print(round_data.chapter)
    print("-" * 60)
    print(round_data.task)
    print("\nПримеры:")
    print(round_data.examples)

    hint_used = False
    while True:
        pattern = input("\nВведите регулярное выражение (или ? для подсказки): ").strip()

        if pattern == "?":
            print("Подсказка:", round_data.hint)
            hint_used = True
            continue

        success, message = round_data.check(pattern)
        print("\n" + message)

        if success:
            print("\nУЛИКА ПОЛУЧЕНА!")
            print(round_data.clue)
            return

        print("Попробуйте исправить выражение и ввести его ещё раз.")


def main():
    run_self_tests()
    print("=== REGEX-ДЕТЕКТИВ ===")
    print("Ваша задача — раскрыть дело, решая задания с регулярными выражениями.")

    for index, round_data in enumerate(ROUNDS, start=1):
        play_round(round_data, index)

    print("\n" + "=" * 60)
    print("ДЕЛО РАСКРЫТО!")
    print("Вы собрали все улики и успешно завершили расследование.")


if __name__ == "__main__":
    main()
