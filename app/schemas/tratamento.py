"""Schemas de Tratamento Fora de Domicílio"""
from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from app.schemas.autorizacao import PacienteBase, MedicoBase, TratamentoBase


class TratamentoCreate(BaseModel):
    """Schema para criar tratamento fora de domicílio"""
    numero_protocolo: str
    data_protocolo: date
    paciente: PacienteBase
    medico: MedicoBase
    tratamento: TratamentoBase


class TratamentoResponse(BaseModel):
    """Schema de resposta de tratamento"""
    id: int
    numero_protocolo: str
    data_protocolo: date
    paciente: PacienteBase
    medico: MedicoBase
    tratamento: TratamentoBase
    status: str
    criado_em: datetime
    
    class Config:
        from_attributes = True
