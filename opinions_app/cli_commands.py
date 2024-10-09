import csv

import click

from . import app, db
from .models import Opinion
from settings import FILE_NAME_CSV

TEXT_COUNTER = 'Загружено мнений: {}'
TEXT_NO_FILE_FOUND = 'Файл "{}" не обнаружен!'


@app.cli.command('load_opinions')
@click.argument('file_name', required=False)
def load_opinions_command(file_name):
    """Функция загрузки мнений в базу данных.
    После команды принимает аргумент имени файла с расширением csv, например:
    flask load_opinions file.csv
    """
    if not file_name:
        file_name = FILE_NAME_CSV
    try:
        with open(file_name, encoding='utf-8') as f:
            # Создаём итерируемый объект, который отображает каждую строку
            # в качестве словаря с ключами из шапки файла:
            reader = csv.DictReader(f)
            counter = 0
            for row in reader:
                opinion = Opinion(**row)
                db.session.add(opinion)
                db.session.commit()
                counter += 1
        click.echo(TEXT_COUNTER.format(counter))
    except FileNotFoundError:
        click.echo(TEXT_NO_FILE_FOUND.format(file_name))
