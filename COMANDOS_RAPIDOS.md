# 🚀 Comandos Rápidos para Rodar e Testar

## ✅ Dependências Já Instaladas!

As dependências foram instaladas no ambiente virtual. Agora é só executar!

## 🚀 Como Rodar o Servidor

### Opção 1: Usando o Script (Mais Fácil)

```bash
cd /home/fernando/Documentos/projetoTFD/backend
./rodar_servidor.sh
```

### Opção 2: Manual

```bash
cd /home/fernando/Documentos/projetoTFD/backend
source venv/bin/activate
python3 main.py
```

### Opção 3: Com Uvicorn Direto

```bash
cd /home/fernando/Documentos/projetoTFD/backend
source venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

## 🌐 Acessar a API

Após iniciar o servidor, acesse:

- **Documentação Swagger (Recomendado)**: http://localhost:8001/docs
- **Health Check**: http://localhost:8001/health
- **API Root**: http://localhost:8001

## 🧪 Testar Rápido

### 1. Health Check (no navegador)
```
http://localhost:8001/health
```
Deve retornar: `{"status": "ok"}`

### 2. Documentação Interativa
```
http://localhost:8001/docs
```
Teste todos os endpoints diretamente no navegador!

### 3. Teste via cURL (no terminal)

#### Health Check
```bash
curl http://localhost:8001/health
```

#### Cadastrar Usuário
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

#### Login
```bash
curl -X POST "http://localhost:8001/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=teste@teste.com&password=senha123"
```

## 🛑 Parar o Servidor

Pressione `Ctrl + C` no terminal onde o servidor está rodando.

## ✅ Status Atual

- ✅ Ambiente virtual criado
- ✅ Dependências instaladas
- ✅ Arquivo `.env` configurado
- ✅ Pronto para rodar!

## 🎯 Próximos Passos

1. Execute: `./rodar_servidor.sh`
2. Acesse: http://localhost:8001/docs
3. Teste os endpoints na interface Swagger!
