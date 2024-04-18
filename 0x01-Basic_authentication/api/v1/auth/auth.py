#!/usr/bin/env python3
"""auth module"""
from typing import List, TypeVar

from flask import request


class Auth:
    """Auth class definition"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if not request and "Authorization" not in request.header:
            return None
        return request.header["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
