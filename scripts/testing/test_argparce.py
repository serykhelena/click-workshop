import subprocess


def test_adder(capsys):  # noqa: ARG001
    args = ["python", "example_argparce.py", "3", "5"]

    # Захватываем stderr, где находится вывод логов
    result = subprocess.run(args, capture_output=True, text=True, check=False)  # noqa: S603
    output = result.stderr  # Используем stderr для логов

    # Проверяем, есть ли в выводе ожидаемый текст
    assert "Сумма: 8" in output, f"Ожидалось 'Сумма: 8', но получили: {output}"  # noqa: S101


# Нюансы:
# Необходимо использовать фикстуру capsys, которая даёт доступ к тексту из stdout и stderr
