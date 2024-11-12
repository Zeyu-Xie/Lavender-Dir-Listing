import os
import shutil
import sys
from jinja2 import Template

def get_template():
    with open(os.path.join(os.path.dirname(__file__), "template.html"), "r") as f:
        return f.read()
tp = Template(get_template())

# Parameters
email = sys.argv[1]
website_name = sys.argv[2]
website_url = sys.argv[3]

# func: Determine if a folder has an index.html file
def have_index_html(path):
    if os.path.isdir(path):
        if "index.html" in os.listdir(path):
            return True
    return False

# func: Construct pages
def page_construct(path, relpath):

    global tp
    global email, website

    title = f"Index of {relpath}"
    item_list = []
    for item in os.listdir(path):
        if item != "index.html":
            item_list.append(item)
    return tp.render(
            email = email, 
            title = title, 
            relpath=relpath, 
            item_list=item_list, 
            website_name=website_name,
            website_url=website_url
        )

# func: dfs
def dfs(prp, relpath):

    path = os.path.join(prp, relpath)

    # Determine if the current folder contains an index.html file
    if not have_index_html(path):
        page = page_construct(path, relpath)
        with open(os.path.join(path, "index.html"), "w") as f:
            f.write(str(page))

    # Recursively call the dfs function for all subfolders
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            dfs(prp, os.path.join(relpath, item))

# func: main
def main(source, folder):

    # Copy all files and folders to the pages root path
    try:
        for item in os.listdir(source):
            if os.path.isfile(os.path.join(source, item)):
                shutil.copy(os.path.join(source, item), folder)
            else:
                shutil.copytree(os.path.join(source, item), os.path.join(folder, item))
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    # dfs
    dfs(folder, ".")


if __name__ == '__main__':

    main("/source", "/folder")