import argparse
from alcom.aligner import CommentsAligner
import pathlib

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', required=False, type=str)
	args = parser.parse_args()

	aligner = CommentsAligner()

	if args.file:
		filename = pathlib.Path(args.file)
		if not filename.is_file():
			print("File was not found!")
		else:
			aligner.align_comments(filename)
	else:
		for file in pathlib.Path().cwd().rglob('*.asm'):
			aligner.align_comments(file)

if __name__ == '__main__':
	main()
