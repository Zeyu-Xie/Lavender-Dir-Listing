import os
import shutil
from jinja2 import Template

def get_template():
    with open(os.path.join(os.path.dirname(__file__), "template.html"), "r") as f:
        return f.read()
tp = Template(get_template())

# func: Determine if a folder has an index.html file
def have_index_html(path):
    if os.path.isdir(path):
        if "index.html" in os.listdir(path):
            return True
    return False

# func: Construct pages
def page_construct(path, relpath):
    item_list = []
    for item in os.listdir(path):
        if item != "index.html":
            item_list.append(item)
    return tp.render(title=relpath, item_list=item_list)

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