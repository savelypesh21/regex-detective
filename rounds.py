from passes import ROUNDS as PASSES_ROUNDS
from archive import ROUNDS as ARCHIVE_ROUNDS

# В команде два участника: по два раунда на каждого.
ROUNDS = PASSES_ROUNDS + ARCHIVE_ROUNDS


def run_self_tests():
    # Глава 1: Бюро пропусков
    assert PASSES_ROUNDS[0].check(r"[A-Z]{2}-\d{3}")[0] is True
    assert PASSES_ROUNDS[0].check(r"[A-Z]+-\d{3}")[0] is False
    assert PASSES_ROUNDS[0].check(r"[A-Z]{2}-[")[0] is False

    # Глава 2: Архив переписки
    assert ARCHIVE_ROUNDS[0].check(r"CASE-\d{4}(?!\d)")[0] is True
    assert ARCHIVE_ROUNDS[0].check(r"\d+")[0] is False
    assert ARCHIVE_ROUNDS[0].check(r"CASE-[")[0] is False

    return True


if __name__ == "__main__":
    run_self_tests()
    print("Все автоматические проверки пройдены.")
