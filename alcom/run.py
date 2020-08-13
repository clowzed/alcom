import argparse
try:
	from alcom.aligner import CommentsAligner
except:
	from aligner import CommentsAligner

import pathlib

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', required=False, type=str)
	parser.add_argument('-nbc', '--align_no_blank_comments', required = False, action = 'store_true')
	args = parser.parse_args()

	align_function = CommentsAligner.align_comments_in_line

	if args.align_no_blank_comments:
		align_function = CommentsAligner.align_no_blank_comments

	aligner = CommentsAligner(align_function=align_function)

	if args.file:
		filename = pathlib.Path(args.file)

		if not filename.is_file():
			print("File was not found!")
		else:
			aligner.align_comments(filename)

	else:
		aligner.align_directories(pathlib.Path.cwd())

if __name__ == '__main__':
	main()
