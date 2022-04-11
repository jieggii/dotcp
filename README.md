# dotcp
Copy selected dotfiles to directory

## What is it?
As said, **dotcp** copies _selected_ dotfiles to directory you indicated.
For example, `dotcp ~/awesome-dotifles/config/` will copy your selected dotfiles into `~/awesome-dotfiles/config/`.
How to _select_ dotfiles, you would ask? **dotcp** has it's own config. E.g:
```
i3
fish
alacritty
```
_(**dotcp**'s config file path should be `$XDG_CONFIG_HOME/dotcp/config`, but you can indicate it using `--config` option)_

Now **dotcp** will copy **i3**, **fish** and **alacritty** config directories into `~/awesome-dotfiles/config/` if you would run the previous command.

## Why?
Just wanted to have something similar to [this script](https://github.com/jieggii/dotfiles/blob/ed77dc9c0a5056cd00d9e647e6d55a1498783434/update.bash) but customizable and extensible.

## Installation
**dotcp** can be easily installed via **pip** (as any other shitty python program):

`pip install --user dotcp`

## Usage
At first just run **dotcp** without any flags, indicating destination directory that does not yet exist (e.g. `destination-dir`):

`dotcp destination-dir/`

Then you will have to use one of these flags: `--overwrite` or `--append` to update content of destination directory.
* `--overwrite` does the same thing as `rm -r destination-dir && dotcp destination-dir`
* `--append` appends your selected dotfiles into `destination-dir` saving its content

Examples:
* `dotcp --overwrite destination-dir/`
* `dotcp --append destination-dir/`
