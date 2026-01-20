import os, shutil, sys
from generate_pages_recursive import generate_pages_recursive

def copy_static_to_docs():
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.mkdir("docs")

    recursive_copy("static", "docs")

def recursive_copy(source, destination):
    directory_list = os.listdir(source)
    for item in directory_list:
        item_source_path = os.path.join(source, item)
        item_destination_path = os.path.join(destination, item)
        if os.path.isfile(item_source_path):
            shutil.copy(item_source_path, item_destination_path)
        else:
            os.mkdir(item_destination_path)
            recursive_copy(item_source_path, item_destination_path)
    


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_static_to_docs()
    generate_pages_recursive("content/", "template.html", "docs/", basepath)

main()