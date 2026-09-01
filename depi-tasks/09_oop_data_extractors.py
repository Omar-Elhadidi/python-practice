"""
Task: Object-Oriented Programming (OOP) - Data Extractor Hierarchy

Build an object-oriented data extraction system:
1. Base Class (DataExtractor): Holds common attributes (source_name, batch_size), tracks total extractors, and defines default extract() and __str__() methods.
2. Child Class (ApiExtractor): Inherits from DataExtractor, uses super() to initialize base attributes, adds endpoint_url, and overrides extract().
3. Child Class (DatabaseExtractor): Inherits from DataExtractor, adds db_type and table_name, and overrides extract().
4. Main: Instantiates both extractors and loops through them polymorphically.
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
        print(f"🗄️ {self.db_type} Querying {self.batch_size} rows from table {self.table_name}...")


def main():
    api_extractor_1 = ApiExtractor(source_name="RemoteOK_Jobs", batch_size=500, endpoint_url="https://remoteok.com/api")
    db_extractor_1 = DatabaseExtractor(source_name="Company_DB", batch_size=1000, db_type="PostgreSQL", table_name="employees")

    objects = [api_extractor_1, db_extractor_1]

    for obj in objects:
        obj.extract()


if __name__ == "__main__":
    main()
