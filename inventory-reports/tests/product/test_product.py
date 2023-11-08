from inventory_report.inventory.product import Product


def test_cria_produto():
    created_product = Product(
        1,
        "MESA",
        "Smarcaro",
        "2021-07-01",
        "2023-03-11",
        "SC11",
        "Utilizar em locais cobertos",
    )

    assert created_product.id == 1
    assert created_product.nome_do_produto == "MESA"
    assert created_product.nome_da_empresa == "Smarcaro"
    assert created_product.data_de_fabricacao == "2021-07-01"
    assert created_product.data_de_validade == "2023-03-11"
    assert created_product.numero_de_serie == "SC11"
    assert (
        created_product.instrucoes_de_armazenamento
        == "Utilizar em locais cobertos"
    )
