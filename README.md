# Foodie Order

Foodie Order é um microsserviço projetado para lidar com o processamento de pedidos em um sistema de entrega de alimentos. Este projeto é construído usando Python e segue as melhores práticas para arquitetura de microsserviços.

## Tabela de Conteúdos
- [Instalação](#instalação)
- [Uso](#uso)
- [Testes](#testes)
- [Cobertura de Testes](#cobertura-de-testes)
- [Docker](#docker)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Instalação

Para configurar o projeto localmente, siga estas etapas:

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/emenezes93/foodie_order.git
    cd foodie_order
    ```

2. **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # No Windows use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para executar a aplicação, use o seguinte comando:

```bash
python main.py
```

Isso iniciará o microsserviço, pronto para lidar com solicitações de processamento de pedidos.

## Testes
Para executar os testes, use o seguinte comando:

```bash
pytest
```

Isso executará a suíte de testes e exibirá os resultados no console.

## Cobertura de Testes
Utilizamos pytest-cov para medir a cobertura dos testes. Abaixo está o relatório de cobertura:

```bash
pytest -vv --cov=. get_pedido_steps.py
```

## Resumo da Cobertura

```bash
---------- coverage: platform win32, python 3.12.3-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
get_pedido_steps.py      27      5    81%
-----------------------------------------
TOTAL                    27      5    81%
```

## Docker
Você também pode executar o serviço usando Docker. Aqui estão as etapas:

Construa a imagem Docker:

1. **Construa a imagem Docker:**
    ```bash
    docker build -t foodie_order .
    ```

2. **Execute o container Docker::**
    ```bash
    docker build -t foodie_order .
    ```

Isso executará a aplicação em um container Docker, acessível em **http://localhost:8000**.