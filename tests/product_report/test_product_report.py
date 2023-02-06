from inventory_report.inventory.product import Product


def test_relatorio_produto():
    PRODUCT = {
        'id': 1,
        'nome_do_produto': 'Produto',
        'nome_da_empresa': 'Empresa',
        'data_de_fabricacao': '2023-02-01',
        'data_de_validade': '2024-02-01',
        'numero_de_serie': '123 456 789',
        'instrucoes_de_armazenamento': 'Instruções'
    }

    product = Product(
        PRODUCT['id'],
        PRODUCT['nome_do_produto'],
        PRODUCT['nome_da_empresa'],
        PRODUCT['data_de_fabricacao'],
        PRODUCT['data_de_validade'],
        PRODUCT['numero_de_serie'],
        PRODUCT['instrucoes_de_armazenamento']
    )

    expect = (
        f'O produto {PRODUCT["nome_do_produto"]} fabricado em '
        f'{PRODUCT["data_de_fabricacao"]} por '
        f'{PRODUCT["nome_da_empresa"]} com validade até '
        f'{PRODUCT["data_de_validade"]} precisa ser armazenado '
        f'{PRODUCT["instrucoes_de_armazenamento"]}.'
    )

    assert product.__repr__() == expect
