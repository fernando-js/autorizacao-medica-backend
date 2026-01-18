"""Schemas para autenticação e tokens"""
from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    """Schema de resposta do token"""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Schema de dados do token"""
    email: Optional[str] = None
