import logging
logger = logging.getLogger(__name__)


def get_user_service():
    """
    Function to fetch user list
    """
    try:
        logger.info("Start of the service")
        return {"user_list": [{"email": "xyz", "role": "A"},{"email": "kja","role":"B"}]}
    except Exception as e:
        logger.error(e)

