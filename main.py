### BACKGROUND:
    # This is for checking if all media files of iOS's Photos App exported to SD card

# create an array that ranges from 0000 to most recent number of media file var "numberRanges"

# Scan for all files in folder, then store each file name as a String into a new array "items_in_folder"

# create another array where if file number is found within the folder, it gets moved to this array: var fileFounded

# Create another array for duplicates
    # if statement: check if duplicate item is in  var "fileFounded" first
    # Next spot to check is in var "items_in_folder"