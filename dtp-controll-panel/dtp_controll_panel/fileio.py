import os
import re 
import time
import random
from dptrp1.dptrp1 import DigitalPaper, find_auth_files, get_default_auth_files
ROOT_FOLDER = 'Document'

"""
    Uploads all PDF documents to the root directory of the registered DPT device
"""
def upload_files_to_dpt(directory): 
     
    ## Establish connection
    dpt = DigitalPaper()
    authenticate(dpt)

    fileList = []
     # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    

    pattern = r"\.pdf$"

    # List all files in the directory
    print(f"Files in directory '{directory}':")
    for root, dirs, files in os.walk(directory):
        for file in files:
            filePath = os.path.join(root, file)
            fileList.append(filePath)
            if re.search(pattern, file, re.IGNORECASE):
                print(f"Writing file to DPT :'{file}'")
                # dptrp1 upload ~/Desktop/scan.pdf
                remote_path = add_prefix(ROOT_FOLDER + "/" + os.path.basename(filePath))
                dpt.upload_file(filePath,remote_path)
            else :
                print(f"Invalid file ending (PDFs only allowed) :'{file}'")   

    print("finished")              
            
      
def add_prefix(remote_path: str) -> str:
    return remote_path if remote_path.startswith(ROOT_FOLDER) else f'{ROOT_FOLDER}/{remote_path}'

def authenticate(dpt):
    """
        Logic lifted from dptrp1 cli lib 
    """ 
    
    # When connecting to a device, we default to looking for auth files in
    # both our own configuration directory and in Sony's paths
    found_deviceid, found_privatekey = find_auth_files()
    key = found_privatekey
    client_id = found_deviceid

    if not os.path.exists(key) or not os.path.exists(client_id):
        print("Could not read device identifier and private key.")
        print("Please use command 'register' first:")
        exit(1)
    with open(client_id) as fh:
        client_id = fh.readline().strip()
    with open(key, "rb") as fh:
        key = fh.read()
    dpt.authenticate(client_id, key)

# # Example usage:
directory_path = "/Users/muneebhaq/Downloads/pdf"
upload_files_to_dpt(directory_path)    


"""
    Pick a random a file and flip to a random page
"""
def pick_a_random_file_flip_to_page(): 
     
    ## Establish connection
    dpt = DigitalPaper()
    authenticate(dpt)

    
    print("Picking a random file ")
    print("Pulling files ... ")
    fileList = dpt.list_documents()
    random_number = random.randint(1, len(fileList) -1)

    file = fileList[random_number]
    print(f"File {file["entry_name"]}")  
    total_pages = int(file["total_page"])
    rand_page = 1
    if total_pages > 1:
        rand_page = random.randint(1, int(file["total_page"]) -1)
    print(f"Random page {rand_page}") 
    print("Flipping to random page..")

    entry_id = file["entry_id"]
    dpt.display_document(entry_id,rand_page)

    print("finished")  
