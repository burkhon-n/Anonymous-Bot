import json

ADMIN_ID = "admin_id"
URL = "URL"
TOKEN = "TOKEN"
CHANNEL = "@channel_username"

messages = {
    'start': "<b>Welcome to Anonymous Bot!\n\n👋 Hi there!</b> We’re here to help you share your thoughts anonymously, safely, and with ease.\n\n🚀 <b>How it works:</b>\n\n  •  Send us any message you want.\n  •  We’ll forward it anonymously to the community.\n  •  For messages with links, we’ll review them before sharing!\n\nFeel free to drop your message anytime—your privacy is our priority! 💬",
    'help': "🤔 <b>How to Use the Bot:</b>\n\n<b>1.</b> Send a message to the bot.\n<b>2.</b> If your message contains a link, it will be reviewed by an admin before being shared.\n<b>4.</b> Messages without links are shared directly and anonymously in the channel.\n4. If your message contains inappropriate content, the admin can block you.\n\n🚫 <b>Blocked Users:</b>\n\n  •  If you’re blocked, all your messages will be sent for review before being forwarded.",
    'url_review': "🔍 <b>Review Required</b> 🔍\n\nYour message contains a URL. It will be reviewed by an admin before being shared.",
}

def get_blocked_users():
    with open("blocked_users.json", "r") as file:
        return json.load(file)
