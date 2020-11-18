export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/data/data/com.termux/files/usr/bin"
export LC_ALL=C
################################## npm install ##################################
if [ ${GitPullExitStatus} -eq 0 ]; then
  PackageListNew=$(cat package.json)
  if [ "${PackageListOld}" != "${PackageListNew}" ]; then
    echo -e "检测到 ${ScriptsDir}/package.json 内容有变化，再次运行 npm install...\n"
    npm install || npm install --registry=https://registry.npm.taobao.org
    if [ $? -ne 0 ]; then
      echo -e "\nnpm install 运行不成功，自动删除 ${ScriptsDir}/node_modules 后再次尝试一遍..."
      rm -rf ${ScriptsDir}/node_modules
    fi
    echo
  fi
  if [ ! -d ${ScriptsDir}/node_modules ]; then
    echo -e "运行npm install...\n"
    npm install || npm install --registry=https://registry.npm.taobao.org
    if [ $? -ne 0 ]; then
      echo -e "\nnpm install 运行不成功，自动删除 ${ScriptsDir}/node_modules...\n请进入 ${ScriptsDir} 目录后手动运行 npm install...\n"
      rm -rf ${ScriptsDir}/node_modules
      exit 1
    fi
  fi
fi