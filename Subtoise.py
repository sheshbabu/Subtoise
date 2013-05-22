import subprocess
import os
import sublime, sublime_plugin

class Subtoise:
	def get_path(self):
		return os.path.abspath(self.view.file_name())

	def run_command(self, tsvn_command):
		args = ["TortoiseProc.exe"]
		path = "/path:" + self.get_path()
		args.append(path)
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