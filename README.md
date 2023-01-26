# API Django Calculadora de Pitagoras

**Autor**: Weslley Augusto de Oliveira

**Resumo**: API criada para ser consumida pelo projeto [Calculadora de Pitagoras](https://github.com/wedi0/Calculadora-Pitagoras-Reactjs).

## Observações:

* Primeira vez que uso Django.
* Esse projeto tem como finalidade documentar meu processo mais ou menos passo a passo de como tudo foi feito.

# Projeto

Antes de tudo, primeiro vamos nos inteira sobre dois conceitos: 
* O que é um framework?
* O que é uma API?

## O que é um Framework?

*Um framework em desenvolvimento de software, é uma abstração que une códigos comuns entre vários projetos de software provendo uma funcionalidade genérica. Um framework pode atingir uma funcionalidade específica, por configuração, durante a programação de uma aplicação*.
  
A grosso modo podemos definir um framework como uma ferramenta que facilitar o desenvolvimento de projetos.

## O que é uma API?

*API significa Application Programming Interface (Interface de Programação de Aplicação). No contexto de APIs, a palavra Aplicação refere-se a qualquer software com uma função distinta. A interface pode ser pensada como um contrato de serviço entre duas aplicações.*

Em outras palavras, API é um intermediário entre o cliente e a aplicação. Por exemplo, você vai até um restaurante, um garçom anota seu pedido e envia para cozinha que, por sua vez, visualiza o pedido, prepara a comida e entrega ao garçom para ele servir você(o cliente). Nesse exemplo o garçom é a API, pois ele intermedia a cozinha e o cliente.  

# Django

Django é um framework para desenvolvimento rápido para web, escrito em Python. Neste framework também é possível desenvolvermos APIs, por isso minha usei ele na construção da minha. 

### COMO BAIXAR, INSTALAR E USAR? 

* 1º passo, precisar ter o Python instalado.
* 2º passo, criar um diretório para o Projeto.
* 3º passo, criar o ambiente de desenvolvimento com o comando: `python -m venv <nome_projeto>`
* 4º passo, inicializar o ambiente de desenvolvimento: `source nome_da_virtualenv/bin/activate` (linux) `nome_da_virtualenv/Scripts/Activate`(Windows)
* 5º passo, instalar Django no seu ambiente de dev. com o seguinte comando(dar cd no ambiente dev. criado): `pip install django`
* 6º passo, instalar Djangoframework: `pip install djangorestframework`
* 7º passo, criar projeto Django: `django-admin startproject <nome_projeto>`
* 8º passo, criar sua aplicação dentro do projeto Django: `django-admin startapp <nome_app>`
