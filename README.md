# Devhelp integration for Sublime Text

[Devhelp][] integration for Sublime Text. Initially based on [Zeal plugin][].

[Devhelp][] is a GNOME app for browsing and searching API documentation.

[Devhelp]: https://wiki.gnome.org/Apps/Devhelp
[Zeal plugin]: https://github.com/SublimeText/Zeal

## Usage

"Devhelp" item will be available in the context menu (searches for the word
clicked).

To enable keyboard shortcuts, select `Preferences` -> `Package Settings` ->
`Devhelp` -> `Key Bindings`. Default configuration contains key bindings for
<kbd>F1</kbd> and <kbd>Ctrl</kbd>+<kbd>F1</kbd>, but they are commented out.
You may copy them to your configuration and uncomment them.

## Installation

### From Package Control

The easiest way to install the package is to use
[Package Control](https://packagecontrol.io/).
Choose *Package Control: Install Package* in the Command Palette
(<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>)
and type "Devhelp".

https://packagecontrol.io/packages/Devhelp

### Using Git

Go to your Sublime Text `Packages` directory and clone the repository using the command below:

    $ git clone https://github.com/amezin/sublime-devhelp.git Devhelp

## Configuration

Select `Preferences: Devhelp Settings` form the command palette
to open the configuration files.

If your devhelp executable cannot be found by default,
change the `devhelp_command` setting.
