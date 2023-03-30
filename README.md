# Find the Missing Media
Purpose: Automate finding the missing photo and video when importing from iOS devices or camera storage cards.

Reason: To increase efficiency of verifiying and logging the possibly missing photos and videos.


***House Keeping***
- Name change for project is work in progress (WIP)
- The commands mentioned, so experiences on Windows and Linux may vary.
- If you encounter an issue on a step and there's no additional information, use them Google skills! It'll be good practice :3

Blog post: 
- TBA

Video demo:
- TBA
____
# Requirements
- A computer (desktop or laptop) that can run MacOS, Windows, or Linux

____
# Instructions

1. Make sure Python is installed. If it isn't, [check Python's official guide on how to](https://wiki.python.org/moin/BeginnersGuide/Download)!

1. Download the zip, which is found in the releases page ([here](https://github.com/SeikaHirori/checkAllPhotos/releases)). Download the latest release under "Assets"

1. Extract the files from the downloaded zip file to the desktop. [^1]

1. Open a terminal to the extracted folder.
    - We will be using this for the rest of the session.

1. Create a virtual environment (venv) by running the command [^2]:
    `python3 -m venv venv`

1. Run the environment by using the command[^3]:
    `source venv/bin/activate`

1. Install the required library by running:
    `pip install -r requirements.txt`

1. Now, move the photos and videos in the folder "_media"

1. Run the command:
    `python3 main.py`

1. Enter the first IMG's digit
    - Ex: If the first/smallest IMG is "IMG_0038", type and enter "38"

1. Enter the last IMG's digit
    - Ex: If the last/largest IMG is "IMG_0090", type and enter "90"

1. If successful, check the "_excel" folder and view the newly created xlsx (Microsoft's Excel) spreadsheets of the following categories:
    - Duplicate Images
    - Misc File
    - Missing Media
    - Original Image

1. To check for missing IMGs, view the spreadsheet that contains "missing_media".

# Additional Information

[^1]: Any location is fine, but Desktop simplifies the process :3

[^2]: Information on venv found [here](https://docs.python.org/3/library/venv.html#creating-virtual-environments) :3

[^3]: Info for other platforms: [here](https://docs.python.org/3/library/venv.html#how-venvs-work) :3
