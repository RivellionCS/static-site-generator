import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file_1, open(template_path, "r") as file_2:
        markdown_file = file_1.read()
        template_file = file_2.read()
    html_node = markdown_to_html_node(markdown_file).to_html()
    page_title = extract_title(markdown_file)
    template_file = template_file.replace("{{ Title }}", page_title)
    template_file = template_file.replace("{{ Content }}", html_node)
    template_file = template_file.replace('href="/', f'href="{basepath}')
    template_file = template_file.replace('src="/', f'src="{basepath}')
    dir_path = os.path.dirname(dest_path)
    if dir_path != "" and not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    with open(dest_path, "w") as written_file:
        written_file.write(template_file)