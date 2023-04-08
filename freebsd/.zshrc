# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/USER/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
PS1='%n@%m %/ $ '

# Some aliases for convenience
alias ls='ls -lah'
alias python='python3.9'
alias pip='python3.9 -m pip'