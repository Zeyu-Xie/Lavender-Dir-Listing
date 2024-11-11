import os
import shutil
import yaml
import bs4


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    conf = {}
    with open(config_path, 'r') as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
    return conf

# Determine if a folder has an index.html file


def have_index_html(path):
    if os.path.isdir(path):
        if "index.html" in os.listdir(path):
            return True
    return False

# Construct pages


def page_construct(path, relpath):
    page = bs4.BeautifulSoup(
        "<html><head><title>Index</title></head><body></body></html>", "html.parser")
    # back
    back = page.new_tag("a", href="../")
    back.string = "Back"
    page.body.append(back)
    # title
    title = page.new_tag("h1")
    title.string = relpath
    page.body.append(title)
    # ul
    ul = page.new_tag("ul")
    for item in os.listdir(path):
        if item != "index.html":
            li = page.new_tag("li")
            a = page.new_tag("a", href=f"./{item}")
            a.string = item
            li.append(a)
            ul.append(li)
    page.body.append(ul)
    return page


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


def main(folder):

    rp = os.path.dirname(__file__)  # Root Path
    prp = os.path.join(rp, folder)  # Pages Root Path

    # Copy all files and folders to the pages root path
    try:
        os.makedirs(prp, exist_ok=True)
        for item in os.listdir(rp):
            if os.path.isdir(item):
                if item != "dict":
                    shutil.copytree(item, os.path.join(prp, item))
            else:
                shutil.copy(item, os.path.join(prp, item))
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    # dfs
    dfs(prp, ".")


if __name__ == '__main__':

    config = load_config()
    main(config['folder'])
