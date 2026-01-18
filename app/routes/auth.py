"""Rotas de autenticação"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse, UsuarioLogin, UsuarioUpdate, UsuarioAlterarSenha
from app.schemas.token import Token
from app.utils.auth import (
    verify_password,
    get_password_hash,
    create_access_token,
    get_current_user
)
from app.config import get_settings

router = APIRouter(prefix="/auth", tags=["Autenticação"])
settings = get_settings()


@router.post("/cadastro", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """Cadastra um novo usuário (prefeitura/município)"""
    
    # Verificar se e-mail já existe
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail já cadastrado"
        )
    
    # Verificar se CNPJ já existe
    db_cnpj = db.query(Usuario).filter(Usuario.cnpj == usuario.cnpj).first()
    if db_cnpj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CNPJ já cadastrado"
        )
    
    # Criar novo usuário
    db_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=get_password_hash(usuario.senha),
        nome_municipio=usuario.nome_municipio,
        cnpj=usuario.cnpj,
        uf=usuario.uf,
        cidade=usuario.cidade,
        cpf=usuario.cpf,
        telefone=usuario.telefone,
        data_nascimento=usuario.data_nascimento,
        plano="gratuito"
    )
    
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    
    return db_usuario


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Realiza login e retorna token de acesso"""
    
    # Buscar usuário por e-mail
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()
    
    if not usuario or not verify_password(form_data.password, usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not usuario.ativo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário inativo"
        )
    
    # Criar token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": usuario.email}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UsuarioResponse)
def obter_usuario_atual(current_user: Usuario = Depends(get_current_user)):
    """Obtém informações do usuário atual"""
    return current_user


@router.put("/me", response_model=UsuarioResponse)
def atualizar_usuario(
    usuario_update: UsuarioUpdate,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Atualiza dados do usuário atual"""
    
    # Verificar se e-mail foi alterado e se já existe
    if usuario_update.email and usuario_update.email != current_user.email:
        email_existe = db.query(Usuario).filter(
            Usuario.email == usuario_update.email,
            Usuario.id != current_user.id
        ).first()
        if email_existe:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="E-mail já cadastrado"
            )
    
    # Verificar se CNPJ foi alterado e se já existe
    if usuario_update.cnpj and usuario_update.cnpj != current_user.cnpj:
        cnpj_existe = db.query(Usuario).filter(
            Usuario.cnpj == usuario_update.cnpj,
            Usuario.id != current_user.id
        ).first()
        if cnpj_existe:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="CNPJ já cadastrado"
            )
    
    # Atualizar apenas campos que foram enviados
    update_data = usuario_update.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(current_user, field, value)
    
    db.commit()
    db.refresh(current_user)
    
    return current_user


@router.put("/me/alterar-senha", response_model=UsuarioResponse)
def alterar_senha(
    senha_data: UsuarioAlterarSenha,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Altera a senha do usuário atual"""
    
    # Verificar senha atual
    if not verify_password(senha_data.senha_atual, current_user.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Senha atual incorreta"
        )
    
    # Verificar se novas senhas coincidem
    if senha_data.nova_senha != senha_data.confirmar_senha:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="As senhas não coincidem"
        )
    
    # Verificar se a nova senha é diferente da atual
    if verify_password(senha_data.nova_senha, current_user.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A nova senha deve ser diferente da senha atual"
        )
    
    # Atualizar senha
    current_user.senha_hash = get_password_hash(senha_data.nova_senha)
    
    db.commit()
    db.refresh(current_user)
    
    return current_user
