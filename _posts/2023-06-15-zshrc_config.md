---
layout: post
title: 我的zshrc配置
date: 2023-06-15
tags: shell
---

```

# alias proxy='export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890'

alias proxy='export https_proxy=http://user:pwd@127.0.0.1:7890 http_proxy=http://user:pwd@127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890'


# export http_proxy="http://user:pwd@127.0.0.1:7890"
# export https_proxy="http://user:pwd@127.0.0.1:7890"

alias unproxy="unset all_proxy"

alias gitproxy='git config --global http.proxy http://127.0.0.1:7890 && git config --global https.proxy https://127.0.0.1:7890'

alias ungitproxy='git config --global --unset http.proxy && git config --global --unset https.proxy'

alias vscode="open -a 'Visual Studio Code'"
alias pycharm="open -a 'PyCharm'"

export PATH=~/flutter/bin:$PATH

export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn

export PATH=/opt/homebrew/opt/ruby/bin:$PATH
export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
export PATH=`gem environment gemdir`/bin:$PATH
# Add RVM to PATH for scripting. Make sure this is the last PATH variable change.
export PATH="$PATH:$HOME/.rvm/bin"


export PATH=$PATH:/usr/local/mysql/bin
export PATH=$PATH:/usr/local/mysql/support-files

```
