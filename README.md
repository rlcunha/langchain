# Projeto Chatbot com LangChain

Este projeto implementa um chatbot inteligente utilizando:
- LangChain para orquestração de agentes
- OpenAI GPT-3.5-turbo como modelo de linguagem
- Streamlit para interface web
- SQLite para banco de dados

## Funcionalidades
- Consulta a banco de dados SQL
- Cálculos matemáticos
- Buscas na web
- Histórico de conversas

## Como executar
1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o .env com suas chaves de API
```

3. Execute a aplicação:
```bash
streamlit run Class5/front.py
```

## Melhorias Implementadas
- [x] Documentação completa
- [x] Tratamento de erros detalhado
- [x] Interface gráfica aprimorada
- [x] Controle de versões com CHANGELOG

## Melhorias futuras
- [ ] Implementar persistência do histórico
- [ ] Adicionar mais testes
- [ ] Configurar CI/CD
