# Configuração do Backend no Easypanel

Guia completo para deploy do backend no Easypanel com banco de dados PostgreSQL.

## 🗄️ Banco de Dados

### Banco de Dados Configurado: **PostgreSQL**

O backend está configurado para usar **PostgreSQL** em produção (SQLite apenas para desenvolvimento).

### String de Conexão (DATABASE_URL)

Formato:
```
postgresql://usuario:senha@host:porta/nome_do_banco
```

Exemplo:
```
postgresql://admin:senha123@postgres.seudominio.com:5432/autorizacao_medica
```

## 📋 Passo a Passo no Easypanel

### 1. Criar Banco de Dados PostgreSQL

1. No Easypanel, vá em **"Database"** ou **"Add Resource"**
2. Escolha **"PostgreSQL"**
3. Configure:
   - **Name**: `autorizacao-medica-db` (ou o nome que preferir)
   - **Database**: `autorizacao_medica` (nome do banco)
   - **User**: `admin` (ou o usuário que preferir)
   - **Password**: (será gerado automaticamente - ANOTE!)
4. Clique em **"Create"**

### 2. Anotar Informações de Conexão

Após criar o banco, anote:
- **Host**: `postgres.seudominio.com` (ou similar)
- **Port**: `5432` (padrão PostgreSQL)
- **Database**: `autorizacao_medica`
- **User**: `admin` (ou o que você configurou)
- **Password**: (senha gerada)

### 3. Construir String DATABASE_URL

Use as informações acima para montar a string:

```
postgresql://admin:senha123@postgres.seudominio.com:5432/autorizacao_medica
```

Onde:
- `admin` = usuário
- `senha123` = senha
- `postgres.seudominio.com` = host
- `5432` = porta (padrão)
- `autorizacao_medica` = nome do banco

### 4. Criar Aplicação Python

1. No Easypanel, vá em **"Projects"** ou **"New App"**
2. Escolha **"Python"** ou **"Source"**
3. Configure:
   - **Name**: `autorizacao-medica-backend`
   - **Source**: Conecte o repositório GitHub `autorizacao-medica-backend`
   - **Branch**: `main`

### 5. Configurar Build

**Build Command** (se necessário):
```bash
pip install -r requirements.txt
```

### 6. Configurar Start Command

**Start Command**:
```bash
uvicorn main:app --host 0.0.0.0 --port 8001
```

### 7. Configurar Port

**Port**: `8001`

### 8. Configurar Variáveis de Ambiente

Na seção **"Environment Variables"** ou **"Env"**, adicione:

```env
# Segurança (MUDE EM PRODUÇÃO!)
SECRET_KEY=sua-chave-secreta-forte-aqui-gerar-aleatoriamente

# Banco de Dados (use a string de conexão que você montou)
DATABASE_URL=postgresql://admin:senha123@postgres.seudominio.com:5432/autorizacao_medica

# Ambiente
ENVIRONMENT=production

# CORS (URL do seu frontend no Easypanel)
CORS_ORIGINS=https://seu-frontend.com,https://www.seu-frontend.com

# JWT
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 9. Linkar Banco de Dados à Aplicação

No Easypanel, você pode:
- **Linkar o banco** diretamente na interface (mais fácil)
- Ou usar a string `DATABASE_URL` completa

### 10. Atualizar requirements.txt (Se necessário)

Certifique-se de que o `requirements.txt` inclui:

```txt
# Para PostgreSQL
psycopg2-binary==2.9.9
```

## 🔐 Gerar SECRET_KEY Segura

Para gerar uma SECRET_KEY segura, execute:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Ou use online: https://generate-secret.vercel.app/32

## 📝 Variáveis de Ambiente Completas

```env
# Obrigatórias
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=postgresql://usuario:senha@host:porta/banco

# Opcionais (têm valores padrão)
ENVIRONMENT=production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
CORS_ORIGINS=https://seu-frontend.com
```

## 🔗 Conexão com Banco de Dados

### Formato da String de Conexão

```
postgresql://[usuario]:[senha]@[host]:[porta]/[nome_do_banco]
```

### Componentes:

- **usuario**: Usuário do banco (ex: `admin`)
- **senha**: Senha do banco
- **host**: Endereço do banco (ex: `postgres.easypanel.com`)
- **porta**: Porta PostgreSQL (geralmente `5432`)
- **nome_do_banco**: Nome do banco (ex: `autorizacao_medica`)

## ✅ Checklist de Deploy

- [ ] Banco PostgreSQL criado no Easypanel
- [ ] String DATABASE_URL montada e testada
- [ ] Repositório GitHub conectado
- [ ] Variável SECRET_KEY configurada (chave forte)
- [ ] Variável DATABASE_URL configurada
- [ ] CORS_ORIGINS configurado (URL do frontend)
- [ ] Port configurada: `8001`
- [ ] Start command configurado: `uvicorn main:app --host 0.0.0.0 --port 8001`
- [ ] Banco linkado à aplicação (ou via DATABASE_URL)
- [ ] Deploy realizado e funcionando

## 🧪 Testar Após Deploy

1. Acesse: `https://seu-backend.easypanel.com/docs`
2. Teste o endpoint `/health`: deve retornar `{"status": "ok"}`
3. Teste cadastro: `POST /api/auth/cadastro`
4. Teste login: `POST /api/auth/login`

## 📚 Documentação da API

Após deploy, a documentação interativa estará em:
- **Swagger UI**: `https://seu-backend.easypanel.com/docs`
- **ReDoc**: `https://seu-backend.easypanel.com/redoc`

## ⚠️ Observações Importantes

1. **SECRET_KEY**: Use uma chave forte e única em produção
2. **DATABASE_URL**: Mantenha segura, não exponha em logs
3. **CORS**: Configure apenas domínios permitidos
4. **Backup**: Configure backup automático do PostgreSQL no Easypanel
5. **SSL**: O Easypanel geralmente configura SSL automaticamente

## 🆘 Troubleshooting

**Erro de conexão com banco:**
- Verifique se a string DATABASE_URL está correta
- Verifique se o banco está linkado à aplicação
- Verifique se `psycopg2-binary` está no requirements.txt

**Erro de CORS:**
- Adicione a URL do frontend em `CORS_ORIGINS`
- Verifique se o formato está correto (separado por vírgula)

**Erro de import:**
- Verifique se todas as dependências estão no `requirements.txt`
- Verifique se o build foi bem-sucedido
