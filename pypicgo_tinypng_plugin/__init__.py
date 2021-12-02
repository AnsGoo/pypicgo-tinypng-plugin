import tinify
from pathlib import Path
from pypicgo.core.base.plugin import BeforePlugin
from pypicgo.core.base.file import UploadFile

BASE_DIR = Path(__file__).resolve().parent


class TinypngPlugin(BeforePlugin):
    name = 'tinypng'

    def __init__(self, key: str, **kwargs):
        super().__init__(**kwargs)
        self.key = key

    def execute(self, file: UploadFile) -> UploadFile:
        filepath = file.tempfile.resolve()
        filename = file.tempfile.name
        tinify.key = self.key
        after_filepath = BASE_DIR.joinpath('temp')
        if not after_filepath.exists():
            after_filepath.mkdir(parents=True)
        after_filepath = after_filepath.joinpath(filename)
        tinify.from_file(str(filepath)).to_file(str(after_filepath.resolve()))
        file.tempfile = after_filepath
        return file
