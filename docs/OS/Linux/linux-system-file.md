# System Files

## .bashrc

## .bash_aliases

ABC.. nó là một đoạn script nằm trong `.bashrc`. Một số commands để như sau.

```bash
alias killmkdocs="ps -aux | grep mkdocs | awk '{print $2}' | xargs sudo kill -9"

function foreach_git()
{
   if [ $# -eq 0 ]; then
      echo "Usage: foreach_git <git command>"
      return 1
   fi

   base_dir=$(pwd)

   # Find all .git directories and run command inside their parent directories
   for i in $(find -name .git); do
        cd ${i:2:-4};
        $@;
        cd $base_dir;
   done;
}

function uninstall_package()
{
    if [ $# -eq 0 ]; then
        echo "Need a package name."
        return 1
    fi

    for i in $#; do
        sudo apt-get remove $1 -y;
        sudo apt-get purge $1 -y;
        sudo apt-get autoremove;
        sudo apt-get clean;
    done;
}

```