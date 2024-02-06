import os
import sys
import shutil
from jinja2 import Template

root_file_path = "/github/workspace"
root_page_path = "/_site_Lavender_Dir_Listing"
template = ""

def write_file(path, content):
    with open(path, "a") as file:
        file.write(content)
        file.close()
        
def dfs(path):

    data = {
        "repoName": "Lavender Dir Listing",
        "title": os.path.basename(path),
        "list": []
    }

    file_path = os.path.abspath(os.path.join(root_file_path, path))
    page_path = os.path.join(os.path.join(root_page_path, path), "index.html")

    write_file(page_path, "")

    file_list = os.listdir(file_path)

    for item in file_list:

        file_path_ = os.path.join(file_path, item)
        page_path_ = os.path.join(os.path.join(root_page_path, path), item)
        path_ = os.path.join(path, item)
        data["list"].append(item)

        if os.path.isfile(file_path_):
            shutil.copy(file_path_, page_path_)
        elif os.path.isdir(file_path_):
            os.mkdir(page_path_)
            dfs(path_)
    
    write_file(page_path, template.render(data))

if __name__ == "__main__":

    with open('/template.html', 'r') as file:
        template = Template(file.read())

    if len(sys.argv) > 1:
        
        root_file_path = sys.argv[1]
        dfs("")
        
    else:
        print("no directory specified")
        sys.exit()
    