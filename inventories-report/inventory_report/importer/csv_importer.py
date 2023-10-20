from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file_path):
        endWith = file_path.split(".")[-1]
        if endWith == "csv":
            with open(file_path, "r") as file:
                file_csv = csv.DictReader(file)
                data = []
                for item in file_csv:
                    data.append(item)
                return data
        else:
            raise ValueError("Arquivo inválido")
        
