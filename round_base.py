import re
from dataclasses import dataclass

@dataclass
class Round:
    title: str
    chapter: str
    task: str
    examples: str
    hint: str
    clue: str
    kind: str
    tests: list
    replacement: str = "[СКРЫТО]"

    def check(self, pattern: str):
        try:
            regex = re.compile(pattern)
        except re.error as error:
            return False, f"Синтаксическая ошибка в регулярном выражении: {error}"

        if self.kind == "fullmatch":
            for value, expected in self.tests:
                actual = regex.fullmatch(value) is not None
                if actual != expected:
                    state = "принят" if actual else "отклонён"
                    wanted = "должен быть принят" if expected else "должен быть отклонён"
                    return False, f"Контрпример: {value!r}. Ваш шаблон {state} эту строку, но она {wanted}."
            return True, "Все проверочные строки обработаны правильно."

        if self.kind == "finditer":
            for text, expected in self.tests:
                actual = [match.group(0) for match in regex.finditer(text)]
                if actual != expected:
                    return False, f"Контрпример: {text!r}.\\nОжидалось: {expected}\\nПолучено:  {actual}"
            return True, "Во всех сообщениях найдены ровно нужные номера дел."

        if self.kind == "sub":
            for text, expected in self.tests:
                actual = regex.sub(self.replacement, text)
                if actual != expected:
                    return False, f"Контрпример: {text!r}.\\nОжидалось после замены: {expected!r}\\nПолучено: {actual!r}"
            return True, "Во всех фрагментах конфиденциальные данные скрыты правильно."

        return False, "Неизвестный тип проверки."
