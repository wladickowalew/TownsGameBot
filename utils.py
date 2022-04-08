from aiogram.utils.helper import Helper, HelperMode, ListItem


class TestStates(Helper):
    mode = HelperMode.snake_case

    WAITING_NAME = ListItem()
    WAITING_AGE = ListItem()
