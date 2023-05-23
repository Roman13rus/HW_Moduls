# from application.salary import calculate_salary ###вариант импорта №2
from application import salary
# from application.db.people import get_employees  ##вариант импорта №2
from application.db import people
from datetime import datetime
import logging
my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.INFO)
my_handler = logging.FileHandler(f"logs\{__name__}.log", mode='w')
my_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

my_handler.setFormatter(my_formatter)
my_logger.addHandler(my_handler)

if __name__ == "__main__":
    start = datetime.now()
    print(f'The module is running {start}')
    salary.calculate_salary()
    people.get_employees()
    finish = datetime.now()
    print(f'The module has finished working {finish}')
    print(f'The module was working {finish - start}')
    my_logger.info(f"Successful result: The module has finished working.")



