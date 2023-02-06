from inventory_report.reports.simple_report import SimpleReport
from collections import Counter
from typing import List, Dict


class CompleteReport:
    def generate(data: List[Dict]) -> str:
        simple_report = SimpleReport.generate(data)

        products = Counter(product["nome_da_empresa"] for product in data)
        inventory = ""
        for company, quantity in products.items():
            inventory += f"- {company}: {quantity}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{inventory}"
        )
