import logging
import pytest


class LogGen:
    @staticmethod
    def loggen():
        # getLogger() method takes the test case name as input
        logger = logging.getLogger(__name__)

        # FileHandler() method takes location and path of log file
        fileHandler = logging.FileHandler('.\\Logs\\logfile.log')

        # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        # addHandler() method takes fileHandler object as parameter
        logger.addHandler(fileHandler)

        # setting the logger level
        logger.setLevel(logging.INFO)

        return logger


################################################## Pytest HTML Report #################################################

# It is hook for adding environment info to HTML report
def pytest_configure(config):
    config.metadata['Project name'] = "nop Commerce"
    config.metadata['Module Name'] = "Customers"
    config.metadata['Tester'] = "Pavan"


# It is hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)
