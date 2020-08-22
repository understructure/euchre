import json
import logging


class Logger(logging.Logger):
    def __init__(self, name):
        self.name = name

    def info(self, msg, *args, **kwargs):
        if "msg_type" in kwargs:
            msg_type = kwargs["msg_type"]
            message_type_msg = self._get_message_by_message_type(msg_type)
        else:
            msg_type = ""
            message_type_msg = msg
        message = {"level": "INFO", "type": msg_type, "msg": message_type_msg}
        return message

    def _get_message_by_message_type(self, msg_type):
        if msg_type == "hand":
            rez = {}
        elif msg_type == "trick":
            rez = {}
        elif msg_type == "game":
            rez = {}
        else:
            raise NotImplementedError("Message type %s is not implemented", msg_type)
