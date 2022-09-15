import os
import qrcode

class Qr:
    @staticmethod
    def make(text: str) -> None:
        qrcode.make(text).save("static/images/hello.png")