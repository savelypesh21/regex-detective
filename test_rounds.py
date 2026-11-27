from rounds import ROUNDS, run_self_tests


def test_all_rounds_accept_intended_patterns():
    patterns = [
        r"[A-Z]{2}-\d{3}",
        r"[ABC]\d{2}[A-Z]",
        r"CASE-\d{4}(?!\d)",
        r"ID:[A-Z]{2}\d{3}",
    ]
    assert len(ROUNDS) == 4
    for round_data, pattern in zip(ROUNDS, patterns):
        assert round_data.check(pattern)[0] is True


def test_invalid_syntax_does_not_crash():
    for round_data in ROUNDS:
        success, message = round_data.check("[")
        assert success is False
        assert "Синтаксическая ошибка" in message


def test_wrong_pattern_is_rejected():
    assert ROUNDS[0].check(r"\d+")[0] is False
    assert ROUNDS[2].check(r"ABC")[0] is False


if __name__ == "__main__":
    run_self_tests()
    test_all_rounds_accept_intended_patterns()
    test_invalid_syntax_does_not_crash()
    test_wrong_pattern_is_rejected()
    print("Все тесты пройдены.")
