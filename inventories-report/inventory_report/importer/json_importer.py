from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file_path):
        endWith = file_path.split(".")[-1]
        if endWith == "json":
            with open(file_path, "r") as file:
                data = json.load(file)
                return data
        else:
            raise ValueError("Arquivo inválido")
