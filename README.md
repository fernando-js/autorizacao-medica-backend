# Sistema de Autorização Médica - Backend

Backend do sistema de autorização médica e tratamento fora de domicílio, desenvolvido com Python e FastAPI.

## 📋 Status

✅ **Backend Implementado** - API REST funcional

## 🎯 Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal
- **FastAPI**: Framework web moderno e rápido
- **SQLAlchemy**: ORM para banco de dados
- **SQLite**: Banco de dados (desenvolvimento)
- **JWT**: Autenticação por tokens
- **Bcrypt**: Hash de senhas

## 📁 Estrutura do Projeto

```
backend/
├── app/
│   ├── __init__.py
│   ├── config.py              # Configurações da aplicação
│   ├── database.py            # Configuração do banco de dados
│   ├── models/                # Modelos de dados (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   ├── autorizacao.py
│   │   └── tratamento_fora_domicilio.py
│   ├── schemas/               # Schemas Pydantic (validação)
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   ├── autorizacao.py
│   │   ├── tratamento.py
│   │   └── token.py
│   ├── routes/                # Rotas da API
│   │   ├── __init__.py
│   │   ├── auth.py            # Autenticação (login, cadastro)
│   │   ├── autorizacoes.py    # CRUD de autorizações
│   │   └── tratamentos.py     # CRUD de tratamentos
│   └── utils/                 # Utilitários
│       ├── __init__.py
│       └── auth.py            # Funções de autenticação JWT
├── main.py                    # Ponto de entrada da aplicação
├── requirements.txt           # Dependências Python
└── README.md
```

## 🚀 Como Executar

### 1. Instalar Dependências

```bash
cd backend
pip install -r requirements.txt
```

Ou use um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do backend (copie de `.env.example`):

```bash
cp .env.example .env
```

Edite o arquivo `.env`:

```env
SECRET_KEY=seu-secret-key-aqui-mude-em-producao
DATABASE_URL=sqlite:///./autorizacao_medica.db
ENVIRONMENT=development
```

### 3. Executar o Servidor

```bash
python main.py
```

Ou usando uvicorn diretamente:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

### 4. Acessar a API

- **API**: http://localhost:8001
- **Documentação Swagger**: http://localhost:8001/docs
- **Documentação ReDoc**: http://localhost:8001/redoc

## 📚 Endpoints da API

### Autenticação (`/api/auth`)

- `POST /api/auth/cadastro` - Cadastrar novo usuário (prefeitura)
- `POST /api/auth/login` - Fazer login (retorna token JWT)
- `GET /api/auth/me` - Obter informações do usuário atual

### Autorizações (`/api/autorizacoes`)

- `POST /api/autorizacoes` - Criar nova autorização médica
- `GET /api/autorizacoes` - Listar autorizações do usuário
- `GET /api/autorizacoes/{id}` - Obter autorização específica

### Tratamentos (`/api/tratamentos`)

- `POST /api/tratamentos` - Criar tratamento fora de domicílio
- `GET /api/tratamentos` - Listar tratamentos do usuário
- `GET /api/tratamentos/{id}` - Obter tratamento específico

## 🔐 Autenticação

A API usa JWT (JSON Web Tokens) para autenticação.

1. **Cadastrar**: `POST /api/auth/cadastro`
2. **Login**: `POST /api/auth/login` (retorna token)
3. **Usar token**: Adicione no header: `Authorization: Bearer {token}`

### Exemplo de Uso:

```bash
# Login
curl -X POST "http://localhost:8001/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=email@example.com&password=senha123"

# Usar token
curl -X GET "http://localhost:8001/api/autorizacoes" \
  -H "Authorization: Bearer {seu-token}"
```

## 🗄️ Banco de Dados

O banco de dados SQLite é criado automaticamente na primeira execução.

**Localização**: `autorizacao_medica.db` (na raiz do backend)

### Para PostgreSQL (Produção):

1. Instale `psycopg2-binary`:
```bash
pip install psycopg2-binary
```

2. Configure no `.env`:
```env
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## 📦 Deploy no Easypanel

1. Crie um novo projeto no Easypanel
2. Escolha "Python" como tipo de aplicação
3. Conecte o repositório GitHub `autorizacao-medica-backend`
4. Configure:
   - **Command**: `uvicorn main:app --host 0.0.0.0 --port 8001`
   - **Port**: `8001`
   - **Environment Variables**: Configure `SECRET_KEY` e `DATABASE_URL`
5. Configure banco de dados PostgreSQL se necessário
6. Deploy automático

## 🔄 Próximos Passos

- [ ] Integrar frontend com API REST
- [ ] Adicionar validações de CPF/CNPJ
- [ ] Implementar recuperação de senha por e-mail
- [ ] Adicionar geração de relatórios em PDF
- [ ] Implementar upload de documentos
- [ ] Adicionar sistema de notificações

## 📝 Observações

- O backend está pronto para receber requisições do frontend
- Substitua `localStorage` no frontend por chamadas à API
- Configure CORS no `.env` para permitir requisições do frontend
- Em produção, use PostgreSQL e configure `SECRET_KEY` forte
