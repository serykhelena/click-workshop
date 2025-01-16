import click


@click.group()
def cli():
    """
    Основной CLI с подгруппами, демонстрирующими разные варианты click.version_option.
    """  # noqa: RUF002


# Первая подгруппа: версия задаётся вручную через аргумент version
@cli.group()
@click.version_option(version="1.0.0", message="Версия первой группы: %(version)s")
def group1():
    """
    Первая подгруппа.
    """


@group1.command()
def hello():
    click.echo("Привет из первой группы!")


# Вторая подгруппа: версия берётся из package_name
@cli.group()
@click.version_option(package_name="click-workshop")
def group2():
    """
    Вторая подгруппа.
    """


@group2.command()
def status():
    click.echo("Статус из второй группы.")


# Третья подгруппа: кастомное сообщение версии
@cli.group()
@click.version_option(version="2.3.4", message="Кастомное сообщение: Версия %(version)s!")
def group3():
    """
    Третья подгруппа.
    """


@group3.command()
def info():
    click.echo("Информация из третьей группы.")


if __name__ == "__main__":
    cli()

# Примеры вызова из командной строки:
# python version_option.py group1 --version
# python version_option.py group2 --version
# python version_option.py group3 --version

# Нюансы:
# Возможно задавать версию вручную через 'version', брать из 'package_name'
# или использовать кастомное сообщение через 'message'.
