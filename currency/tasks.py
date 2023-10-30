from celery import shared_task
from celery.utils.log import get_task_logger

from .utils import fetch_currencies_data


logger = get_task_logger(__name__)


@shared_task
def update_rates():
    fetch_currencies_data()
