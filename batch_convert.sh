#!/bin/bash

export PYTHONPATH=.
# 定义文件夹路径
folder_path="/home1/xieziyue/abnf-extractor/abnf/complete_set/"


# 定义错误日志文件路径
error_log="error_log.txt"

# 删除旧的错误日志文件（如果存在）
rm -f "$error_log"

# 获取文件夹中所有文件的列表
file_list=$(find "$folder_path" -type f)

# 循环处理每个文件
for file_path in $file_list; do
    # 提取文件名（不包含路径）
    file_name=$(basename "$file_path")

    echo "Processing file: $file_name"
    # 定义输出文件路径
    output_path="result/complete_set/${file_name%.*}.py"

    # 执行指令并捕获错误输出
    error_output=$(python abnf_to_regexp/main.py -i "$file_path" -o "$output_path" --format python-nested 2>&1 >/dev/null)
    
    # 检查是否有错误输出
    if [[ -n $error_output ]]; then
        # 记录错误到日志文件
        echo "Error processing file: $file_name" >> "$error_log"
        echo "$error_output" >> "$error_log"
    fi
done
