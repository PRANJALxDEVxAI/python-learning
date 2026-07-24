import argparse

parser = argparse.ArgumentParser()

parser.add_argument("url" , help = "Url of the file to download")
parser.add_argument("output" , help = "by which name do you want to save your file")

args = parser.parse_args()

print(args.url)
print(args.output)

