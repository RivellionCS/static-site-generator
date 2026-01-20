import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    directory_list = os.listdir(dir_path_content)
    for item in directory_list:
        item_source_path = os.path.join(dir_path_content, item)
        item_destination_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_source_path):
            if not item_source_path.endswith(".md"):
                continue
            root, ext = os.path.splitext(item_destination_path)
            html_path = root + ".html"
            generate_page(item_source_path, template_path, html_path, basepath)
        else:
            os.makedirs(item_destination_path, exist_ok=True)
            generate_pages_recursive(item_source_path, template_path, item_destination_path, basepath)