def split_file(input_filename, lines_per_file=10000):
    # 打开输入文件
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        # 为输出文件设置计数器
        file_count = 1
        # 当前正在写入的文件对象
        current_output = None
        
        for line_number, line in enumerate(input_file, 1):
            # 如果是第一行或当前行号能被lines_per_file整除，那么创建新的输出文件
            if line_number % lines_per_file == 1:
                # 如果不是第一个文件，先关闭上一个文件
                if current_output:
                    current_output.close()
                # 创建新文件并打开以准备写入
                output_filename = f"split_{file_count}.txt"
                current_output = open(output_filename, 'w', encoding='utf-8')
                file_count += 1
            # 写入当前行到输出文件
            current_output.write(line)
        
        # 在循环结束时确保最后一个文件被正确关闭
        if current_output:
            current_output.close()

# 使用函数分割文件
split_file('./sentence-cut/sentences.txt')