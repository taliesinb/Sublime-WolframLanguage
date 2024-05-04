import sublime_plugin
import sublime, subprocess, os

def open_file(filepath):
    if sublime.platform() == "osx":
        subprocess.Popen(("open", filepath))
    elif sublime.platform() == "windows":
        os.startfile(filepath)
    elif sublime.platform() == "linux":
        subprocess.Popen(("xdg-open", filepath))

class SideBarEditorOpenCommand(sublime_plugin.WindowCommand):
    
    def run(self, paths = []):
        for path in paths:
            open_file(path)

    def is_enabled(self, paths = []):
        for path in paths:
            if not path.endswith((".nb", ".cdf", ".wl", ".m", ".wls")):
                return False

        return True
