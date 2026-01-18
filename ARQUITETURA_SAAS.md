# Arquitetura SaaS - Sistema de Autorização Médica

## 🎯 Visão Geral

Este documento descreve a arquitetura proposta para transformar o sistema em uma plataforma SaaS (Software as a Service) multi-tenant, permitindo vender para múltiplas prefeituras.

## 📋 Conceito Multi-Tenant

Cada prefeitura (tenant) terá:
- Seu próprio painel administrativo isolado
- Seus próprios dados isolados
- Seu próprio sistema de numeração de protocolos
- Limitações baseadas no plano contratado

## 🏗️ Estrutura do Backend (Python)

### Recomendação: **Implementar depois**

**Por quê?**
- É mais fácil desenvolver primeiro para um único tenant
- Depois adicionar multi-tenancy quando já tiver a base funcionando
- Evita complexidade desnecessária no início

### Quando implementar SaaS?
- Após ter o sistema básico funcionando (CRUD completo)
- Após validar o produto com um cliente piloto
- Quando estiver pronto para escalar comercialmente

## 🔧 Arquitetura Proposta (Para Implementação Futura)

### 1. Modelo de Dados Multi-Tenant

```python
# Exemplo de estrutura (usando SQLAlchemy)

class Tenant(Prefeitura):
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cnpj = Column(String, unique=True)
    plano = Column(String)  # 'gratuito', 'basico', 'premium'
    ativo = Column(Boolean, default=True)
    criado_em = Column(DateTime)
    limite_protocolos = Column(Integer)  # Baseado no plano

class Usuario:
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey('tenant.id'))
    nome = Column(String)
    email = Column(String)
    role = Column(String)  # 'admin', 'operador', 'viewer'
    
class Autorizacao:
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey('tenant.id'))  # 🔑 CHAVE
    protocolo = Column(String)  # Gerado por tenant
    # ... demais campos
```

### 2. Middleware de Tenant (Middleware/Filtro)

Toda requisição deve identificar o tenant:

```python
# Flask/FastAPI Middleware
@app.middleware("http")
async def tenant_middleware(request: Request, call_next):
    # Identificar tenant via:
    # 1. Subdomínio (municipio.seusistema.com)
    # 2. Header HTTP (X-Tenant-ID)
    # 3. Token JWT (contém tenant_id)
    
    tenant_id = identificar_tenant(request)
    request.state.tenant_id = tenant_id
    
    response = await call_next(request)
    return response

# Em todos os queries, filtrar por tenant_id
def get_autorizacoes():
    tenant_id = request.state.tenant_id
    return Autorizacao.query.filter_by(tenant_id=tenant_id).all()
```

### 3. Geração de Protocolo por Tenant

Cada município tem seu próprio sistema:

```python
def gerar_protocolo(tenant_id: int) -> str:
    tenant = Tenant.query.get(tenant_id)
    ultimo_numero = get_ultimo_protocolo(tenant_id)
    
    # Formato customizado por tenant
    if tenant.formato_protocolo == "ANO/SEQUENCIAL":
        return f"{datetime.now().year}/{ultimo_numero:06d}"
    elif tenant.formato_protocolo == "SEQUENCIAL":
        return f"{ultimo_numero:06d}"
    # ...
```

### 4. Planos e Limites

```python
PLANOS = {
    'gratuito': {
        'limite_protocolos_mes': 50,
        'limite_usuarios': 3,
        'recursos': ['basico']
    },
    'basico': {
        'limite_protocolos_mes': 500,
        'limite_usuarios': 10,
        'recursos': ['basico', 'relatorios']
    },
    'premium': {
        'limite_protocolos_mes': -1,  # Ilimitado
        'limite_usuarios': -1,
        'recursos': ['basico', 'relatorios', 'api', 'suporte_prioritario']
    }
}

def verificar_limite(tenant_id: int, tipo: str):
    tenant = Tenant.query.get(tenant_id)
    plano = PLANOS[tenant.plano]
    
    if tipo == 'protocolo':
        usado = contar_protocolos_mes(tenant_id)
        limite = plano['limite_protocolos_mes']
        if limite > 0 and usado >= limite:
            raise LimiteExcedidoException()
```

### 5. Painéis Administrativos

#### Painel da Prefeitura (Tenant)
- `/admin/` - Área administrativa da prefeitura
- Configurações do município
- Gestão de usuários locais
- Visualização de estatísticas
- Configuração de formato de protocolo

#### Painel Super Admin (SaaS Owner)
- `/superadmin/` - Área do dono do SaaS
- Listar todas as prefeituras
- Gerenciar planos e assinaturas
- Estatísticas globais
- Billing e cobrança
- Suporte

## 🔐 Autenticação e Autorização

### JWT com Tenant ID

```python
def criar_token(usuario_id: int, tenant_id: int):
    payload = {
        'user_id': usuario_id,
        'tenant_id': tenant_id,  # ✅ Incluir no token
        'role': 'admin',
        'exp': datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, SECRET_KEY)

# Verificar em cada requisição
def get_tenant_id_from_token():
    token = request.headers.get('Authorization')
    payload = jwt.decode(token, SECRET_KEY)
    return payload['tenant_id']
```

## 📊 Banco de Dados

### Opção 1: Banco Único com Tenant ID (Recomendado)
- **Prós**: Simples, fácil de manter
- **Contras**: Todos os dados no mesmo banco
- **Ideal para**: Começar com SaaS

### Opção 2: Banco Separado por Tenant
- **Prós**: Isolamento total
- **Contras**: Complexo, difícil manutenção
- **Ideal para**: Empresas grandes com necessidades específicas

**Recomendação**: Comece com Opção 1, migre para Opção 2 se necessário.

## 🚀 Roadmap de Implementação

### Fase 1: Sistema Básico (Atual)
- ✅ Frontend simples
- ⏳ Backend básico (um tenant)
- ⏳ CRUD de autorizações e tratamentos

### Fase 2: Multi-Tenancy (Futuro)
1. Adicionar modelo `Tenant`
2. Adicionar `tenant_id` em todas as tabelas
3. Implementar middleware de tenant
4. Criar painel administrativo da prefeitura
5. Implementar sistema de planos
6. Criar painel super admin
7. Implementar billing

### Fase 3: Recursos Avançados
- API para integrações
- Relatórios avançados
- Notificações por email/SMS
- Upload de documentos
- Assinatura digital

## 💡 Estratégia Recomendada

1. **Desenvolver primeiro como sistema único**
   - Foco em funcionalidades
   - Validar com um cliente piloto

2. **Depois adicionar multi-tenancy**
   - Refatorar código para suportar tenant_id
   - Adicionar middleware
   - Criar painéis admin

3. **Então preparar para SaaS**
   - Sistema de planos
   - Billing
   - Onboarding de novos clientes

## 🛠️ Tecnologias Sugeridas para Backend

- **Framework**: FastAPI ou Flask
- **ORM**: SQLAlchemy
- **Autenticação**: JWT (python-jose)
- **Multi-tenancy**: django-tenants (se usar Django) ou implementação custom
- **Billing**: Stripe ou similar
- **Banco**: PostgreSQL (suporta multi-tenant bem)

## 📝 Observações Importantes

1. **Isolamento de Dados**: Crítico para privacidade e conformidade
2. **Performance**: Índices em `tenant_id` são essenciais
3. **Segurança**: Nunca confiar no cliente - sempre validar tenant_id no backend
4. **Billing**: Automatizar cobrança e suspensão de contas
5. **Onboarding**: Fluxo simples para novas prefeituras se cadastrarem

## ❓ Perguntas Frequentes

**P: Devo implementar multi-tenancy agora ou depois?**
R: **DEPOIS**. Desenvolva o sistema básico primeiro, valide com clientes, depois adicione multi-tenancy.

**P: Como identificar qual tenant está usando o sistema?**
R: Via subdomínio, header HTTP, ou token JWT. Subdomínio é mais user-friendly.

**P: E se uma prefeitura quiser instalar em seu próprio servidor?**
R: Considere uma versão "on-premise" no futuro, mas foque primeiro em SaaS.

**P: Como cobrar das prefeituras?**
R: Integre com Stripe/PagSeguro para assinaturas recorrentes baseadas em planos.

---

**Conclusão**: Planeje a arquitetura SaaS agora, mas **implemente depois**. Desenvolva primeiro o sistema básico para validar o produto.
