"""
Task: Object-Oriented Programming (OOP) - Data Pipeline Extractor System

Requirements:
1. Build a base DataExtractor class with a shared class counter (total_extractors) and __str__ representation.
2. Create an ApiExtractor child class inheriting from DataExtractor using super().__init__() and adding endpoint_url.
3. Create a DatabaseExtractor child class inheriting from DataExtractor adding db_type and table_name.
4. Override the extract() method in both child classes to demonstrate polymorphism.
5. Create instances in main(), loop through them polymorphically, and print total extractors.

Concepts: Classes & Objects, Inheritance, super(), Method Overriding, Polymorphism, Class Variables vs Instance Variables.
"""

class DataExtractor:

    total_extractors = 0

    def __init__(self, source_name, batch_size):
        self.source_name = source_name
        self.batch_size = batch_size
        DataExtractor.total_extractors += 1

    def extract(self):
        print(f"{self.source_name} extracting {self.batch_size} records")

    def __str__(self):
        return f"{self.source_name} Extractor (Batch: {self.batch_size})"


class ApiExtractor(DataExtractor):

    def __init__(self, source_name, batch_size, endpoint_url):
        super().__init__(source_name, batch_size)
        self.endpoint_url = endpoint_url

    def extract(self):
        print(f"🌐 {self.source_name} Requesting {self.batch_size} records from {self.endpoint_url}...")


class DatabaseExtractor(DataExtractor):

    def __init__(self, source_name, batch_size, db_type, table_name):
        super().__init__(source_name, batch_size)
        self.db_type = db_type
        self.table_name = table_name

    def extract(self):
        print(f"🗄️ {self.db_type} Querying {self.batch_size} rows from table '{self.table_name}'...")


def main():
    api_extractor_1 = ApiExtractor(
        source_name="RemoteOK_Jobs",
        batch_size=500,
        endpoint_url="https://remoteok.com/api"
    )
    db_extractor_1 = DatabaseExtractor(
        source_name="Company_DB",
        batch_size=1000,
        db_type="PostgreSQL",
        table_name="employees"
    )

    objects = [api_extractor_1, db_extractor_1]

    for obj in objects:
        obj.extract()

    print(f"\nTotal Extractors Initialized: {DataExtractor.total_extractors}")


if __name__ == "__main__":
    main()
