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
                              "\n\nPlease edit Devhelp.sublime-settings"
                              .format(cmd_setting))
        return

    try:
        subprocess.Popen([cmd_path, '-s', query])
    except Exception as e:
        sublime.status_message("Devhelp: {}".format(e))
        raise


class DevhelpSearchCommand(sublime_plugin.TextCommand):
    def get_region(self, event=None):
        if event is None:
            return next(iter(self.view.sel()), None)

        point = self.view.window_to_text((event['x'], event['y']))
        return sublime.Region(point, point)

    def get_word(self, event=None):
        region = self.get_region(event)

        if region is None:
            return ''

        if region.empty():
            region = self.view.word(region)

        return self.view.substr(region).strip()

    def is_enabled(self, event=None):
        selectors = settings.get('devhelp_selectors')
        if not selectors:
            return True

        region = self.get_region(event)
        if region is None:
            return False

        for selector in selectors:
            if self.view.match_selector(region.a, selector):
                return True

        return False

    def is_visible(self, event=None):
        return self.is_enabled(event)

    def want_event(self):
        return True

    def input(self, args):
        if args.get('text'):
            return None

        return SearchTextInputHandler(self.get_word(args.get('event')))

    def run(self, edit, text, event=None):
        open_devhelp(text)


class DevhelpSearchSelectedCommand(DevhelpSearchCommand):
    def input(self, args):
        return None

    def run(self, edit, event=None):
        text = self.get_word(event)

        if not text:
            sublime.status_message("Devhelp: no word selected")
            return

        super().run(edit, text, event)


class SearchTextInputHandler(sublime_plugin.TextInputHandler):
    def __init__(self, initial_text):
        self._initial_text = initial_text

    def name(self):
        return 'text'

    def initial_text(self):
        return self._initial_text

    def validate(self, text):
        return text != ''
