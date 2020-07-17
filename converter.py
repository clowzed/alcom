import pathlib
import argparse
COMMENT_SPLITTER:str = ';'

def parse_line(line:str):
	count:int = line.count(COMMENT_SPLITTER) - 1
	line:str = line[::-1].replace(COMMENT_SPLITTER, '', count)[::-1]
	line:str = line.rstrip()
	comment:str = ''
	if COMMENT_SPLITTER in line:
		if not line.lstrip().startswith(COMMENT_SPLITTER):
			line, comment = line.split(COMMENT_SPLITTER)
			comment = comment.strip()
			line = line.rstrip()
		else:
			comment = line.rstrip()
			line = ''
	return line, comment

def max_line_len_in_file(file:pathlib.Path, offset:int):
	max_line_len = 0

	with open(file, encoding = 'utf-8') as f:
		for line in f:
			if COMMENT_SPLITTER in line:
				line, comment = parse_line(line)
			max_line_len = max(max_line_len, len(line))

	return max_line_len + offset

def prettify_comment(line:str, max_len:int):
	line, comment = parse_line(line)

	if not line and not comment:
		return ''
	elif not line:
		return f"{' '*max_len}{comment.strip()}"

	comment = f'{COMMENT_SPLITTER}    {comment}'
	offset_len = max_len - len(line.expandtabs(tabsize = 4))
	comment_offset = ' ' * offset_len
	line = f"{line}{comment_offset}{comment}"
	return line

def align_comments(file:pathlib.Path):
	offset:int = 20
	max_line_len:int = max_line_len_in_file(file, offset)
	new_file:pathlib.Path = file.with_suffix('').with_name(file.with_suffix('').name + '_align').with_suffix('.asm')
	with open(file, encoding = 'utf-8') as f:
		with open(new_file, 'w',encoding = 'utf-8') as new:
			for line in f:
				new.write(prettify_comment(line, max_line_len) + '\n')
	file.unlink()
	new_file.rename(file)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', required=False, type=str)
	args = parser.parse_args()
	if args.file:
		filename = pathlib.Path(args.file)
		if not filename.is_file():
			print("File was not found!")
		else:
			align_comments(filename)
	else:
		for file in pathlib.Path().cwd().rglob('*.asm'):
			align_comments(file)

if __name__ == '__main__':
	main()