import secrets
import os


def remove_objects_with_condition(lst, condition):
    return [item for item in lst if not condition(item)]


def get_index_of_element(lst, condition):
    for index, element in enumerate(lst):
        try:
            if condition(element):
                return index
        except:
            continue
    return -1  # Return -1 if no element satisfies the condition


def generate_random_string(length):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_string = ''.join(secrets.choice(alphabet) for _ in range(length))
    return "A" + random_string


def list_files(directory):
    file_names = []
    for root, dirs, all_files in os.walk(directory):
        for current_file in all_files:
            file_path = os.path.join(root, current_file)
            file_names.append(file_path)
    return file_names


def write_to_file(path, output_content):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, 'w') as f2:
        f2.write(output_content)
