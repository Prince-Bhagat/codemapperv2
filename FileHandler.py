import os


def get_file_paths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))

    return file_paths


def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


# Example usage:
directory_path = '/path/to/your/directory'
paths = get_file_paths(directory_path)

# Print the paths of all files
for path in paths:
    print(path)
