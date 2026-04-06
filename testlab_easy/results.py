class Results:
    def __init__(self, db):
        self.db = db
        self.path = "Results"

    def write_block(self, name, data, properties=None, overwrite=True):
        print(f"[Testlab] Writing block: {name}")

        self.db.AddItem(
            self.path,
            name,
            data,
            properties,
            overwrite
        )
