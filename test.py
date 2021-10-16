import unittest
import coloredlogs
import logging
import sys
from L7_user.tests.user_tests import UserTests
from L7_event.tests.event_tests import EventTests

coloredlogs.install()

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

if __name__ == "__main__":
    unittest.main()