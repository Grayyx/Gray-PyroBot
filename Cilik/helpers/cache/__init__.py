from base64 import b64decode
from os import getenv

CBHDSYS = getenv(
    "CBHDSYS",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL1N5dXp1dS9HcmF5LVB5cm9Cb3Q=").decode("utf-8"),
)
