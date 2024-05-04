import sublime_plugin
import sublime, subprocess, os

def open_file(filepath):
    if sublime.platform() == "osx":
        subprocess.Popen(("open", filepath))
    elif sublime.platform() == "windows":
        os.startfile(filepath)
    elif sublime.platform() == "linux":
        subprocess.Popen(("xdg-open", filepath))

class ContextEditorOpenCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):
        name = self.view.file_name()
        open_file(name)

    def is_enabled(self):
        name = self.view.file_name()
        if name == None:
            return False
        if name.endswith((".nb", ".cdf", ".wl", ".m", ".wls")):
            return True
        return False
