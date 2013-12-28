# encoding: utf-8

import sublime, sublime_plugin

class TranslateExtendedCharsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print("Info: replacing all non-ASCII characters with their ASCII equivalents")
    dict = {
      u'“': '"',
      u'”': '"',
      u'’': '\''
    }
    regions = self.view.find_all('[^\x00-\x7F]')
    for region in regions:
      char = self.view.substr(region)
      if char in dict:
        self.view.replace(edit, region, dict[char])
      else:
        print('Warning: undefined translation for non-ASCII character "' + char.encode('utf-8') + '"')
