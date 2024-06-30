git：命令行输入git，可以查看系统有没有安装Git
git config --global user.name "xuanhongwei"
git config --global user.email "1325997218@qq.com"
git init：把目录变成Git可以管理的仓库
git add test.py：把文件添加到仓库
git commit -m "add XXX"：把文件提交到仓库
git status：随时掌握工作区的状态
git diff：如果git status告知有文件被修改过，用git diff可以查看修改的内容
git log：穿梭历史前，用此命令查看提交历史，以便确定要回退到哪个版本，添加--pretty oneline，精简显示
git reflog：重返未来前，用此命令查看命令历史，以便确定要回到未来的哪个版本
git reset --hard commit_id：使用此命令，在历史版本间穿梭

撤回
场景1：当改乱了工作区/暂存区某个文件的内容，想直接丢弃工作区/暂存区的修改时，用命令git checkout -- file
场景2：当不但改乱了工作区某个文件的内容，还添加到了暂存区，想丢弃修改，分两步，第一步用git reset HEAD <file>，就回到了场景1，第二步按场景1操作
场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退

删除
先手动删除文件，然后使用git rm <file>，进而使用git commit -m "XXX"
如果删错了，使用git checkout -- test.py恢复到版本库的最新版本
注意：从来没有被添加到版本库就被删除的文件，是无法恢复的

git remote add origin git@server-name:path/repo-name.git：关联一个远程库
密码：公钥SSH
密码：允许访问SSH的密码

git push -u origin master（第一次提交）
git push origin master（第二次及以后的提交）

git remote -v：查看远程库信息
git remote rm <name>：此处的“删除”其实是解除了本地和远程的绑定关系，并不是物理上删除了远程库。远程库本身并没有任何改动。要真正删除远程库，需要登录到GitHub，在后台页面找到删除按钮再删除。