"""
This is the module where we have defined
User service method.
"""

import logging

logger = logging.getLogger(__name__)


def get_user_service():
    """
    Retrieve user list from the data.

    Args:
        item_id (int): The ID of the item.

    Returns:
        dict: A dictionary containing the user emails and theri
        respective roles.

    Raises:
        HTTPException: If the item_id is invalid.
        ValueError: If the `id` provided is not a positive integer.
    """
    try:
        logger.info("Start of the service")
        return {
            "user_list": [{"email": "xyz", "role": "A"}, {"email": "kja", "role": "B"}]
        }
    except KeyError as e:
        logger.error(e)
