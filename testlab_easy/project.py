from .section import Section
from .results import Results
from .export import Export
from .processing import Processing


class Project:
    def __init__(self, app):
        self.app = app
        self.db = app.ActiveBook.Database()

        self.export = Export(self)
        self.processing = Processing(self)

    def section(self, name):
        return Section(self.db, name)

    @property
    def results(self):
        return Results(self.db)
