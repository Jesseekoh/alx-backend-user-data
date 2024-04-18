#!/usr/bin/env python3
"""auth module"""
from typing import List, TypeVar

from flask import request


class Auth:
    """Auth class definition"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        # if not request and "Authorization" not in request.header:
        return None
        # return request.header["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        return None
