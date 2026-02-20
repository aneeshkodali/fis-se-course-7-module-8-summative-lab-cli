import json
import os

def load_data(file_path: str) -> list:
    '''
    Arguments:
    - file_path: File path

    Returns data from list (empty if not found)
    '''

    # end early if no file found
    if not os.path.exists(file_path):
        return []
    
    # try to return file contents
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except Exception as e:
            print(f"Error when retrieving file data: {e}")
            return []

def save_data(
    file_path=str, 
    data=list
):
    '''
    Arguments:
    - file_path: File path
    - data: Data to write to file path
    '''
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)