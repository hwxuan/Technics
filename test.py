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
