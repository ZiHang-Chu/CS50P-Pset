# A collection of recognized filetypes
filetypes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}


def main():
    f_name = input("File name: ").strip().lower()
    print(filetype_check(f_name))


def filetype_check(f_name):
    if "." in f_name:
        check = f_name.split(".", 1)
        if check[1] in filetypes:
            return filetypes[check[1]]
        else:
            return "application/octet-stream"
    else:
        return "application/octet-stream"


main()
