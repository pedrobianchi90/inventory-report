from collections import Counter


class SimpleReport():
    @staticmethod
    def generate(inventory: list):
        list = []

        oldest = min(product["data_de_fabricacao"] for product in inventory)
        expire_next = min(product["data_de_validade"] for product in inventory)

        for item in inventory:
            list.append(item["nome_da_empresa"])

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {expire_next}\n"
            f"Empresa com mais produtos: {Counter(list).most_common()[0][0]}"
            )
