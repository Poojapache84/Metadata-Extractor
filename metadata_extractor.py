import os
import time


def extract_metadata(filename):

    if os.path.exists(filename):

        print("=" * 45)
        print("      FILE METADATA EXTRACTOR")
        print("=" * 45)

        print(f"File Name       : {os.path.basename(filename)}")
        print(f"File Path       : {os.path.abspath(filename)}")
        print(f"File Size       : {os.path.getsize(filename)} Bytes")

        created = time.ctime(os.path.getctime(filename))
        modified = time.ctime(os.path.getmtime(filename))

        print(f"Created On      : {created}")
        print(f"Modified On     : {modified}")

    else:
        print("File not found.")


extract_metadata("sample.txt")