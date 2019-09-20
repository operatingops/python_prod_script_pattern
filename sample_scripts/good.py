"""
This script is ready for production.
"""

import argparse
import logging
import time

from pythonjsonlogger import jsonlogger


def setup_logging(log_level, simulate):
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    logHandler = logging.StreamHandler()
    if simulate:
        formatter = jsonlogger.JsonFormatter(
            fmt='%(asctime)s %(levelname)s %(name)s %(message)s',
            prefix='SIMULATE'
        )
    else:
        formatter = jsonlogger.JsonFormatter(
            fmt='%(asctime)s %(levelname)s %(name)s %(message)s'
        )
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)


def get_arguments():  # pragma: no cover
    parser = argparse.ArgumentParser(
        description='Sample script.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--simulate', action='store_true',
                        help="Print what would be done but don't do it.")
    parser.add_argument('--log-level', type=str, default='INFO',
                        help='Python log level. INFO, DEBUG, etc.')
    parser.add_argument('offset', help='Integer for sample action.', type=int)
    return parser.parse_args()


def offset_is_actionable(offset):
    result = offset + 5
    if result < 10:
        return True
    else:
        return False


def act_on_offset(offset, simulate=False):
    logger = logging.getLogger(__name__)
    done = False
    if not simulate:
        try:
            time.sleep(5)
            done = True
        except Exception:
            # Catching all exceptions is an anti-pattern. This is a generic
            # example of how you could use log levels when errors happen.
            # Our pretend work won't trigger this, but a real script would do
            # something more interesting that might break.
            logger.error('Failure.')
    return done


def run(offset, log_level='INFO', simulate=False):
    setup_logging(log_level, simulate)
    logger = logging.getLogger(__name__)
    if offset_is_actionable(offset):
        logger.info('Acting.')
        act_on_offset(offset, simulate)
        logger.info('Action complete.')
    else:
        logger.info('Nothing to do.')


def entry_point():  # pragma: no cover
    args = get_arguments()
    run(args.offset, args.log_level, args.simulate)
