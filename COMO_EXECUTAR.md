# Como Executar o Projeto Wise Routes

## Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação e Execução

### 1. Instalar Dependências
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 2. Executar a Aplicação
\`\`\`bash
python app.py
\`\`\`

### 3. Acessar no Navegador
Abra seu navegador e acesse: `http://localhost:5000`

## Páginas Disponíveis
- **Dashboard**: `http://localhost:5000/` - Métricas principais
- **Mapa Interativo**: `http://localhost:5000/map` - Planejamento de rotas
- **Gestão de Motoristas**: `http://localhost:5000/drivers` - Performance e educação
- **Controle de Veículos**: `http://localhost:5000/vehicles` - Frota e manutenção
- **Análise de Custos**: `http://localhost:5000/costs` - Otimização financeira
- **Monitoramento Climático**: `http://localhost:5000/weather` - Condições meteorológicas
- **Relatórios**: `http://localhost:5000/reports` - Analytics avançados

## Solução de Problemas

### Erro de Importação do Flask
Se você receber erro "Import 'flask' could not be resolved":
1. Certifique-se de que está no ambiente virtual correto
2. Execute: `pip install --upgrade flask`
3. Reinicie seu editor/IDE

### Porta já em uso
Se a porta 5000 estiver ocupada, o Flask automaticamente tentará a próxima porta disponível.

## Estrutura do Projeto
\`\`\`
wise-routes/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── data/
│   └── synthetic_data.py  # Dados sintéticos (facilmente substituíveis)
├── templates/             # Templates HTML
├── static/
│   ├── css/
│   └── js/
└── README.md
\`\`\`

## Substituição de Dados
Os dados sintéticos estão em `data/synthetic_data.py` e podem ser facilmente substituídos por:
- Conexão com banco de dados
- Importação de arquivos Excel/CSV
- APIs externas
