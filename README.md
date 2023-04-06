Git 版本控制学习笔记（二）
2023-02-25
 · 12 分钟 · 5718 字 · Dejavu Moe
目录
准备
git init 初始化
git remote 远程仓库
add 添加
remove 删除
rename 重命名
git pull 拉取
git push 推送
git fetch 获取
pull vs fetch
git checkout 切换
git branch 分支管理
git tag 标签管理
git reset 回退
git revert 撤销
git merge 合并
git base 重放
git stash 贮藏
git cherry-pick 挑选提交
git reflog 回溯
准备
在本文中，我们使用 GitHub 作为远程仓库服务器，先创建一个新的 Git 远程仓库，我们的 Git 之旅从这里开始。

本文记录过程中，创建的远程仓库：MoeOffice/Git-Travel

Git 中的命令和参数繁多且灵活，不可能全部都记得，本文在 ChatGPT 的帮助下完成，作为方便自己日后查阅的 Cheat Sheet 🤤

git init 初始化
在本地初始化一个 Git 仓库

mkdir Git-Travel
cd Git-Travel
git init
# 输出
Initialized empty Git repository in /Users/dejavu/MoeOffice/Git-Travel/.git/
git remote 远程仓库
git remote 命令用于管理本地 Git 仓库与远程仓库之间的连接

add 添加
添加远程仓库，用法

git remote add <name> <url>

# 比如
git remote add origin git@github.com:MoeOffice/Git-Travel.git
注意： origin是默认的远程仓库名称，通常是指 Git 仓库的主机或者托管平台。当你使用 git clone 命令从一个远程 Git 仓库中克隆代码库时，Git 会自动为你设置一个名为 origin 的远程仓库，以便在将来能够与原始代码库进行交互。

通常情况下，origin 是指向远程代码仓库的 URL 地址，通过它可以访问和操作远程代码库。在进行 Git 操作时，你可以使用 origin 来指代远程代码库，例如 git push origin master 表示将本地分支的变更推送到远程仓库 origin 上的 master 分支。

需要注意的是，origin 只是一个默认的远程仓库名称，你可以使用其他名称来代替它。当你需要与多个远程仓库交互时，可以使用不同的名称来标识它们，例如 git remote add upstream <url> 可以将一个新的远程仓库添加到本地仓库中，并指定它的名称为 upstream。

查看远程仓库信息

git remote -v

# 示例输出
origin	git@github.com:MoeOffice/Git-Travel.git (fetch)
origin	git@github.com:MoeOffice/Git-Travel.git (push)
remove 删除
从本地 Git 仓库删除远程仓库

git remote remove <name>

# 比如
git remote remove origin

# 现在查看信息，应该输出为空
git remote -v
为了继续学习，我们将远程仓库添加回来

git remote add origin git@github.com:MoeOffice/Git-Travel.git
rename 重命名
重命名远程仓库

git remote rename <old-name> <new-name>

# 比如
git remote rename origin upstream

# 现在查看信息
git remote -v
upstream	git@github.com:MoeOffice/Git-Travel.git (fetch)
upstream	git@github.com:MoeOffice/Git-Travel.git (push)
为了继续学习，我们将远程仓库命名改回来

git remote rename upstream origin
git pull 拉取
我在远程仓库做了一些更改，现在我想让本地仓库同步这些更改，用法

git pull <remote> <branch>

# 比如
git pull origin master
From github.com:MoeOffice/Git-Travel
 * branch            master     -> FETCH_HEAD
