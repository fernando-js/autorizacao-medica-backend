# Como Testar o Backend Localmente

Guia rápido para testar o backend em desenvolvimento local.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🚀 Passo a Passo

### 1. Instalar Dependências

```bash
cd /home/fernando/Documentos/projetoTFD/backend
pip3 install -r requirements.txt
```

Ou use um ambiente virtual (recomendado):

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt
```

### 2. Criar Arquivo .env

Crie um arquivo `.env` na raiz do backend com:

```env
# Segurança
SECRET_KEY=WV5HKz4LUsvOHFw-Rff1sPEVCA2ML5tr37Qbf03cnb0

# Ambiente
ENVIRONMENT=development

# Banco de Dados (SQLite para desenvolvimento)
DATABASE_URL=sqlite:///./autorizacao_medica.db

# CORS
CORS_ORIGINS=http://localhost:8000,http://127.0.0.1:8000

# JWT
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Executar o Servidor

```bash
cd /home/fernando/Documentos/projetoTFD/backend
python3 main.py
```

Ou usando uvicorn diretamente:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

### 4. Acessar a API

- **API**: http://localhost:8001
- **Documentação Swagger**: http://localhost:8001/docs
- **Documentação ReDoc**: http://localhost:8001/redoc
- **Health Check**: http://localhost:8001/health

## 🧪 Testar Endpoints

### 1. Health Check

```bash
curl http://localhost:8001/health
```

Resposta esperada:
```json
{"status": "ok"}
```

### 2. Cadastrar Usuário

```bash
curl -X POST "http://localhost:8001/api/auth/cadastro" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Prefeitura Teste",
    "email": "teste@prefeitura.com",
    "senha": "senha123",
    "nome_municipio": "Município Teste",
    "cnpj": "12.345.678/0001-90",
    "uf": "SP",
    "cidade": "São Paulo"
  }'
```

### 3. Fazer Login

```bash
curl -X POST "http://localhost:8001/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=teste@prefeitura.com&password=senha123"
```

Resposta esperada:
```json
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

### 4. Criar Autorização (com token)

```bash
# Primeiro faça login e copie o token
TOKEN="seu-token-aqui"

curl -X POST "http://localhost:8001/api/autorizacoes" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "numero_protocolo": "2024/001",
    "paciente": {
      "nome": "João Silva",
      "cpf": "123.456.789-00",
      "data_nascimento": "1990-01-01",
      "telefone": "(11) 99999-9999",
      "cidade": "São Paulo"
    },
    "medico": {
      "nome": "Dr. Maria Santos",
      "crm": "123456",
      "uf_crm": "SP"
    },
    "tratamento": {
      "tipo": "quimioterapia",
      "local": "Hospital Central",
      "data_inicio": "2024-01-15",
      "frequencia": "semanal",
      "endereco": "Rua Teste, 123",
      "cidade": "São Paulo",
      "uf": "SP",
      "justificativa": "Tratamento necessário"
    }
  }'
```

## 📚 Usar a Documentação Interativa

A forma mais fácil de testar é usar a documentação Swagger:

1. Acesse: http://localhost:8001/docs
2. Clique em "Authorize" (cadeado no topo)
3. Faça login primeiro em `/api/auth/login`
4. Copie o token retornado
5. Cole no campo "Authorize" no formato: `Bearer seu-token`
6. Agora pode testar todos os endpoints diretamente na interface

## 🗄️ Banco de Dados Local

O banco SQLite será criado automaticamente em:
```
/home/fernando/Documentos/projetoTFD/backend/autorizacao_medica.db
```

Para visualizar os dados:
```bash
sqlite3 autorizacao_medica.db
.tables
SELECT * FROM usuarios;
```

## 🐛 Troubleshooting

**Erro: ModuleNotFoundError**
- Instale as dependências: `pip3 install -r requirements.txt`

**Erro: SECRET_KEY required**
- Crie o arquivo `.env` com as variáveis

**Erro: Port already in use**
- Use outra porta: `uvicorn main:app --port 8002`

**Erro de CORS**
- Verifique se `CORS_ORIGINS` inclui a URL do frontend

## ✅ Checklist

- [ ] Dependências instaladas
- [ ] Arquivo `.env` criado
- [ ] Servidor rodando na porta 8001
- [ ] Health check funcionando
- [ ] Documentação acessível em /docs
- [ ] Teste de cadastro funcionando
- [ ] Teste de login funcionando
