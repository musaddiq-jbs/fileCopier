# File Copy Script

This Python script allows you to copy files with a specific file type extension recursively from a source directory to a destination directory.

## Prerequisites

- Python 3.x installed on your system

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where the script is located.

3. Run the script with the following command:

   ```
   python script_name.py --source /path/to/source/directory --destination /path/to/destination/directory --extension file_extension
   ```

   Replace `script_name.py` with the actual name of the script file, `/path/to/source/directory` with the path to the source directory, `/path/to/destination/directory` with the path to the destination directory, and `file_extension` with the desired file type extension (e.g., txt, pdf, jpg).

   For example:

   ```
   python script_name.py --source /home/user/documents --destination /home/user/backup --extension txt
   ```

   This command will copy all files with the ".txt" extension from the "/home/user/documents" directory and its subdirectories to the "/home/user/backup" directory.

## Arguments

The script accepts the following command-line arguments:

- `--source`: Required. The path to the source directory from which files will be copied.
- `--destination`: Required. The path to the destination directory where the files will be copied to.
- `--extension`: Required. The file type extension to filter the files (e.g., txt, pdf, jpg).

## Example

Suppose you have the following directory structure:

```
/home/user/documents/
    ├── file1.txt
    ├── file2.pdf
    ├── file3.txt
    └── subfolder/
        ├── file4.txt
        └── file5.pdf
```

Running the script with the following command:

```
python script_name.py --source /home/user/documents --destination /home/user/backup --extension txt
```

will copy all files with the ".txt" extension from "/home/user/documents" and its subdirectories to "/home/user/backup". The resulting directory structure will be:

```
/home/user/backup/
    ├── file1.txt
    ├── file3.txt
    └── file4.txt
```

## Notes

- The script will create the destination directory if it doesn't exist.
- If a file with the same name already exists in the destination directory, it will be overwritten.
- The script will display a message for each file that is copied, indicating the source and destination paths.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).
