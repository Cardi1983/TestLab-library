class Section:
    def __init__(self, db, name):
        self.db = db
        self.name = name

    def list(self):
        elements = self.db.ElementNames(self.name, 1)
        return [elements.Item(i) for i in range(elements.Count)]

    def get(self, item_name):
        full_path = f"{self.name}/{item_name}"
        return self.db.GetItem(full_path)
