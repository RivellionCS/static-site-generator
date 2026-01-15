import os, shutil

def copy_static_to_public():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")

    recursive_copy("static", "public")

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
    copy_static_to_public()

main()