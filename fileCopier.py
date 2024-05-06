import os
import shutil
import argparse

def copy_files(source_folder, destination_folder, extension):
    for folder, _, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith(extension):
                source_path = os.path.join(folder, filename)
                destination_path = os.path.join(destination_folder, filename)
                shutil.copy(source_path, destination_path)
                print(f"Copied: {source_path} -> {destination_path}")

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Copy files based on file type extension recursively.')

    # Add arguments
    parser.add_argument('--source', required=True, help='Path to the source directory')
    parser.add_argument('--destination', required=True, help='Path to the destination directory')
    parser.add_argument('--extension', required=True, help='File type extension to filter files (e.g., txt)')

    # Parse arguments
    args = parser.parse_args()

    # Call copy_files function with provided arguments
    copy_files(args.source, args.destination, args.extension)

if __name__ == "__main__":
    main()

