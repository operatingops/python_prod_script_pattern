"""
This script is ready for production.
"""

import argparse
import logging
import time


class SimulatorFilter(logging.Filter):
    def __init__(self, simulate):
        self.simulate = simulate
        super(SimulatorFilter, self).__init__()

    def filter(self, record):
        record.prefix = 'SIMULATE ' if self.simulate else ''
        return True


def setup_logging(log_level, simulate):

    # Setup a root logger with a format that matches what we plan to use.
    # This means LogRecords from other libraries will still be emitted and will
    # look similar to ours.
    root_format_string = '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
    logging.basicConfig(format=root_format_string, level=log_level)

    # Setup our logger with a filter that adds a prefix whenever simulate=True.
    # Don't propagate because our format string expects a prefix not set on
    # handlers of loggers created by other libraries.
    format_string = '%(asctime)s | %(levelname)s | %(name)s | %(prefix)s%(message)s' # noqa
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt=format_string)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    logger = logging.getLogger(__name__)
    logger.propagate = False
    has_simulator_filter = [i for i in logger.filters
                            if isinstance(i, SimulatorFilter)]
    if not has_simulator_filter:
        logger.addFilter(SimulatorFilter(simulate))


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
            logger.info('Action complete.')
        except Exception:
            # Our pretend work won't trigger this, but a real script would do
            # something more interesting that might break.
            logger.info('Failure.')
    else:
        logger.debug('Simulate option set. Not acting.')
    return done


def run(offset, log_level='INFO', simulate=False):
    setup_logging(log_level, simulate)
    logger = logging.getLogger(__name__)
    if offset_is_actionable(offset):
        logger.info('Acting.')
        act_on_offset(offset, simulate)
    else:
        logger.info('Nothing to do.')


def entry_point():  # pragma: no cover
    args = get_arguments()
    run(args.offset, args.log_level, args.simulate)
