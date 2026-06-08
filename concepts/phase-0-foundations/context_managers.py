class DatabaseConnection:
    def __enter__(self):
        print("Opening Database Connection...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")

    def query(self):
        print("Running Query")


with DatabaseConnection() as db:
    db.query()
    raise Exception("Something went wrong")

print("Done. ")
