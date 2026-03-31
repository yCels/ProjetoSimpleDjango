# 🎓 Escola API - Django REST Framework

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Este projeto é uma API robusta para gerenciamento escolar, desenvolvida durante o treinamento de **Django REST Framework** na Alura. A aplicação permite o controle completo de alunos, cursos e a gestão de matrículas.

## 📝 Sobre o Projeto

O foco principal foi a criação de uma API utilizando o padrão **MVT (Model-View-Template)** adaptado para o ambiente REST, explorando as facilidades que o Django oferece para produtividade e segurança.

Neste curso, criamos recursos de alunos para disponibilizar e aprendemos a trabalhar com as ações principais do CRUD. Realizamos esse processo para cursos e para matrículas, vinculando os dois modelos. Preparamos nossos `viewsets`, registramos URLs e configuramos detalhes específicos para consultar todas as matrículas de uma pessoa e todos os alunos em um determinado curso.

### Principais Funcionalidades:
* **CRUD Completo:** Operações de criação, leitura, atualização e deleção para Alunos, Cursos e Matrículas.
* **Filtros Customizados:** * Listagem de todas as matrículas de um aluno específico.
    * Listagem de todos os alunos matriculados em um curso específico.
* **Serialização Dinâmica:** Uso de `ModelSerializer` para representação dos dados em JSON, incluindo campos calculados e relações.
* **Autenticação:** Inclusão de autenticação básica para proteger os dados da API.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Django**: Framework web principal.
* **Django REST Framework (DRF)**: Para a construção da camada de API.
* **SQLite**: Banco de dados padrão.

---

## 🚀 Como Iniciar o Projeto Localmente

Siga o passo a passo abaixo para configurar o ambiente e rodar a API na sua máquina:

1.
git clone https://github.com/yCels/ProjetoSimpleDjango

2.
python -m venv venv
venv\Scripts\activate

3.
pip install -r requirements.txt

4.
python manage.py migrate

5.
python manage.py migrate

6.
python manage.py createsuperuser 

7.
python manage.py runserver

<img width="824" height="375" alt="image" src="https://github.com/user-attachments/assets/6db97add-3a98-42a1-8e9d-58b7ab178d38" />

