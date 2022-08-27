import json
import logging

logger = logging.getLogger("my_logger")


def get_keys() -> list():
    """
    Reads the api_keys.json file and returns the keys

    Args: None
    Raises: OSError if the file is not found
    Returns: [dict] of keys
    """
    try:
        logger.debug("Reading keys")
        with open("configs/api_keys.json", "r") as readerFile:
            fileDat = readerFile.read()
        readerFile.close()
        return json.loads(fileDat)
    except Exception as e:
        logger.critical("Error at reading keys: %s", e)
        raise OSError


def update_keys(keys):
    """
    Stores the keys in the api_keys.json file

    Args: keys - dict of keys
    Raises: OSError
    Returns: None
    """

    try:
        logger.debug("Updating keys")
        with open("configs/api_keys.json", "w") as writerFile:
            writerFile.write(json.dumps(keys))
        writerFile.close()
    except Exception as e:
        logger.error("Error at updating keys: %s", e)
        raise OSError


def process_keys(keys) -> tuple[dict, int]:
    """
    Processes the keys and returns the key
    which is still valid

    Args: keys - dict of keys
    Raises: None
    Returns:
    """

    logger.debug("Processing keys")

    for index, item in enumerate(keys):
        if keys[index]["status"] == "OK":
            return item, index
