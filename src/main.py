import os
import shutil


def main():
    if os.path.exists("../public/"):
        shutil.rmtree("../public/")

    os.mkdir("./public/")

    src_dir = "./static/"
    dest_dir = "./public/"

    def copy_directory(src_dir, dest_dir):
        for entry in os.listdir(src_dir):
            src_entry = os.path.join(src_dir, entry)
            dest_entry = os.path.join(dest_dir, entry)

            if os.path.isfile(src_entry):
                shutil.copy(src_entry, dest_entry)

            elif os.path.isdir(src_entry):
                shutil.copytree(src_entry, dest_entry)

    copy_directory(src_dir, dest_dir)


main()
