"""Schemas de Autorização Médica"""
from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class PacienteBase(BaseModel):
    """Schema base de paciente"""
    nome: str
    cpf: str
    data_nascimento: date
    telefone: str
    email: Optional[str] = None
    cidade: str


class MedicoBase(BaseModel):
    """Schema base de médico"""
    nome: str
    crm: str
    uf_crm: str


class TratamentoBase(BaseModel):
    """Schema base de tratamento"""
    tipo: str
    local: str
    data_inicio: date
    data_fim: Optional[date] = None
    frequencia: str
    endereco: str
    cidade: str
    uf: str
    cep: Optional[str] = None
    justificativa: str


class AutorizacaoCreate(BaseModel):
    """Schema para criar autorização"""
    numero_protocolo: Optional[str] = None
    data_protocolo: Optional[date] = None
    paciente: PacienteBase
    medico: MedicoBase
    tratamento: TratamentoBase


class AutorizacaoResponse(BaseModel):
    """Schema de resposta de autorização"""
    id: int
    numero_protocolo: Optional[str]
    data_protocolo: Optional[date]
    paciente: PacienteBase
    medico: MedicoBase
    tratamento: TratamentoBase
    status: str
    criado_em: datetime
    
    class Config:
        from_attributes = True
