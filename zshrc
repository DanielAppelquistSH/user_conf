# The following lines were added by compinstall

zstyle ':completion:*' completer _expand _complete _ignored _approximate
zstyle ':completion:*' ignore-parents parent
zstyle ':completion:*' matcher-list '' ''
zstyle :compinstall filename '$HOME/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
setopt inc_append_history
setopt share_history

HISTFILE=$HOME/.zhistory
HISTSIZE=3000
SAVEHIST=2000

setopt EXTENDED_HISTORY
setopt HIST_EXPIRE_DUPS_FIRST
setopt HIST_IGNORE_DUPS
setopt HIST_SAVE_NO_DUPS

export BROWSER="firefox -new-tab"

# Set up help (general)
unalias  run-help  &> /dev/null
autoload run-help

# Set up help specifically for git
unalias  run-help-git &> /dev/null
autoload run-help-git

# Execute local file if it exists
[ -f $HOME/.zshrc_local ] && . $HOME/.zshrc_local
