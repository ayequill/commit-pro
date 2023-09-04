#!/usr/bin/env python
import subprocess
import cmd
import shlex
import os


class CommitPro(cmd.Cmd):
    """ Represents the git tool class. """
    intro = "Welcome to the Commit Pro CLI. Type 'help' for a list of commands."
    prompt = "> "

    def __init__(self):
        super().__init__()
        self.file_suggestions = []

    def complete_ga(self, text, line, begidx, endidx):
        """
        Tab completion for 'ga' command (Git add).
        """
        if not text:
            return self.file_suggestions
        return [file for file in self.file_suggestions if file.startswith(text)]

    def do_git(self, line):
        """
        Execute Git commands. Usage: git [command]
        """
        try:
            args = shlex.split(line)
            subprocess.check_call(['git'] + args)
        except subprocess.CalledProcessError as e:
            print(f"Git command failed: {e}")
        except FileNotFoundError:
            print("Git is not installed or not in the system's PATH.")

    def do_add(self, line):
        """
        Add files to Git and prompt for a commit message. Usage: ga [files]
        """
        try:
            args = shlex.split(line)
            if not args:
                print("Please provide the file(s) to add.")
                self.help_add()
                return
            subprocess.check_call(['git', 'add'] + args)
            print("Files added to Git successfully.")

            # Prompt for a commit message
            commit_message = input("Enter a commit message: ")
            if not commit_message:
                print("No commit message provided. Skipping commit.")
            elif len(commit_message.split()) < 2:
                print("Commit message not descriptive enough. Skipping commit.")
            else:
                subprocess.check_call(['git', 'commit', '-m', commit_message])
                print("Changes committed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to add files to Git: {e}")

    def do_push(self, line):
        """
        Push changes to Git remote repository. Usage: gp
        """
        try:
            subprocess.check_call(['git', 'push'])
            print("Changes pushed to Git successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to push changes to Git: {e}")

    def do_pull(self, _):
        """ Pulls latest changes from origin """
        try:
            res = subprocess.run(['git', 'pull'], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True)
            print(res.stdout)
        except subprocess.CalledProcessError as e:
            print(f"{e}")

    def do_remote(self, _):
        """ Checks remote sources """
        try:
            res = subprocess.run(['git', 'remote', '-v'], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True)
            print(res.stdout)
        except subprocess.CalledProcessError as e:
            print(f"No remote found: {e}")

    def do_status(self, line):
        """
        Check Git status. Usage: gs
        """
        try:
            result = subprocess.run(['git', 'status', '-s'], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Failed to check Git status: {e}")

    def do_create_branch(self, branch_name):
        """
        Create a new branch. Usage: create_branch <branch_name>
        """
        try:
            subprocess.check_call(['git', 'branch', branch_name])
            print(f"Created branch '{branch_name}' successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create branch: {e}")

    def do_delete_branch(self, branch_name):
        """
        Delete a branch. Usage: delete_branch <branch_name>
        """
        try:
            subprocess.check_call(['git', 'branch', '-d', branch_name])
            print(f"Deleted branch '{branch_name}' successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to delete branch: {e}")

    def do_list_branches(self, _):
        """
        List all branches. Usage: list_branches
        """
        try:
            result = subprocess.run(['git', 'branch'], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True)
            branches = result.stdout.strip().split('\n')
            for branch in branches:
                print(branch)
        except subprocess.CalledProcessError as e:
            print(f"Failed to list branches: {e}")

    def do_switch_branch(self, branch_name):
        """
        Switch to a different branch. Usage: switch_branch <branch_name>
        """
        try:
            subprocess.check_call(['git', 'checkout', branch_name])
            print(f"Switched to branch '{branch_name}' successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to switch to branch: {e}")

    def do_log(self, _):
        """
        View the commit history. Usage: history
        """
        try:
            result = subprocess.run(['git', 'log'], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True)
            commit_history = result.stdout
            print(commit_history)
        except subprocess.CalledProcessError as e:
            print(f"Failed to view commit history: {e}")

    def do_EOF(self, line):
        """
        Exit the console gracefully. Usage: EOF (Ctrl+D)
        """
        print("Exiting Commit Pro Console.")
        return True

    def do_quit(self, _):
        """ Exits the console """
        return True

    def emptyline(self):
        pass

    # Help Documentation

    def help_quit(self):
        """ Quit Command Help """
        print("Quit command to exit the program\n")

    def help_add(self):
        """ Help for ga command """
        print("Adds files to git")
        print("[Usage]: add <file>\n")

    def help_remote(self):
        """ Help for remote command """
        print("Checks for remote sources")
        print("[Usage]: remote ")

    def help_push(self):
        """ Help for push command """
        print("Pushes files to git")
        print("[Usage]: push")

    def help_pull(self):
        """ Help for pull command """
        print("Pulls files from git")
        print("[Usage]: pull")


if __name__ == "__main__":
    console = CommitPro()
    console.file_suggestions = os.listdir()
    console.cmdloop()
