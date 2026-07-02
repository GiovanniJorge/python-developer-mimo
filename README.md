# Python Developer - Mimo

Exercícios e projetos relacionados ao curso "Python Developer" da Mimo — coleção de aplicações práticas desenvolvidas ao longo do aprendizado. Ideal para estudantes que querem acompanhar e praticar os conceitos ensinados no curso.

## Conteúdo principal
- Projetos focados em resolver problemas práticos usando Python.
- Implementação de conceitos como APIs, requisições HTTP, manipulação de dados e interação com o usuário.
- Exemplos que utilizam bibliotecas populares como `requests` para consumir APIs externas.

## Badges
![Licença](https://img.shields.io/github/license/GiovanniJorge/python-developer-mimo?style=flat-square)

## Sumário
- [Visão geral](#visão-geral)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Destaques do repositório](#destaques-do-repositório)
- [Como executar](#como-executar)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Autor / Contato](#autor--contato)

## Visão geral
Este repositório organiza pequenos projetos em Python que exemplificam conceitos de programação prática e resolução de problemas do mundo real. Cada arquivo fonte implementa uma aplicação específica, consumindo APIs, manipulando dados ou interagindo com o usuário por meio de scripts diretos.

## Estrutura do repositório
Top-level:
```text
├── .gitattributes
├── LICENSE                  # Licença MIT do projeto
├── README.md                # Este arquivo
└── projetos-finais/         # Projetos finais e integrados do curso
    ├── chatgpt-clone.py     # Clone funcional de chatbot usando API OpenAI
    ├── star-wars-api.py     # Consumo de API Star Wars para listar entidades
    └── ...                  # Outros subprojetos desenvolvidos nas seções práticas
```

### Como se encaixa:
- O repositório abriga uma variedade de scripts e projetos independentes criados ao longo do curso.
- Cada arquivo `.py` é um programa executável autônomo. A dinâmica comum de uso consiste em instalar os pacotes globais ou via ambiente virtual e disparar o arquivo desejado.

## Destaques do repositório

### ChatGPT Clone
* **Descrição:** Script interativo que simula uma interface de chatbot via terminal, integrando chamadas e consumo da API oficial da OpenAI.
* **Tecnologias:** Python, OpenAI API, Requests.

### Star Wars API
* **Descrição:** Aplicação focada no consumo, tratamento e exibição de dados estruturados obtidos de forma assíncrona ou direta da API pública do ecossistema Star Wars.
* **Tecnologias:** Python, SWAPI (Star Wars API), Requests.

## Como executar

### Pré-requisitos
- **Python** (v3.7 ou superior)
- **pip** como gerenciador de pacotes Python

### Passos para execução

1. **Clone o repositório:**
```bash
git clone [https://github.com/GiovanniJorge/python-developer-mimo.git](https://github.com/GiovanniJorge/python-developer-mimo.git)
cd python-developer-mimo
```

2. **Instale as dependências externas necessárias:**
```bash
pip install requests
```

3. **Configure as variáveis de ambiente obrigatórias (Exemplo para o ChatGPT Clone):**

* **No Windows (PowerShell):**
```powershell
$env:MIMO_OPENAI_API_KEY="sua-chave-aqui"
```

* **No Linux/macOS (Terminal):**
```bash
export MIMO_OPENAI_API_KEY="sua-chave-aqui"
```

4. **Execute o script desejado via terminal:**
```bash
python projetos-finais/chatgpt-clone.py
```

## Contribuindo
Contribuições são bem-vistas! Se deseja adicionar um novo projeto prático ou sugerir melhorias no tratamento de exceções HTTP, siga os passos abaixo:

1. Faça um **Fork** do repositório.
2. Crie uma branch com nome descritivo: `feature/novo-projeto` ou `fix/bug-descricao`.
3. Faça commits atômicos com mensagens claras e objetivas.
4. Abra um **Pull Request** detalhando as alterações implementadas.

## Licença
Este repositório utiliza a licença MIT — consulte o arquivo [LICENSE](LICENSE) na raiz.

## Autor / Contato
- **Autor:** Giovanni Jorge  
- **Repositório:** [https://github.com/GiovanniJorge/python-developer-mimo](https://github.com/GiovanniJorge/python-developer-mimo)
