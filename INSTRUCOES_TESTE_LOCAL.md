# 🧪 Como Testar o Backend Localmente

## ⚠️ Pré-requisito

Se ainda não tiver `python3-venv` instalado:

```bash
sudo apt install python3.12-venv
```

## 🚀 Opção 1: Usar o Script Automático

```bash
cd /home/fernando/Documentos/projetoTFD/backend
./testar_local.sh
```

## 🚀 Opção 2: Manual

### 1. Criar Ambiente Virtual

```bash
cd /home/fernando/Documentos/projetoTFD/backend
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Criar Arquivo .env

Crie um arquivo `.env` na raiz do backend:

```bash
cat > .env << 'EOF'
SECRET_KEY=WV5HKz4LUsvOHFw-Rff1sPEVCA2ML5tr37Qbf03cnb0
ENVIRONMENT=development
DATABASE_URL=sqlite:///./autorizacao_medica.db
CORS_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
EOF
```

### 4. Executar o Servidor

```bash
# Com ambiente virtual ativado
python3 main.py
```

Ou:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

## 🌐 Acessar a API

- **Documentação Swagger**: http://localhost:8001/docs
- **API Health Check**: http://localhost:8001/health
- **API Root**: http://localhost:8001

## 🧪 Testar na Documentação Swagger

1. Acesse: http://localhost:8001/docs
2. Teste `/health` primeiro
3. Teste `/api/auth/cadastro` para criar um usuário
4. Teste `/api/auth/login` para fazer login
5. Use o token retornado no botão "Authorize" (cadeado)
6. Teste os outros endpoints

## 📝 Exemplo de Teste via cURL

### Health Check
```bash
curl http://localhost:8001/health
```

### Cadastrar Usuário
```bash
curl -X POST "http://localhost:8001/api/auth/cadastro" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Teste",
    "email": "teste@teste.com",
    "senha": "senha123",
    "nome_municipio": "Município Teste",
    "cnpj": "12.345.678/0001-90",
    "uf": "SP",
    "cidade": "São Paulo"
  }'
```

### Login
```bash
curl -X POST "http://localhost:8001/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=teste@teste.com&password=senha123"
```

## ✅ Checklist

- [ ] `python3-venv` instalado
- [ ] Ambiente virtual criado
- [ ] Dependências instaladas
- [ ] Arquivo `.env` criado
- [ ] Servidor rodando
- [ ] Documentação acessível em /docs
