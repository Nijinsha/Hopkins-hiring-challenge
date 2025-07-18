import sys
from hopkins.core.workflow import ExecutiveSummaryGenerator

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file.pdf|input_file.txt>")
        sys.exit(1)
    input_path = sys.argv[1]
    generator = ExecutiveSummaryGenerator(input_path)
    generator.run()

if __name__ == "__main__":
    main()
