#!/bin/sh

# 获取当前用户的 Git 配置
user_name=$(git config user.name)
user_email=$(git config user.email)

# 检查 user.name 是否以 -srp 结尾
if [[ ! $user_name =~ -srp$ ]]; then
  echo "Error: user.name must end with -srp"
  exit 1
fi

# 检查 user.email 是否以 @srp.one 结尾
if [[ ! $user_email =~ @srp.one$ ]]; then
  echo "Error: user.email must end with @srp.one"
  exit 1
fi

exit 0