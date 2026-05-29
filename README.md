# LSP-twiggy

Twig support for Sublime’s LSP.

Provided through [twiggy-language-server](https://github.com/moetelo/twiggy/tree/master/packages/language-server).

### Installation

* Install [LSP](https://packagecontrol.io/packages/LSP), [Twig Syntax](https://packagecontrol.io/packages/Twig) and [LSP-twiggy](https://packagecontrol.io/packages/LSP-twiggy) via Package Control.
* (Optional but recommended) Install the [LSP-file-watcher-rust](https://packagecontrol.io/packages/LSP-file-watcher-rust) (or if it doesn't work for some reason then [LSP-file-watcher-chokidar](https://packagecontrol.io/packages/LSP-file-watcher-chokidar)) via Package Control to enable functionality to notify the server about new or changed files.
* Restart Sublime.

### Configuration

There are some ways to configure the package and the language server.

- From `Preferences > Package Settings > LSP > Servers > LSP-twiggy`
- From the command palette `Preferences: LSP-twiggy Settings`
