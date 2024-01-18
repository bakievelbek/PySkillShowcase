"""
Single Responsibility Principle (SRP)

"""


class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def format_json(self):
        return f'{{"title": "{self.title}", "content": "{self.content}"}}'


# SRP is followed here as the Report class is only responsible for holding the report data.

"""
Open/Closed Principle (OCP)

"""


class ReportPrinter:
    def print_report(self, report, formatter):
        formatted_report = formatter.format(report)
        print(formatted_report)


class JSONFormatter:
    def format(self, report):
        return report.format_json()


class XMLFormatter:
    def format(self, report):
        # Assume XML formatting implementation
        return "XML formatted report"


# ReportPrinter is open for extension (new formatters can be added) but closed for modification.


"""
Liskov Substitution Principle (LSP)

"""


class ReadOnlyReport(Report):
    def format_json(self):
        # Special implementation for read-only report
        return super().format_json()


# ReadOnlyReport can substitute Report without altering the correctness of the program.


"""
Interface Segregation Principle (ISP)


"""


class Printable:
    def print(self):
        pass


class Savable:
    def save(self):
        pass


class PrintableReport(Report, Printable):
    def print(self):
        # Implementation of print
        pass


class SavableReport(Report, Savable):
    def save(self):
        # Implementation of save
        pass


# By segregating interfaces (Printable and Savable), classes don't rely on interfaces they don't use.


"""
Dependency Inversion Principle(DIP)

"""

from abc import ABC, abstractmethod


class Formatter(ABC):
    @abstractmethod
    def format(self, report):
        pass


class ReportPrinter:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter

    def print_report(self, report):
        formatted_report = self.formatter.format(report)
        print(formatted_report)

# ReportPrinter depends on the Formatter abstraction, not on concrete implementations.
