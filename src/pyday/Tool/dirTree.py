import os

def dirTree(path, exclude_list=None, max_depth=None, current_depth=0):
    # Get the list of files and directories in the given path
    files = os.listdir(path)
    # Loop through the list
    for file in files:
        # Exclude files or directories in exclude_list
        if exclude_list is not None and file in exclude_list:
            continue
        # If the file is a directory and we haven't exceeded the max depth
        if os.path.isdir(os.path.join(path, file)) and (max_depth is None or current_depth < max_depth):
            # Print the directory name
            print("|   " * current_depth + "|-- " + file)
            # Recursively call the function with the subdirectory as the path and increased depth
            dirTree(os.path.join(path, file), exclude_list, max_depth, current_depth + 1)
        # If the file is a file or we've exceeded the max depth
        else:
            # Print the file name
            print("    " * current_depth + "|-- " + file)