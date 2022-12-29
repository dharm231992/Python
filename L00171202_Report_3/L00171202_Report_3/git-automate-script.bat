@echo off
:: Bat file to automate git steps
:: Git status to find the status of the commit
git status
echo '**************************************************'
echo "Performing an add for all files in this directory"
:: Git add . includes all the files in current folder
git add .
git status
echo '**************************************************'
echo 'Enter the commit message:'
read CommitMessage
:: Git commit used to commit 
git commit -m "$CommitMessage"
git status
echo '**************************************************'
echo 'Pushing to GITHUB repository'
:: Push committed folders/files to remote origin master branch
git push -u origin master
echo '**************************************************'
echo 'Done!'