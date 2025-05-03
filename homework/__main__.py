import sys

from homework.src.wordcount import main

if __name__ == "_main_":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    main(input_dir, output_dir)
