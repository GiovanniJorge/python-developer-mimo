# Python Developer - Mimo
Exercícios e projetos relacionados ao curso "Python Developer" da Mimo — coleção de aplicações práticas desenvolvidas ao longo do aprendizado. Ideal para estudantes que querem acompanhar e praticar os conceitos ensinados no curso.

## Conteúdo principal
- Projetos focados em resolver problemas práticos usando Python.
- Implementação de concepts como APIs, requisições HTTP, manipulação de dados e interação com o usuário.
- Exemplos que utilizam bibliotecas populares como `requests` para consumir APIs externas.

## Badges
- Linguagem: ![Python](https://img.shields.io/badge/Python-100%25-blue)
- Licença: MIT (ver arquivo LICENSE)

## Sumário
- [Visão geral](#visão-geral)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Como executar](#como-executar)
- [Pré-requisitos](#pré-requisitos)
- [Boas práticas / recomendações](#boas-práticas--recomendações)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Autor / Contato](#autor--contato)

## Visão geral
Este repositório organiza pequenos projetos em Python que exemplificam conceitos de programação prática e resolução de problemas do mundo real. Cada arquivo fonte normalmente implementa uma aplicação específica, consumindo APIs, manipulando dados ou interagindo com o usuário.

## Estrutura do repositório
Top-level:
- `.gitattributes` — configurações de atributos do Git
- `LICENSE` — licença MIT do projeto
- `README.md` — este arquivo
- `desktop.ini` — configuração de ícones (Windows)
- `projetos-finais/` — projetos finais do curso
  - `chatgpt-clone.py` — clone funcional de chatbot usando API OpenAI
  - `star-wars-api.py` — consumo de API Star Wars para listar entidades

Como se encaixa:
- Cada arquivo `.py` é um programa independente (projeto). A forma usual de usar o repositório é executar o arquivo correspondente ao projeto que deseja testar.
- Os projetos utilizam requisições HTTP para consumir APIs externas, demonstrando comunicação com serviços web.

## Como executar

### Instalação de dependências
Antes de executar qualquer projeto, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

Se não existir um arquivo `requirements.txt`, instale as bibliotecas necessárias:

```bash
pip install requests
```

### Executar um projeto específico
Para executar o clone do ChatGPT:
```bash
python projetos-finais/chatgpt-clone.py
```

Para executar o consumo da API Star Wars:
```bash
python projetos-finais/star-wars-api.py
```

### Variáveis de ambiente
Alguns projetos (como o `chatgpt-clone.py`) requerem variáveis de ambiente. Configure-as conforme necessário:

**Para Windows (PowerShell):**
```powershell
$env:MIMO_OPENAI_API_KEY="sua-chave-aqui"
```

**Para macOS/Linux (bash):**
```bash
export MIMO_OPENAI_API_KEY="sua-chave-aqui"
```

## Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- Conexão com a internet (para consumo de APIs)

## Boas práticas / recomendações
- Use ambientes virtuais para isolar dependências:
  ```bash
  python -m venv venv
  source venv/bin/activate  # macOS/Linux
  venv\Scripts\activate     # Windows
  ```
- Documente cada projeto no topo do arquivo (comentário explicando entrada esperada, saída e propósito).
- Use type hints quando possível para melhorar a legibilidade do código.
- Prefira nomes de variáveis descritivos e em inglês para compatibilidade internacional.
- Trate exceções apropriadamente, especialmente em requisições HTTP.
- Mantenha o código limpo seguindo PEP 8 (guia de estilo Python).

## Contribuindo
Contribuições são bem-vindas (ex.: correções, melhorias, novos projetos, documentação). Fluxo sugerido:
1. Fork do repositório.
2. Criar branch com nome descritivo: `feature/novo-projeto` ou `fix/bug-descricao`.
3. Fazer commits atômicos com mensagens claras.
4. Abrir Pull Request descrevendo as mudanças e, se aplicável, o objetivo do novo projeto.
5. Se possível, inclua instruções de execução e exemplos de uso.

Sugestões adicionais:
- Adicione um pequeno README ou comentários dentro de cada pasta explicando o objetivo dos projetos.
- Considere adicionar um arquivo `requirements.txt` com todas as dependências do projeto.
- Implemente testes unitários usando `unittest` ou `pytest`.

## Testes e automação (opcional)
- Poderia ser adicionado um workflow (GitHub Actions) que valida o código com `pylint` ou `flake8`.
- Para verificação automática de estilo, adicionar `black` ou `autopep8` na pipeline de CI/CD.

## Licença
Este repositório utiliza a licença MIT — consulte o arquivo `LICENSE` na raiz.

## Autor / Contato
Autor: Giovanni Jorge  
Repositório: https://github.com/GiovanniJorge/python-developer-mimo
