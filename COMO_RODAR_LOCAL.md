# 🚀 Como Rodar e Testar o Backend Localmente

## ✅ Passo 1: Instalar Pré-requisito (se necessário)

```bash
sudo apt install python3.12-venv
```

## ✅ Passo 2: Criar Ambiente Virtual

```bash
cd /home/fernando/Documentos/projetoTFD/backend
python3 -m venv venv
```

## ✅ Passo 3: Ativar Ambiente Virtual

```bash
source venv/bin/activate
```

Você verá `(venv)` no início do prompt.

## ✅ Passo 4: Instalar Dependências

```bash
pip install -r requirements.txt
```

## ✅ Passo 5: Verificar Arquivo .env

O arquivo `.env` já foi criado com as configurações. Verifique:

```bash
cat .env
```

Deve conter:
```
SECRET_KEY=WV5HKz4LUsvOHFw-Rff1sPEVCA2ML5tr37Qbf03cnb0
ENVIRONMENT=development
DATABASE_URL=sqlite:///./autorizacao_medica.db
CORS_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## ✅ Passo 6: Executar o Servidor

Com o ambiente virtual ativado:

```bash
python3 main.py
```

Ou:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

Você verá algo como:
```
INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## 🌐 Passo 7: Acessar a API

Abra no navegador:

- **Documentação Swagger (Recomendado)**: http://localhost:8001/docs
- **Health Check**: http://localhost:8001/health
- **API Root**: http://localhost:8001

## 🧪 Passo 8: Testar na Documentação Swagger

1. Acesse: http://localhost:8001/docs
2. Você verá todos os endpoints disponíveis
3. Teste na seguinte ordem:

### a) Health Check
- Clique em `GET /health`
- Clique em "Try it out"
- Clique em "Execute"
- Deve retornar: `{"status": "ok"}`

### b) Cadastrar Usuário
- Clique em `POST /api/auth/cadastro`
- Clique em "Try it out"
- Preencha o JSON de exemplo:
```json
{
  "nome": "Prefeitura Teste",
  "email": "teste@prefeitura.com",
  "senha": "senha123",
  "nome_municipio": "Município Teste",
  "cnpj": "12.345.678/0001-90",
  "uf": "SP",
  "cidade": "São Paulo"
}
```
- Clique em "Execute"
- Deve retornar os dados do usuário criado

### c) Fazer Login
- Clique em `POST /api/auth/login`
- Clique em "Try it out"
- Preencha:
  - `username`: `teste@prefeitura.com`
  - `password`: `senha123`
- Clique em "Execute"
- **Copie o `access_token` retornado!**

### d) Usar Token (Authorize)
- Clique no botão **"Authorize"** (cadeado no topo)
- Cole o token no formato: `Bearer seu-token-aqui`
- Clique em "Authorize"
- Agora você pode testar endpoints protegidos

### e) Criar Autorização
- Clique em `POST /api/autorizacoes`
- Clique em "Try it out"
- Preencha o JSON de exemplo
- Clique em "Execute"
- Deve criar a autorização com sucesso

## 📝 Teste Rápido via Terminal (cURL)

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

## 🗄️ Verificar Banco de Dados

O banco SQLite será criado automaticamente em:
```
/home/fernando/Documentos/projetoTFD/backend/autorizacao_medica.db
```

Para visualizar:
```bash
sqlite3 autorizacao_medica.db
.tables
SELECT * FROM usuarios;
.quit
```

## 🛑 Parar o Servidor

Pressione `Ctrl + C` no terminal onde o servidor está rodando.

## ✅ Checklist

- [ ] Ambiente virtual criado
- [ ] Dependências instaladas
- [ ] Arquivo `.env` configurado
- [ ] Servidor rodando na porta 8001
- [ ] Documentação acessível em /docs
- [ ] Health check funcionando
- [ ] Cadastro de usuário funcionando
- [ ] Login funcionando
- [ ] Token sendo gerado

## 🐛 Problemas Comuns

**Erro: ModuleNotFoundError**
- Ative o venv: `source venv/bin/activate`
- Instale dependências: `pip install -r requirements.txt`

**Erro: Port already in use**
- Use outra porta: `uvicorn main:app --port 8002`

**Erro: SECRET_KEY required**
- Verifique se o arquivo `.env` existe e tem SECRET_KEY

**Erro ao criar venv**
- Instale: `sudo apt install python3.12-venv`
