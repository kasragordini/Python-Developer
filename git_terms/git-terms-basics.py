### Introduction to Git

# Print the current working directory.
$ pwd

# Move to the data directory.
$ cd data

# List all files and sub-directories.
$ ls

# Using the terminal, enter the command to find out what version of Git is installed.
$ git --version

# Turn the current directory into a Git repo.
git init

# Create a new Git repo called stress-performance.
$ git init stress-performance

# Change into the stress-performance directory.
$ cd stress-performance

# Check the status of the new repo.
$ git status

# Place report.md, which is in your current working directory, in the staging area. 
$ git add report.md

# Use a single command to add the two modified files to the staging area.
$ git add .

# Check the state of files in the repo.
$ git status

# Make a commit, including an appropriate flag so you can provide a log message "Add 2 participants and update to-do list." as part of the command.
$ git commit -m "Add 2 participants and update to-do list."



### Version History

# Viewing a repository's history
$ git log

# View information about the last two commits only
$ git log -2

# View information about the last two commits made for report.md only.
$ got log -2 report.md

# 

$ git diff			# show changes between all unstaged files and the latest commit
$ git diff report.md		# show changes between an unstaged file and the latest commit
$ git diff --staged		# show changes between all staged files and the latest commit
$ git diff --staged report.md	# show changes between a staged file and the latest commit
$ git diff a864rfcd ebe93178	# show changes between two commits using hash
$ git diff HEAD~1 HEAD~2	# show changes between two commits using HEAD instead of commit hashes

$ git revert HEAD 			# revert all files from a given commit
$ git revert HEAD --no-edit		# revert without opening a text editor
$ git revert HEAD -n			# revert without making a new commit
$ git checkout HEAD~1 -- report.md	# revert a single file from the previous commit
$ git restore --staged report.md	# remove a single file from te staging area
$ git restore --staged			# remove all files from the staging area

