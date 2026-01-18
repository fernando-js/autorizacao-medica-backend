"""Schemas de Usuário"""
from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional


class UsuarioBase(BaseModel):
    """Schema base de usuário"""
    nome: str
    email: EmailStr
    nome_municipio: str
    cnpj: str
    uf: str
    cidade: str


class UsuarioCreate(UsuarioBase):
    """Schema para criar usuário"""
    cpf: Optional[str] = None
    telefone: Optional[str] = None
    data_nascimento: Optional[date] = None
    senha: str


class UsuarioLogin(BaseModel):
    """Schema para login"""
    email: EmailStr
    senha: str


class UsuarioResponse(UsuarioBase):
    """Schema de resposta do usuário"""
    id: int
    plano: str
    ativo: bool
    criado_em: datetime
    
    class Config:
        from_attributes = True
