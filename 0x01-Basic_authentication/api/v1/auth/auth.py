#!/usr/bin/env python3
from typing import List, TypeVar

from flask import request


class Auth:
    """Auth class definition"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication"""
        if (not path or excluded_paths == None or len(excluded_paths) == 0):
            return True

        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        if not request and "Authorization" not in request.header:
            return None
        return request.header["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        return None
