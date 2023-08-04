# convert rfc*.py to regexp csv
import os
import re


def extract_variables(file_path):
    """
    Extract variables from the Python file.

    Args:
        file_path (str): The path of the Python file.

    Returns:
        List[Tuple[str, str]]: A list of tuples. Each tuple contains variable name and variable value.
    """
    with open(file_path, 'r') as f:
        content = f.read()

    # Run the Python script and capture its local variables.
    locals = {}
    exec(content, {}, locals)

    # Filter out built-in functions and classes, keeping only string variables.
    variables = [(name, value) for name, value in locals.items() if isinstance(value, str)]
    return variables


import csv

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['rfc_num', 'rulename', 'regexp'])  # 写入CSV文件的标题行
        writer.writerows(data)  # 写入数据行


# 调用函数将数据写入CSV文件

def main():
    result_folder = 'result/complete_set'
    all_files = os.listdir(result_folder)
    python_files = [file for file in all_files if file.endswith('.py') and file.startswith('rfc')]

    result = []
    for file in python_files:
        # Extract the num from the file name.
        num = int(re.search(r'rfc(\d+).py', file).group(1))
        
        file_path = os.path.join(result_folder, file)
        variables = extract_variables(file_path)

        for variable in variables:
            result.append((num, variable[0], variable[1]))
    print(result)

    write_to_csv('regexp.csv', result)



if __name__ == '__main__':
    main()
