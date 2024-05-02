from slack_utils import SlackUtils

# Initialize SlackUtils with your Slack webhook URL and channel
slack = SlackUtils(slack_webhook_url='your-slack-webhook-url', channel='your-channel')

try:
    # Your code here...
    slack.send_info_message("This is an informational message.")
except Warning as w:
    # If a warning occurs, send a warning message to Slack
    warning_message = str(w)
    slack.send_warning_message(warning_message)
except Exception as e:
    # If an exception occurs, send an error message to Slack
    error_message = str(e)
    slack.send_error_message(error_message)