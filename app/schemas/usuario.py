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


class UsuarioUpdate(BaseModel):
    """Schema para atualizar dados do usuário"""
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    cpf: Optional[str] = None
    telefone: Optional[str] = None
    data_nascimento: Optional[date] = None
    nome_municipio: Optional[str] = None
    cnpj: Optional[str] = None
    uf: Optional[str] = None
    cidade: Optional[str] = None


class UsuarioAlterarSenha(BaseModel):
    """Schema para alterar senha"""
    senha_atual: str
    nova_senha: str
    confirmar_senha: str


class UsuarioResponse(UsuarioBase):
    """Schema de resposta do usuário"""
    id: int
    cpf: Optional[str] = None
    telefone: Optional[str] = None
    data_nascimento: Optional[date] = None
    plano: str
    ativo: bool
    criado_em: datetime
    
    class Config:
        from_attributes = True
