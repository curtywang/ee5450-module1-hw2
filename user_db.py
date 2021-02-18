from typing import Tuple, Dict


class UserDB(object):
    def __init__(self):
        self._accounts: Dict[str, str] = {}
        self._salts: Dict[str, str] = {}

    def create_user(self, username: str) -> Tuple[str, str]:
        """
        Creates a user and returns a token (password) for the user.
        Only the one-way hash is stored in self._accounts.
        Salts are stored in self._salts.
        Yum.... hash browns!

        :raises: ValueError if the username already exists
        :param username: desired username
        :return: (username, password_token)
        """
        pass

    def is_valid(self, username: str, password) -> bool:
        """
        Check whether the given username and password match a user
        present in the UserDB.  The hash of the input password is
        compared to the stored hash.

        :param username:
        :param password:
        :return: True if the credentials are valid, False if not.
        """
