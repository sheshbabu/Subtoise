import subprocess
import os
import sublime, sublime_plugin

class Subtoise:
	def get_file_path(self):
		return os.path.abspath(self.view.file_name())

	def get_tortoiseproc_path(self):
		settings = sublime.load_settings('Subtoise.sublime-settings')
		tsvn_path = settings.get('svn_tortoiseproc_path')
		if os.path.isfile(tsvn_path):
			return tsvn_path
		else:
			sublime.message_dialog("Please set the path for TortoiseProc.exe")

	def run_command(self, tsvn_command):
		args = []
		tsvn_path = self.get_tortoiseproc_path()
		args.append(tsvn_path)
		file_path = "/path:" + self.get_file_path()
		args.append(file_path)
		args.append(tsvn_command)
		subprocess.Popen(args)

class SubtoiseDiffCommand(sublime_plugin.TextCommand, Subtoise):
	def run(self, edit):
		self.run_command("/command:diff")

class SubtoiseUpdateCommand(sublime_plugin.TextCommand, Subtoise):
	def run(self, edit):
		self.run_command("/command:update")

class SubtoiseCommitCommand(sublime_plugin.TextCommand, Subtoise):
	def run(self, edit):
		self.run_command("/command:commit")