import shutil
import subprocess

import sublime
import sublime_plugin

settings = None


def plugin_loaded():
    global settings
    settings = sublime.load_settings('Devhelp.sublime-settings')


def open_devhelp(query):
    cmd_setting = settings.get('devhelp_command', 'devhelp')
    cmd_path = shutil.which(cmd_setting)

    if not cmd_path:
        sublime.error_message("Could not find your devhelp executable. ({})"
                              '\n\nPlease edit Devhelp.sublime-settings'
                              .format(cmd_setting))
        return

    try:
        subprocess.Popen([cmd_path, '-s', query])
    except Exception as e:
        sublime.status_message("Devhelp: {}".format(e))
        raise


def get_word(view):
    for region in view.sel():
        if region.empty():
            region = view.word(region)

        return view.substr(region).strip()

    return ''


class DevhelpSearchCommand(sublime_plugin.TextCommand):
    def input(self, args):
        if not args.get('text'):
            return SimpleTextInputHandler('text', placeholder="query string", initial_text=get_word(self.view))

    def run(self, edit, text):
        open_devhelp(text)


class DevhelpSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = get_word(self.view)

        if not text:
            sublime.status_message("Devhelp: No word was selected.")
            return

        open_devhelp(text)


class SimpleTextInputHandler(sublime_plugin.TextInputHandler):
    def __init__(self, param_name, *, placeholder='', initial_text=''):
        self.param_name = param_name
        self._placeholder = placeholder
        self._initial_text = initial_text

    def name(self):
        return self.param_name

    def placeholder(self):
        return self._placeholder

    def initial_text(self):
        return self._initial_text
