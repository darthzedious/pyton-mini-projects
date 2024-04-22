from canvas import frame
from hashlib import sha256


def clean_screen():  # this function clears the screen when we go from one page to another
    frame.delete("all")


def get_password_hash(password):
    hash_objects = sha256(password.encode())
    return hash_objects.hexdigest()
