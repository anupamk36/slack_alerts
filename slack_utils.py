# Module docstring
"""
This module contains the SlackUtils class which is used to send alerts to Slack.
owner: @anupamk36
"""

import time
from typing import Dict, Any
import logging
from enum import Enum
import requests


log = logging.getLogger(__name__)


class Status(Enum):
    """
    Enum for status of the alert.
    """

    ERROR = "#FF5733"  # This is a shade of red
    SUCCESS = "#36a64f"  # This is a shade of green
    WARNING = "#FFBF00"  # This is a shade of yellow


class SlackUtils:
    """
    Class for sending alerts to Slack.
    """

    def __init__(self, slack_webhook_url: str, channel: str):
        """
        Initialize SlackUtils.

        Args:
            slack_webhook_url (Optional[str]): Slack webhook URL, defaults to None.
            channel (Optional[str]): Slack channel, defaults to None.
        """
        self.slack_webhook_url: str = slack_webhook_url
        self.channel: str = channel

    def _post_to_slack(self, payload: Dict[str, Any]):
        """
        Post the payload to Slack.
        Args:
            payload (Dict[str, Any]): The payload to send.
        """
        try:
            response = requests.post(self.slack_webhook_url, json=payload, timeout=10)
            response.raise_for_status()
            log.debug("Slack alert sent successfully.")
        except requests.RequestException as exc:
            log.exception("Failed to send Slack alert: %s", exc)

    def _send_message(self, message: str, status: Status):
        """
        Send a message to Slack with the given status.

        Args:
            message (str): The message to send.
            status (Status): The status of the message.
        """
        payload = {
            "color": status.value,
            "channel": self.channel,
            "text": message,
            "ts": int(time.time()),
        }
        self._post_to_slack(payload)

    def send_info_message(self, message: str):
        """
        Send an informational message to Slack.

        Args:
            message (str): The informational message.
        """
        self._send_message(message, Status.SUCCESS)

    def send_warning_message(self, message: str):
        """
        Send a warning message to Slack.

        Args:
            message (str): The warning message.
        """
        self._send_message(message, Status.WARNING)

    def send_error_message(self, message: str):
        """
        Send an error message to Slack.

        Args:
            message (str): The error message.
        """
        self._send_message(f"*Error:* {message}", Status.ERROR)
