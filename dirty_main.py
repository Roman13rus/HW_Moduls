from application.salary import *
from application.db.people import *
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
    calculate_salary()
    get_employees()
    finish = datetime.now()
    print(f'The module has finished working {finish}')
    print(f'The module was working {finish - start}')
    my_logger.info(f"Successful result: The module has finished working.")