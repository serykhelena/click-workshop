import click


@click.command()
def main():
    """
    Пример использования click.prompt.
    """
    # Запрашиваем имя
    name = click.prompt("Введите ваше имя", type=str)
    click.echo(f"Привет, {name}!")

    # Запрашиваем возраст (числовой ввод)
    age = click.prompt("Введите ваш возраст", type=int)
    click.echo(f"Ваш возраст: {age} лет.")

    # Скрытый ввод (например, пароля)
    password_user = click.prompt("Введите ваш пароль", hide_input=True)  # noqa: F841
    click.echo("Ваш пароль успешно принят (он не будет отображён).")

    # Запрос с подтверждением  # noqa: RUF003
    secret_code = click.prompt(
        "Введите секретный код",
        hide_input=True,
        confirmation_prompt=True,
    )
    click.echo(f"Ваш секретный код: {secret_code} (успешно подтверждён).")

    # Значение по умолчанию
    favorite_color = click.prompt("Ваш любимый цвет", default="синий")
    click.echo(f"Ваш любимый цвет: {favorite_color}")

    favorite_color = click.prompt("Ваш любимый цвет (не вводить значение)", default="синий")
    click.echo(f"Ваш любимый цвет: {favorite_color}")


if __name__ == "__main__":
    main()

# Примеры вызова из командной строки:
# python prompt_click.py

# Нюансы:
# По умолчанию click.prompt ожидает строку, но можно указать тип c
#   помощью аргумента type (например, int, float, bool)
# Если пользователь вводит значение неправильного типа, будет повторяться запрос
# Используя параметр confirmation_prompt=True, можно запросить подтверждение введённого значения
# Можно задать значение по умолчанию через параметр default
# Можно использовать параметр hide_input=True, чтобы текст не отображался на экране
# При неправильном вводе будет выброшено исключение click.Abort
