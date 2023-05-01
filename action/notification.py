import gi
gi.require_version("Notify", "0.7")
from gi.repository import Notify

class Notification:
    def __init__(self) -> None:
        Notify.init("Wear Glasses")

    def display(self, name: str):
        notification = Notify.Notification.new ("Wear Glasses",
                               f"Put on your glasses, {name}!",
                               "dialog-information")
        notification.set_timeout(0)
        notification.show()
