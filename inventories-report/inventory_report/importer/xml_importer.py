from inventory_report.importer.importer import Importer
import xmltodict
# xmltodict >> https://www.askpython.com/python-modules/xmltodict-module


class XmlImporter(Importer):
    def import_data(file_path):
        endWith = file_path.split(".")[-1]
        if endWith == "xml":
            with open(file_path, "r") as file:
                file_xml = xmltodict.parse(file.read())
                data = []
                for dict in file_xml["dataset"]["record"]:
                    data.append(dict)
                return data
        else:
            raise ValueError("Arquivo inválido")
