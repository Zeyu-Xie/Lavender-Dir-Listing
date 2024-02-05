import os
import sys
import shutil

root_file_path = "/github/workspace"
root_page_path = "/_site_Lavender_Dir_Listing"

def write_file(path, content):
    with open(path, "a") as file:
        file.write(content)
        file.close()
        
def dfs(path):

    file_path = os.path.abspath(os.path.join(root_file_path, path))
    page_path = os.path.join(os.path.join(root_page_path, path), "index.html")

    write_file(page_path, "")

    file_list = os.listdir(file_path)

    for item in file_list:

        file_path_ = os.path.join(file_path, item)
        page_path_ = os.path.join(os.path.join(root_page_path, path), item)
        path_ = os.path.join(path, item)

        if os.path.isfile(file_path_):
            shutil.copy(file_path_, page_path_)
            write_file(page_path, f"<a href=\"./{item}\">{item}</a>"+"\n")
        elif os.path.isdir(file_path_):
            write_file(page_path, f"<a href=\"./{item}\">{item}</a>"+"\n")
            os.mkdir(page_path_)
            dfs(path_)

if __name__ == "__main__":

    if len(sys.argv) > 1:

        list = os.listdir(sys.argv[1])
        print(list)
        
        root_file_path = sys.argv[1]
        dfs("")
        
    else:
        print("no directory specified")
        sys.exit()
    