基本命令
git：命令行输入git，可以查看系统有没有安装Git
git config --global user.name "frank"
git config --global user.email "frank.xuan@cxmt.com"
git init：把目录变成Git可以管理的仓库
git add test.py：把文件添加到暂存区
git commit -m "add XXX"：把文件提交到本地版本库(仓库)
git status：随时掌握仓库的状态
git diff：如果git status告知有文件被修改过，用git diff可以查看修改的内容。列出你的当前工作区和暂存区之间的变化
git diff HEAD -- test.py：查看(工作区+暂存区)和版本库里面最新版本的区别
git log：穿梭历史前，用此命令查看提交历史，以便确定要回退到哪个版本，添加--pretty=oneline，精简显示
git reflog：重返未来前，用此命令查看命令历史，以便确定要回到未来的哪个版本
git reset --hard commit_id：使用此命令，在历史版本间穿梭

撤回
场景1：git checkout -- file，该命令可以让这个文件回到最近一次git commit或git add时的状态
场景2：当不但改乱了工作区某个文件的内容，还添加到了暂存区，想丢弃修改，分两步：
    第一步用git reset HEAD <file>，回到场景1
    第二步按场景1操作
场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退

删除
先手动删除文件，然后使用git rm <file>，进而使用git commit -m "XXX"
如果删错了，使用git checkout -- test.py恢复到版本库的最新版本
注意：从来没有被添加到版本库就被删除的文件，是无法恢复的。命令git rm用于删除一个文件。如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失最近一次提交后你修改的内容。

git remote add origin git@server-name:path/repo-name.git：关联一个远程库

git push -u origin master（第一次提交）
git push origin master（第二次及以后的提交）

git remote -v：查看远程库详细信息
git remote rm <name>：此处的“删除”其实是解除了本地和远程的绑定关系，并不是物理上删除了远程库。远程库本身并没有任何改动。要真正删除远程库，需要登录到GitHub，在后台页面找到删除按钮再删除。

git clone git@server-name:path/repo-name.git：克隆一个本地仓库

分支管理
查看分支：git branch，命令会列出所有分支，当前分支前面会标一个*号
创建分支：git branch <name>
切换分支：git checkout <name>或者git switch <name>；git switch master：切换到已有的master分支
创建+切换分支：git switch -c <name>（推荐）；git checkout -b <name>=git branch <name> + git checkout <name>；
合并name分支到当前分支：git merge <name>
删除分支：git branch -d <name>
git log --graph --pretty=oneline --abbrev-commit：查看分支合并图
git merge --no-ff -m "merge with no-ff" dev：合并dev分支到主分支前，禁用fast-forward模式，并commit dev分支&添加备注

Bug分支
首先确定要在哪个分支上修复Bug，git checkout过去，然后创建Bug修复分支
git stash：接到临时紧急开发任务，可以使用该命令把当前工作现场“储藏”起来，等以后恢复现场后继续工作
git stash list：查看stash的列表
git stash pop：恢复工作现场的同时，把stash的内容也删除了
git stash apply stash@{0}+git stash drop：作用同上
git cherry-pick 4c805e2：复制一个特定的提交到当前分支

Feature分支
如果要丢弃一个没有被合并过的分支，可以通过git branch -D <name>强行删除

多人协作
1.要在dev分支上开发，就必须创建远程origin的dev分支到本地：git checkout -b dev origin/dev
2.推送分支：git push origin master，origin是远程仓库名称，master是本地要推送的分支名称，可以为dev
3.推送失败，因为你的小伙伴的最新提交和你试图推送的提交有冲突，解决办法：先用git pull把最新的提交从origin/dev抓下来，然后，在本地合并
    如果git pull提示no tracking information，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream-to <branch-name> origin/<branch-name>，再pull
4.如果合并有冲突，则解决冲突，并在本地提交；
5.没有冲突或者解决掉冲突后，再用git push origin <branch-name>推送就能成功

标签管理
命令git tag <tagname>用于新建一个标签，默认为HEAD，也可以指定一个commit id，git tag <tagname> <commit id>；
命令git tag -a <tagname> -m "blablabla..."可以指定标签信息；
命令git tag可以查看所有标签
git show <tagname>查看标签信息
命令git push origin <tagname>可以推送一个本地标签；
命令git push origin --tags可以推送全部未推送过的本地标签；
如果标签已经推送到远程，要删除远程标签就麻烦一点，先从本地删除：
    命令git tag -d <tagname>可以删除一个本地标签；
    命令git push origin :refs/tags/<tagname>可以删除一个远程标签。

使用github
在GitHub上，可以任意Fork开源仓库
自己拥有Fork后的仓库的读写权限
可以推送pull request给官方仓库来贡献代码
