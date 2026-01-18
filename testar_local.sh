#!/bin/bash
# Script para testar o backend localmente

echo "🚀 Configurando ambiente para teste local..."

# Verificar se .env existe
if [ ! -f .env ]; then
    echo "📝 Criando arquivo .env..."
    cat > .env << EOF
# Configurações para desenvolvimento local
SECRET_KEY=WV5HKz4LUsvOHFw-Rff1sPEVCA2ML5tr37Qbf03cnb0
ENVIRONMENT=development
DATABASE_URL=sqlite:///./autorizacao_medica.db
CORS_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
EOF
    echo "✅ Arquivo .env criado!"
else
    echo "✅ Arquivo .env já existe"
fi

# Verificar se venv existe
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv || {
        echo "❌ Erro: python3-venv não instalado"
        echo "Execute: sudo apt install python3.12-venv"
        exit 1
    }
    echo "✅ Ambiente virtual criado!"
fi

# Ativar venv e instalar dependências
echo "📦 Instalando dependências..."
source venv/bin/activate
pip install -r requirements.txt

echo ""
echo "✅ Configuração concluída!"
echo ""
echo "Para iniciar o servidor, execute:"
echo "  source venv/bin/activate"
echo "  python3 main.py"
echo ""
echo "Ou:"
echo "  source venv/bin/activate"
echo "  uvicorn main:app --reload --host 0.0.0.0 --port 8001"
echo ""
echo "Acesse: http://localhost:8001/docs"
