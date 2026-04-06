class Testlab:
    def __init__(self):
        import win32com.client
        self.app = win32com.client.Dispatch("LMSTestLabAutomation.Application")

    def open(self, project_path):
        if self.app.Name == "":
            self.app.Init(f"-w DesktopStandard -t {project_path}")
        else:
            self.app.ActiveBook.Close()
            self.app.OpenProject(project_path)

        from .project import Project
        return Project(self.app)
