
DIRECTORIES = {
"PDF": [".pdf"],
"VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm",".mpg", ".mpeg", ".mkv"],
"Word": [".docx", ".doc", ".odt", ".docm"],
"PowerPoint": [".ppt",".pptx"],
"Excel":[".xls", ".xlsx", ".csv"],
"Images":[".jpeg", ".jpg", ".tiff",".bmp", ".webp", ".png",  "svg", ".gif"],
"Data":[".yaml",".json",".geojson",".xml",".sld",".ysld",".kmz",".aspx"],
"zip":[".zip",".tar",".gz",".7z"],
"Install":[".exe",".whl"],
"python_and_web":[".py", ".html",".ipynb", ".dta",".cur"]
}

my_path =  "C:/Users/edennis/Downloads/"
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

# The directory to be organised

import os
import shutil
def organiser(my_path):
    """
    Organises files by type in the specified Path
    Args:
        my_path ():

    Returns:

    """
    #print(my_path)
    if os.path.exists(my_path):
        # Check for path
        for file in os.listdir(my_path):
            file_path = os.path.join(my_path, file)
            if os.path.isdir(file_path):
                pass

            filename, fileExtension = os.path.splitext(file_path)
            #split filename and file extension
            print(filename, fileExtension)

            # Get list of keys that contains the given value

            value_collec = [item for sublist in DIRECTORIES.values() for item in sublist]

            if str(fileExtension) in value_collec:
                print(str(fileExtension))
                for key, value in DIRECTORIES.items():
                    # searching for correct key
                    #print(key, value)
                    if fileExtension in value:
                        #print("selected key: ", key)
                        selected_key = key
                        base_file = os.path.basename(file_path)

                        try:
                            destination_path_file = f"{my_path}{selected_key}/{base_file}"
                            destination_path = f"{my_path}{selected_key}/{base_file}"
                            # make directory if it doesn't exist already
                            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                            shutil.move(file_path, destination_path_file)
                        except OSError as err:
                            print("failed OS Error", err)
                        except RuntimeError:
                            print("failed runtime")

if __name__ == '__main__':
    organiser(my_path)

