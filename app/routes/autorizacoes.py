"""Rotas de Autorizações Médicas"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date as date_type
from app.database import get_db
from app.models.usuario import Usuario
from app.models.autorizacao import Autorizacao
from app.schemas.autorizacao import AutorizacaoCreate, AutorizacaoResponse
from app.utils.auth import get_current_user

router = APIRouter(prefix="/autorizacoes", tags=["Autorizações"])


@router.post("", response_model=AutorizacaoResponse, status_code=status.HTTP_201_CREATED)
def criar_autorizacao(
    autorizacao: AutorizacaoCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    """Cria uma nova autorização médica"""
    
    db_autorizacao = Autorizacao(
        numero_protocolo=autorizacao.numero_protocolo,
        data_protocolo=autorizacao.data_protocolo,
        usuario_id=current_user.id,
        paciente_nome=autorizacao.paciente.nome,
        paciente_cpf=autorizacao.paciente.cpf,
        paciente_data_nascimento=autorizacao.paciente.data_nascimento,
        paciente_telefone=autorizacao.paciente.telefone,
        paciente_email=autorizacao.paciente.email,
        paciente_cidade=autorizacao.paciente.cidade,
        medico_nome=autorizacao.medico.nome,
        medico_crm=autorizacao.medico.crm,
        medico_uf_crm=autorizacao.medico.uf_crm,
        tratamento_tipo=autorizacao.tratamento.tipo,
        tratamento_local=autorizacao.tratamento.local,
        tratamento_data_inicio=autorizacao.tratamento.data_inicio,
        tratamento_data_fim=autorizacao.tratamento.data_fim,
        tratamento_frequencia=autorizacao.tratamento.frequencia,
        tratamento_endereco=autorizacao.tratamento.endereco,
        tratamento_cidade=autorizacao.tratamento.cidade,
        tratamento_uf=autorizacao.tratamento.uf,
        tratamento_cep=autorizacao.tratamento.cep,
        tratamento_justificativa=autorizacao.tratamento.justificativa,
        status="pendente"
    )
    
    db.add(db_autorizacao)
    db.commit()
    db.refresh(db_autorizacao)
    
    return db_autorizacao


@router.get("", response_model=List[AutorizacaoResponse])
def listar_autorizacoes(
    skip: int = 0,
    limit: int = 100,
    status_filter: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    """Lista todas as autorizações do usuário atual"""
    
    query = db.query(Autorizacao).filter(Autorizacao.usuario_id == current_user.id)
    
    if status_filter:
        query = query.filter(Autorizacao.status == status_filter)
    
    autorizacoes = query.offset(skip).limit(limit).all()
    return autorizacoes


@router.get("/{autorizacao_id}", response_model=AutorizacaoResponse)
def obter_autorizacao(
    autorizacao_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    """Obtém uma autorização específica"""
    
    autorizacao = db.query(Autorizacao).filter(
        Autorizacao.id == autorizacao_id,
        Autorizacao.usuario_id == current_user.id
    ).first()
    
    if not autorizacao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Autorização não encontrada"
        )
    
    return autorizacao
