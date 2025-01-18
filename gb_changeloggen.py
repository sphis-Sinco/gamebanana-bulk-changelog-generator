# This script automatically generates a Bulk changelog to add onto gamebanana

# 1.0 - Base Script
# 1.1 - Directory var, tab support, a tab character variable, and a github page!
# 1.2 - missing "/" at the end of directory check, and quotes for the directory of the "written to" text

# Written by Sphis_Sinco for "Fun over Money".
# This cool little minecraft (java edition) mod ;)
# https://gamebanana.com/mods/569653

# this controls the directory
directory = ""

# make sure there is a / at the end
if not directory.endswith('/'):
    directory = directory + "/"

# this controls what kind of "tab" is checked for
tab_char = "    "
tab_char_len = tab_char.__len__()

# Changelog variables
changelog = ""
gamebanana_changelog = ""

# progress variables
progress = 0
max_progress = 0

# read the log.txt file
f = open(f"{directory}log.txt", "r")
changelog = f.read()

# set the array_logs and max_progress variables
array_logs = changelog.split('\n')
max_progress = array_logs.__len__()

# this function does the actual ", {changelog entry type}"
def checkFor(checking, prefix, suffix):
    returnval = ""

    if checking.startswith(f"- {prefix} ") :
        returnval = checking.removeprefix(f"- {prefix} ")
        returnval = returnval + f", {suffix}"

        return returnval

    return checking

index = 0
for entry in array_logs:
    entry1 = entry
    check = entry1
    tabcount = 0
    while check.startswith('    '):
        check = entry1.removeprefix('    ')
        entry1 = check
        tabcount = tabcount + 1
    addition = check

    # check for different keywords after seeing if the current entry is a changelog entry
    if check.startswith('- '):
        addition = checkFor(addition, "Added", "Addition")
        addition = checkFor(addition, "Removed", "Removal")
        addition = checkFor(addition, "Reworked", "Overhaul")
        addition = checkFor(addition, "Changed", "Tweak")
        addition = checkFor(addition, "Fixed", "Bugfix")

    gamebanana_changelog = gamebanana_changelog + addition

    # prevent extra line break
    if index + 1 != array_logs.__len__():
        gamebanana_changelog = gamebanana_changelog + "\n"


    index=index + 1
    progress = progress + 1

    # print progress
    print(f"Progress: {round(progress/max_progress*100)}% | removed {tabcount} \"{tab_char_len} character\" tabs")


# write to the final_log.txt file
the_log = open(f'{directory}final_log.txt', 'w')
the_log.write(gamebanana_changelog)
print(f"Written to \"{directory}final_log.txt\"")