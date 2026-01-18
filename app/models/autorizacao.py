"""Modelo de Autorização Médica"""
from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Autorizacao(Base):
    """Modelo de Autorização Médica"""
    __tablename__ = "autorizacoes"

    id = Column(Integer, primary_key=True, index=True)
    numero_protocolo = Column(String(50), nullable=True)
    data_protocolo = Column(Date, nullable=True)
    
    # Relacionamento com usuário (prefeitura)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    
    # Dados do paciente
    paciente_nome = Column(String(200), nullable=False)
    paciente_cpf = Column(String(14), nullable=False)
    paciente_data_nascimento = Column(Date, nullable=False)
    paciente_telefone = Column(String(20), nullable=False)
    paciente_email = Column(String(100), nullable=True)
    paciente_cidade = Column(String(100), nullable=False)
    
    # Dados do médico
    medico_nome = Column(String(200), nullable=False)
    medico_crm = Column(String(20), nullable=False)
    medico_uf_crm = Column(String(2), nullable=False)
    
    # Dados do tratamento
    tratamento_tipo = Column(String(50), nullable=False)
    tratamento_local = Column(String(200), nullable=False)
    tratamento_data_inicio = Column(Date, nullable=False)
    tratamento_data_fim = Column(Date, nullable=True)
    tratamento_frequencia = Column(String(30), nullable=False)
    tratamento_endereco = Column(String(300), nullable=False)
    tratamento_cidade = Column(String(100), nullable=False)
    tratamento_uf = Column(String(2), nullable=False)
    tratamento_cep = Column(String(10), nullable=True)
    tratamento_justificativa = Column(Text, nullable=False)
    
    # Status
    status = Column(String(20), default="pendente", nullable=False)  # pendente, aprovada, rejeitada
    
    # Timestamps
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    usuario = relationship("Usuario", back_populates="autorizacoes")
