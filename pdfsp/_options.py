from dataclasses import dataclass

from ._typing import T_OptionalPath,Path 


@dataclass
class Options:
    source_folder: T_OptionalPath = None
    output_folder: T_OptionalPath = None
    combine: bool = False

    def __post_init__(self):
        if self.source_folder is None:
            self.source_folder = "."
        if self.output_folder is None:
            self.output_folder = "Output"
        self.source_folder = Path(self.source_folder)
        self.output_folder = Path(self.output_folder)
        # self.source_folder = self.source_folder.resolve()
        # self.output_folder = self.output_folder.resolve()
        self.output_folder.mkdir(parents=True, exist_ok=True)

        self.combine = True if self.combine else False

        self.source_folder = [self.source_folder] if isinstance(self.source_folder, str) else self.source_folder
        self.output_folder = [self.output_folder] if isinstance(self.output_folder, str) else self.output_folder
        self.source_folder = [self.source_folder] if isinstance(self.source_folder, str) else self.source_folder
        self.output_folder = [self.output_folder] if isinstance(self.output_folder, str) else self.output_folder

        if str(self.source_folder).endswith(".pdf"):
            self.source_folder = [self.source_folder]