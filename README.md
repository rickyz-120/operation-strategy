# Wise Routes - Sistema de Planejamento Logístico

## Descrição
Wise Routes é uma aplicação web desenvolvida em Python/Flask para planejamento e otimização de rotas logísticas. O sistema oferece uma interface neumórfica moderna e funcionalidades completas para gestão de frotas, motoristas, custos e análise de rotas.

## Funcionalidades

### 🎯 Dashboard Principal
- Métricas em tempo real de operações
- Preços de combustível atualizados
- Indicadores de performance
- Resumo de operações diárias

### 🗺️ Mapa Interativo
- Visualização de rotas otimizadas
- Cálculo de melhor trajeto
- Integração com APIs de mapas
- Análise de tráfego e condições

### 👥 Gestão de Motoristas
- Perfil individual de cada motorista
- Histórico de consumo e performance
- Sistema de bonificações e penalidades
- Educação e conscientização

### 🚛 Controle de Veículos
- Cadastro completo da frota
- Consumo médio por veículo
- Custos de manutenção
- Status operacional

### 💰 Análise de Custos
- Custo operacional detalhado
- Análise de viabilidade de veículos elétricos
- Otimização de gastos
- Relatórios financeiros

### 🌤️ Monitoramento Climático
- Condições meteorológicas das rotas
- Alertas de segurança
- Planejamento baseado no clima
- Recomendações operacionais

## Instalação

1. Clone o repositório
2. Instale as dependências:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`
3. Execute a aplicação:
   \`\`\`bash
   python app.py
   \`\`\`
4. Acesse http://localhost:5000

## Estrutura do Projeto

\`\`\`
wise-routes/
├── app.py                 # Aplicação principal Flask
├── data/
│   └── synthetic_data.py  # Dados sintéticos (facilmente substituíveis)
├── static/
│   ├── css/
│   │   └── style.css     # Estilos neumórficos
│   └── js/
│       └── main.js       # JavaScript principal
├── templates/
│   ├── base.html         # Template base
│   └── dashboard.html    # Dashboard principal
└── requirements.txt      # Dependências Python
\`\`\`

## Dados Sintéticos

O sistema utiliza dados sintéticos que podem ser facilmente substituídos por dados reais:
- Modifique `data/synthetic_data.py` para integrar com suas fontes de dados
- Suporte para importação de arquivos Excel/CSV
- Estrutura preparada para APIs externas

## Design Neumórfico

A interface utiliza design neumórfico com:
- Fundo cinza claro (#e0e0e0)
- Sombras suaves duplas (clara e escura)
- Elementos que parecem esculpidos no material
- Fonte preta em todo o projeto
- Efeitos de pressão em botões e interações

## Próximos Passos

1. Integração com APIs reais de mapas
2. Conexão com banco de dados
3. Sistema de autenticação
4. Relatórios avançados
5. Aplicativo móvel
