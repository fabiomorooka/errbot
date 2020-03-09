import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = r'C:\Users\a784292\OneDrive - Atos\Desktop\errbot\first_test\data'
BOT_EXTRA_PLUGIN_DIR = r'C:\Users\a784292\OneDrive - Atos\Desktop\errbot\first_test\plugins'

BOT_LOG_FILE = r'C:\Users\a784292\OneDrive - Atos\Desktop\errbot\first_test\errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@fabio.morooka')  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!

BOT_IDENTITY = {
    'token': 'xoxb-975943619185-986060285141-FVNVe9bN9zkbx4xpMwqC4t6m',
}

BOT_ALT_PREFIXES = ('@errbot')

CHATROOM_PRESENCE = ()