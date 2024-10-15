from os import environ
from typing import Final


class TgKeys:
    TOKEN: Final = environ.get('TOKEN', 'define me!')
    CHAT_ID: Final = environ.get('CHAT_ID', 'define me!')
    ID_FOR_ANSWER: Final = environ.get('ID_FOR_ANSWER', 'define me!')



