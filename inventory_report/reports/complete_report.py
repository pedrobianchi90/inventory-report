from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport:
    def generate(inventory):
        simple_report = SimpleReport.generate(inventory)
        comp = Counter(product["nome_da_empresa"] for product in inventory)
        response = "Produtos estocados por empresa:\n"

        for name, quantity in comp.items():
            response += (f"- {name}: {quantity}\n")

        return (
            f"{simple_report}\n"
            f"{response}\n"
        )
