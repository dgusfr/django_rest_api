# Django Rest API

API desenvolvoda em Pyhton

## Logo

<div align="center">
  <img src="img/logo.png" alt="Imagem do Projeto" width="900">
</div>

## Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Status](#status)
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Autor](#autor)

## Tecnologias Utilizadas

<div style="display: flex; flex-direction: row;">
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/python.png" alt="Logo Django" width="100"/>
  </div>
</div>

## Status

![Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)

## Descrição

Este projeto consiste em uma API RESTful desenvolvida utilizando o framework Django e o Django Rest Framework. Ele permite a busca e adição de dados relacionados a itens.

## Funcionalidades

- Recuperação de dados existentes na API
- Adição de novos itens à API

## Como Usar

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute as migrações: `python manage.py makemigrations` e `python manage.py migrate`
4. Inicie o servidor: `python manage.py runserver`

## Estrutura do Projeto

- `api/serializers.py`: Contém o serializer para o modelo `Item`.
- `api/urls.py`: Define as URLs da API.
- `api/views.py`: Implementa as views para buscar e adicionar dados.
- `base/models.py`: Define o modelo `Item`.
- `base/views.py`: Pode conter views adicionais relacionadas à lógica de negócios.
- `myproject/urls.py`: Configuração principal das URLs do projeto.
- `myproject/settings.py`: Configurações globais do projeto.

## Autor

Desenvolvido por Diego Franco.
