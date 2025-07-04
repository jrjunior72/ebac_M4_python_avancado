# EBAC Módulo 4 – Web Scraping com Python 🐍🕸️

Este projeto foi desenvolvido como parte do Módulo 4 do curso de Backend Python da EBAC. O objetivo é realizar web scraping utilizando bibliotecas poderosas do Python, como `requests`, `BeautifulSoup` e `pandas`.

## 🚀 Tecnologias utilizadas
- Python 3.x
- Requests
- BeautifulSoup
- Pandas

## ⚙️ Como executar
1. Crie e ative um ambiente virtual
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Execute o script principal:
```bash
python nome_do_script.py
```

## 👨‍💻 Autor
- Ricardo Ferreira — [GitHub](https://github.com/jrjunior72)

---

## 📦 2. Gerar `requirements.txt`

Isso garante que qualquer pessoa possa rodar o projeto com as mesmas dependências. Dentro da sua venv, rode:

```bash
pip freeze > requirements.txt
```

## 🗂️ Organização da pasta do projeto
```bash
M4_Python_Avancado/
├── data/              # arquivos coletados via scraping
├── src/               # arquivos .py com os scripts
│   └── multithreading_imdb.py
├── notebooks/         # seus .ipynb, se houver
├── requirements.txt
├── README.md
└── .gitignore