"""Rotas de Tratamentos Fora de Domicílio"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.usuario import Usuario
from app.models.tratamento_fora_domicilio import TratamentoForaDomicilio
from app.schemas.tratamento import TratamentoCreate, TratamentoResponse
from app.utils.auth import get_current_user

router = APIRouter(prefix="/tratamentos", tags=["Tratamentos"])


@router.post("", response_model=TratamentoResponse, status_code=status.HTTP_201_CREATED)
def criar_tratamento(
    tratamento: TratamentoCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    """Cria um novo tratamento fora de domicílio"""
    
    db_tratamento = TratamentoForaDomicilio(
        numero_protocolo=tratamento.numero_protocolo,
        data_protocolo=tratamento.data_protocolo,
        usuario_id=current_user.id,
        paciente_nome=tratamento.paciente.nome,
        paciente_cpf=tratamento.paciente.cpf,
        paciente_data_nascimento=tratamento.paciente.data_nascimento,
        paciente_telefone=tratamento.paciente.telefone,
        paciente_email=tratamento.paciente.email,
        paciente_cidade=tratamento.paciente.cidade,
        medico_nome=tratamento.medico.nome,
        medico_crm=tratamento.medico.crm,
        medico_uf_crm=tratamento.medico.uf_crm,
        tratamento_tipo=tratamento.tratamento.tipo,
        tratamento_local=tratamento.tratamento.local,
        tratamento_data_inicio=tratamento.tratamento.data_inicio,
        tratamento_data_fim=tratamento.tratamento.data_fim,
        tratamento_frequencia=tratamento.tratamento.frequencia,
        tratamento_endereco=tratamento.tratamento.endereco,
        tratamento_cidade=tratamento.tratamento.cidade,
        tratamento_uf=tratamento.tratamento.uf,
        tratamento_cep=tratamento.tratamento.cep,
        tratamento_justificativa=tratamento.tratamento.justificativa,
        status="pendente"
    )
    
    db.add(db_tratamento)
    db.commit()
    db.refresh(db_tratamento)
    
    return db_tratamento


@router.get("", response_model=List[TratamentoResponse])
def listar_tratamentos(
    skip: int = 0,
    limit: int = 100,
    status_filter: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    """Lista todos os tratamentos do usuário atual"""
    
    query = db.query(TratamentoForaDomicilio).filter(
        TratamentoForaDomicilio.usuario_id == current_user.id
    )
    
    if status_filter:
        query = query.filter(TratamentoForaDomicilio.status == status_filter)
    
    tratamentos = query.offset(skip).limit(limit).all()
    return tratamentos


@router.get("/{tratamento_id}", response_model=TratamentoResponse)
def obter_tratamento(
    tratamento_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    """Obtém um tratamento específico"""
    
    tratamento = db.query(TratamentoForaDomicilio).filter(
        TratamentoForaDomicilio.id == tratamento_id,
        TratamentoForaDomicilio.usuario_id == current_user.id
    ).first()
    
    if not tratamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tratamento não encontrado"
        )
    
    return tratamento
