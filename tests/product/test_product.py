from inventory_report.inventory.product import Product


def test_cria_produto():
    product_instance = Product(
        1,
        "produto",
        "empresa",
        "data de fabricacao",
        "data de validade",
        "número de série",
        "instruções",
    )

    assert product_instance.id == 1
    assert product_instance.nome_do_produto == "produto"
    assert product_instance.nome_da_empresa == "empresa"
    assert product_instance.data_de_fabricacao == str("data de fabricacao")
    assert product_instance.data_de_validade == str("data de validade")
    assert product_instance.numero_de_serie == "número de série"
    assert product_instance.instrucoes_de_armazenamento == "instruções"
