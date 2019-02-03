GIT


[] are optional
<> are placeholders, must use some argument

Save git credentials:
    https://stackoverflow.com/questions/35942754/how-to-save-username-and-password-in-git
    ```
    git config credential.helper store
    git pull
    ```

Visualize git commit history:
    https://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git
    git log --graph --oneline

See diff between working directory and previous commit
git diff
git diff --staged to compare working directory and staging area
git diff filename.js to specfically compare that file
git diff commit-SHA1 to compare old commits
git show - show changes made in a commit


Delete unused git branches
https://stackoverflow.com/questions/6127328/how-can-i-delete-all-git-branches-which-have-been-merged
To delete all local branches that are already merged into the currently checked out branch:
git branch --merged | egrep -v "(^\*|master|dev)" | xargs git branch -d
git branch -d deletethisbranch
git push --delete origin branchname
git remote prune origin

Git reset
https://stackoverflow.com/questions/3528245/whats-the-difference-between-git-reset-mixed-soft-and-hard

Get deleted file
    git checkout commit~1 filename
Get deleted commits
    git log --reflog
Get deleted stuff in staging
    git fsck --lost-found
    
git remote add origin /s/remote-project/1

git push/pull remoterepo branch

git log --grep="#1234" find all commits with #1234

https://jfguan:Poiuqwer0!@gitlab.com/jfguan/eecs_201.git
35etGgzzHHGAn_rn8oze