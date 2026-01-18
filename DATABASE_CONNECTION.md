# Configuração de Conexão com Banco de Dados

## 📋 Informações do Banco de Dados

- **Nome do Banco**: `autorizacao_medica`
- **Usuário**: `admin`
- **Senha**: `Aguia@018`
- **Porta**: `5432` (padrão PostgreSQL)

## 🔗 String de Conexão (DATABASE_URL)

**✅ URL de Conexão Interna do Easypanel (PRONTA PARA USAR):**
```
postgres://admin:Aguia@018@tfd_autorizacao-medica-db:5432/autorizacao_medica?sslmode=disable
```

**📋 Informações:**
- **Protocolo**: `postgres://` (usado pelo Easypanel internamente)
- **Host**: `tfd_autorizacao-medica-db`
- **Porta**: `5432`
- **Database**: `autorizacao_medica`
- **User**: `admin`
- **Password**: `Aguia@018`
- **SSL Mode**: `disable` (conexão interna)

**⚠️ Nota:** Esta é a URL interna do Easypanel. Use esta URL exatamente como está!

## 📍 Host do Banco

**Host Interno:** `tfd_autorizacao-medica-db`

✅ **Host encontrado!** Este é o host interno do Easypanel para comunicação entre serviços.

## 🔧 Configuração no Easypanel

### Opção 1: Linkar Banco de Dados (Recomendado)

No Easypanel, quando você linka o banco de dados à aplicação:
- O HOST é configurado automaticamente
- Apenas configure o nome do banco na variável: `DB_NAME=autorizacao_medica`

### Opção 2: Usar DATABASE_URL Completa

Se não usar link, configure a variável `DATABASE_URL` completa:

```env
DATABASE_URL=postgresql://admin:Aguia%40018@postgres.seudominio.com:5432/autorizacao_medica
```

## ✅ Variáveis de Ambiente para o Backend

Adicione estas variáveis no Easypanel (seção Environment Variables):

```env
# Banco de Dados (URL INTERNA DO EASYPANEL)
DATABASE_URL=postgres://admin:Aguia@018@tfd_autorizacao-medica-db:5432/autorizacao_medica?sslmode=disable
```

**✅ URL completa do Easypanel!** Copie exatamente como está acima.

## 🔐 Exemplo Completo de Variáveis (PRONTO PARA USAR)

```env
# Segurança (MUDE EM PRODUÇÃO!)
SECRET_KEY=sua-chave-secreta-forte-aqui

# Banco de Dados (✅ URL INTERNA DO EASYPANEL)
DATABASE_URL=postgres://admin:Aguia@018@tfd_autorizacao-medica-db:5432/autorizacao_medica?sslmode=disable

# Ambiente
ENVIRONMENT=production

# CORS (adicione a URL do seu frontend)
CORS_ORIGINS=https://seu-frontend.com

# JWT (opcional, tem valores padrão)
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 📝 Status

1. ✅ Banco criado: `autorizacao_medica`
2. ✅ Usuário: `admin`
3. ✅ Senha: `Aguia@018`
4. ✅ Host encontrado: `tfd_autorizacao-medica-db`
5. ✅ DATABASE_URL montada
6. ⏳ Próximo: Configurar variável no backend no Easypanel

## ✅ Tudo Configurado!

**✅ URL de Conexão Interna Completa (do Easypanel):**
```
postgres://admin:Aguia@018@tfd_autorizacao-medica-db:5432/autorizacao_medica?sslmode=disable
```

**📝 Próximo Passo:**
1. Copie a URL acima
2. No Easypanel, vá até seu serviço backend Python
3. Vá em **"Environment Variables"** ou **"Env"**
4. Adicione: `DATABASE_URL=postgres://admin:Aguia@018@tfd_autorizacao-medica-db:5432/autorizacao_medica?sslmode=disable`
5. Salve e faça o deploy/restart do serviço

**✅ Está tudo pronto para usar!**
