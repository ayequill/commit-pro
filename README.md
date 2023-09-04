# CommitPro - Git Command Line Interface

**CommitPro** is a simple command-line interface (CLI) tool for managing Git repositories more efficiently. With CommitPro, you can perform common Git operations without leaving your terminal. This README provides an overview of the features, installation, and usage instructions for CommitPro.

## Features

- **Git Commands**: CommitPro supports essential Git commands, including:
  - `add`: Add files to Git and commit them.
  - `push`: Push changes to a Git remote repository.
  - `pull`: Pull the latest changes from the remote repository.
  - `status`: Check the Git repository's status.
  - `git`: Execute any Git command directly from the CLI.
  - Plus, additional commands for branch management, history viewing, and more.

- **Tab Completion**: CommitPro provides tab completion for Git commands and file suggestions for the `add` command, making it easier and faster to use.

- **Custom Commands**: Extend CommitPro by adding your own custom commands to simplify your Git workflow.

## Installation

To use CommitPro, you need to have Git installed on your system.

1. Clone or download this repository to your local machine:

   ```bash
   git clone https://github.com/ayequill/commitpro.git
   ```

2. Navigate to the project directory:

   ```bash
   cd commitpro
   ```

3. Run the CLI:

   ```bash
   python commitpro.py
   ```

## Usage

### Basic Commands

- `add`: Add files to Git and commit them. You'll be prompted to enter a commit message.

   ```bash
   > add file.txt
   ```

- `push`: Push changes to a Git remote repository.

   ```bash
   > push
   ```

- `pull`: Pull the latest changes from the remote repository.

   ```bash
   > pull
   ```

- `status`: Check the Git repository's status.

   ```bash
   > status
   ```

### Branch Management

- `create_branch`: Create a new Git branch.

   ```bash
   > create_branch new_feature
   ```

- `delete_branch`: Delete an existing Git branch.

   ```bash
   > delete_branch old_feature
   ```

- `list_branches`: List all Git branches.

   ```bash
   > list_branches
   ```

- `switch_branch`: Switch to a different Git branch.

   ```bash
   > switch_branch feature_branch
   ```

### History Viewing

- `log`: View the commit history.

   ```bash
   > log
   ```

## Contributing

Contributions to CommitPro are welcome! If you have ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thank you to the [Git](https://git-scm.com/) community for providing a powerful version control system.
- Inspired by the need for a more efficient Git workflow.

## Contact

If you have any questions, suggestions, or feedback, feel free to contact the project maintainer at <siawnic.dev@gmail.com>.
