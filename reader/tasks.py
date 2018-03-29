from celery.task import task
from celery.utils.log import get_task_logger

from reader import parser

logger = get_task_logger(__name__)


@task(bind=True)
def update_feed(self):
    logger.info('Rss feed update started.')
    parser.parse()