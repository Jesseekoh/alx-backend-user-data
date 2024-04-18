#!/usr/bin/env python3
"""auth module"""
from typing import TypeVar

from flask import request


class Auth:
    """Auth class definition"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
