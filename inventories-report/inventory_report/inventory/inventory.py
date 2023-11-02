import csv
import json
import xmltodict
# xmltodict >> https://www.askpython.com/python-modules/xmltodict-module
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        endWith = file_path.split(".")[-1]
        if endWith == "csv":
            result = cls.csv_file(file_path, report_type)
        elif endWith == "json":
            result = cls.json_file(file_path, report_type)
        elif endWith == "xml":
            result = cls.xml_file(file_path, report_type)
        return result

    @classmethod
    def csv_file(cls, path, type):
        with open(path, "r") as file:
            file_csv = csv.DictReader(file)
            data = []
            for item in file_csv:
                data.append(item)
            return cls.generate_report(data, type)

    @classmethod
    def json_file(cls, path, type):
        with open(path, "r") as file:
            data = json.load(file)
            return cls.generate_report(data, type)
           
    @classmethod
    def xml_file(cls, path, type):
        with open(path, "r") as file:
            file_xml = xmltodict.parse(file.read())
            data = []
            for dict in file_xml["dataset"]["record"]:
                data.append(dict)
        return cls.generate_report(data, type)

    @staticmethod
    def generate_report(data, type):
        if type == "completo":
            return CompleteReport.generate(data)
        elif type == "simples":
            print(data)
            return SimpleReport.generate(data)
