import pathlib
import uuid
from typing import Callable, Generator

class FileManager:
	def __init__(self, encoding='utf-8') -> None:
		self.encoding = encoding

	@staticmethod
	def generate_temp_file(filepath:pathlib.Path) -> pathlib.Path:
		current_suffix:str          = filepath.suffix
		new_name      :str          = filepath.with_suffix('').name + str(uuid.uuid4().hex)
		new_filename  :pathlib.Path = filepath.parent.joinpath(new_name).with_suffix(current_suffix)
		return new_filename

	def find_longest_line(self, filepath:pathlib.Path, line_handler:Callable)-> int:
		max_line = max(open(filepath, encoding=self.encoding), key = line_handler)
		return line_handler(max_line)

	@staticmethod
	def find_files_with_extension(directory:pathlib.Path, extension:str) -> Generator[pathlib.Path, None, None]:
		yield from directory.rglob(extension)
