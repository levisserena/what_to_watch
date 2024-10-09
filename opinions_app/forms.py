from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


TEXT_REQUIRED = 'Обязательное поле'
TEXT_SUBMIT = 'Добавить'
TEXT_TITLE = 'Введите название фильма'
TEXT_FIELD_TEXT = 'Напишите мнение'
TEXT_SOURCE = 'Добавьте ссылку на подробный обзор фильма'


class OpinionForm(FlaskForm):
    title = StringField(
        TEXT_TITLE,
        validators=[DataRequired(message=TEXT_REQUIRED),
                    Length(1, 128)]
    )
    text = TextAreaField(
        TEXT_FIELD_TEXT,
        validators=[DataRequired(message=TEXT_REQUIRED)]
    )
    source = URLField(
        TEXT_SOURCE,
        validators=[Length(1, 256), Optional()]
    )
    submit = SubmitField(TEXT_SUBMIT)
