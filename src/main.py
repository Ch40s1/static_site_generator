import os
import shutil
from pathlib import Path

from copystatic import copy_files_recursive
from block_markdown import markdown_to_html


dir_path_static = "./static"
dir_path_public = "./public"
template_path = "./template.html" # Path to the template file
# from_path = "./content/index.md" # Path to the markdown file
# dest_path = "./public/index.html" # Path to the destination file
dir_path_content = "./content"
dest_dir_path = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    print("Generating pages...")
    generate_page_recursive(dir_path_content, template_path, dest_dir_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path} template")
    with open(from_path, 'r') as f:
        content = f.read()
    with open(template_path, 'r') as f:
        template = f.read()

    html_content = markdown_to_html(content).to_html()
    html_title = extract_title(from_path)

    html = template.replace("{{ Content }}", html_content)
    html = html.replace("{{ Title }}", html_title)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(html)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    content = os.listdir(dir_path_content)
    for file in content:
        # join the file to the content directory path /filename
        from_path = os.path.join(dir_path_content, file)
        # join the file to the destination directory (public) /filename
        dest_path = os.path.join(dest_dir_path, file)
        print(f"from_path: {from_path}")
        print(f"dest_path: {dest_path}")
        if os.path.isfile(from_path):
            # is it is a file then add the fuffix to the file in path /filename.html
            dest_path = Path(dest_path).with_suffix(".html")
            # from path tis markdown, and dest path is the public directory
            generate_page(from_path, template_path, dest_path)
        else:
            generate_page_recursive(from_path, template_path, dest_path)







def extract_title(markdown):
    try:
        with open(markdown, 'r') as f:
            while True:
                line = f.readline()
                if line.startswith('#') and line.count('#') == 1:
                    return line[1:].strip()
                if not line:
                    return None
    except FileNotFoundError:
        print(f"File not found: {markdown}")

main()
