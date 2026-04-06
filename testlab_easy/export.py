class Export:
    def __init__(self, project):
        self.project = project

    def to_csv(self, block_name, output_path):
        print(f"[Testlab] Exporting {block_name} to {output_path}")

        item = self.project.db.GetItem(f"Results/{block_name}")

        # TODO: implement actual Testlab export logic
