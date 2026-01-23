# System Files

## .bashrc

## .bash_aliases

ABC.. nó là một đoạn script nằm trong `.bashrc`. Một số commands để như sau.

```bash
alias killmkdocs='ps -aux | grep mkdocs | awk "{print \$2}" | xargs sudo kill -9'
alias cls=clear
alias cfgalias='sudo nano ~/.bash_aliases && . ~/.bash_aliases'
alias cmd='gnome-terminal &'
alias start="xdg-open"

function fug()
{
	git add .
	git commit -m "update"
	git push origin main
}

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
	echo;
	echo ----- $(pwd) -----
	echo;
        $@;
        cd $base_dir;
	echo;
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