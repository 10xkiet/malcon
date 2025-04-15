import os
import csv
import argparse
import random
def file_label_generator(input_dir):
    """
    Generator that yields (file_path, label) tuples.
    Label is 1 for files under 'malware', 0 for 'benign'.
    """
    label_dirs = {'malware': 1, 'benign': 0}

    for subdir, label in label_dirs.items():
        dir_path = os.path.join(input_dir, subdir)
        if not os.path.exists(dir_path):
            print(f"⚠️  Warning: {dir_path} does not exist, skipping.")
            continue

        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.abspath(os.path.join(root, file))
                yield (file_path, label)

def write_csv(generator, output_csv):
    data_list = list(generator)
    random.shuffle(data_list)
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|')
        count = 0
        for file_path, label in data_list:
            writer.writerow([file_path, label])
            count += 1
    print(f"✅ CSV saved to {output_csv} with {count} entries.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate CSV for MalConv training using an iterator')
    parser.add_argument('input_dir', help='Directory containing malware and benign subfolders')
    parser.add_argument('--output_csv', default='train_data.csv', help='Output CSV file path')
    args = parser.parse_args()

    generator = file_label_generator(args.input_dir)
    write_csv(generator, args.output_csv)
