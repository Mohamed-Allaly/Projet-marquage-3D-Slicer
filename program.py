import os, sys, re


def mark(file):
    my_pattern = "[\w\d\s\$\&\+\,\:\;\=\?\@\#\|\<\>\.\^\*\(\)\%\!\-\\\/]"
    content = ''
    output = ''
    comment_opened = False
    with open(file, 'r') as f:
        content = f.read()
    for line in content.split('\n'):
        if not line.strip().startswith('#'):
            matches = re.findall(f'\"[^\"][^\"]{my_pattern}+\"|\'[^\'][^\']{my_pattern}+\'|\(\".+\"+\)', line)
            for word in matches:
                line = line.replace(word, f"_({word})")
            output += line + "\n"
        else:
            output += line + "\n"
    with open(file, 'w') as f:
        f.write(output)

def walk(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith('.py'):
				mark(os.path.join(root,  file))

def main(argv):
	walk(argv)


if __name__ == '__main__':
	main(sys.argv[1])