import requests
from behave import given, when, then

# URL base da API
URLS = {
    'gerarPagamento': 'http://localhost:5000/api/gerarPagamento',
    'atualizarPagamento': 'http://localhost:5000/api/atualizarPagamento'
}

# Dados para os testes
ATUALIZAR_DATA = {
    'codigo': '5432',
    'token': '77777',
    'status': '2'
}

GERAR_DATA = {
    'cpf': '12345678901',
    'nome': 'Cliente de Teste',
    'email': 'cliente@teste.com',
    'token':'77777',
    'status':'1',
    'codigo':'5432',
    'valor':'100.00'
}

# Variáveis para armazenar respostas
qr_code_url = None
response = None

@given('Codigo do pedido,token e status')
def step_impl(context):
    context.data = ATUALIZAR_DATA
    context.url = URLS['gerarPagamento']

@given('um novo cliente com CPF, nome, email, token, status,codigo e valor')
def step_impl(context):
    context.data = GERAR_DATA
    context.url = URLS['atualizarPagamento']

@when('faço uma solicitação POST para a URL de pedidos')
def step_impl(context):
    global qr_code_url
    response = requests.post(context.url, json=context.data)
    context.response = response
    if response.status_code == 200:
        qr_code_url = response.json().get('qr_code_url')

@when('faço uma solicitação POST para a URL de clientes')
def step_impl(context):
    response = requests.post(context.url, json=context.data)
    context.response = response

@when('faço uma solicitação GET para a URL de pedidos')
def step_impl(context):
    response = requests.get(URLS['pedido'])
    context.response = response

@then('recebo um código de resposta 200')
def step_impl(context):
    assert context.response.status_code == 200

@then('recebo um código de resposta 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('recebo um URL do QR code de pagamento')
def step_impl(context):
    assert qr_code_url is not None

@then('recebo um código de resposta 405')
def step_impl(context):
    assert context.response.status_code == 405

@then('recebo uma mensagem de erro indicando que devo usar o método POST')
def step_impl(context):
    expected_message = 'Use POST method to create a new order.'
    response_message = context.response.json()['message']
    assert response_message == expected_message

@then('recebo uma confirmação de criação de cliente')
def step_impl(context):
    expected_message = 'Cliente criado com sucesso'
    response_message = context.response.json().get('message', '')
    assert expected_message in response_message