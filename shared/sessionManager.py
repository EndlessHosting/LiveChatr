from bot import bot
from web import web

class SessionManager:
    """SessionManager for Web <-> Discord"""


    def __init__(self):
        self.sessions = {}

    def create_session(self, session_id):
        self.sessions[session_id] = bot.create_session()

    def end_session(self, session_id):
        self.sessions.pop(session_id)
        # insert ending logic here


    def send_web_message(self, channel_id, message):
        session_id = self.sessions[list(self.sessions.keys()).index(channel_id)]
        return
        # Insert web sending here
        # web.send_client_message(session_id, message)

    def send_discord_message(self, session_id, message):
        return
        # Insert discord sending here
        # bot.send_client_message(sessions[session_id], message)

