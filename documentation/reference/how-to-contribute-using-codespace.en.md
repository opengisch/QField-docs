---
title: QField Documentation Contribution
tx_slug: documentation_get-started_how-to-contribute-using-codespaces
---

# Contributing to the Documentation Using GitHub Codespaces

You can contribute to the QField documentation by making improvements, correcting spelling and grammar, or adding new information.
This guide provides a workflow that doesn't require installing anything on your local machine.
All you need is a web browser and a free GitHub account.

We will use GitHub Codespaces, an online development environment that automatically sets up all the necessary tools for you.

## Step-by-Step Guide

### 1. Create a New Branch

First, you need to create a personal branch where you will make your changes.
A branch isolates your work from the main codebase until it's ready to be merged to the master branch.

1. Navigate to the official [QField Docs repository](https://github.com/opengisch/QField-docs).

2. Click on the branch dropdown, which likely shows `master`.

3. In the text box, type a descriptive name for your new branch.
Branch names should not contain spaces; use underscores (`_`) or hyphens (`-`) instead. For example: `fix_welcome_page_typos`.

4. Click on **"Create branch: `<your_branch_name>` from `master`"**.
GitHub will automatically create the branch and switch to it.

!![](../assets/images/codespaces_steps_001.png,850px)

### 2. Launch the Codespace

Now, launch the cloud-based editor for your new branch.

1. Click the green **`Code`** button.

2. Select the **"Codespaces"** tab.

3. Click the **"Create codespace on `<your_branch_name>`"** button.

!![](../assets/images/codespaces_steps_002.png,850px)

GitHub will now prepare your Codespace.
This may take a few minutes as it installs all the required dependencies in the background.

### 3. (Optional) Set Up the 'Doc Writer' Profile

To enhance your writing experience, you can activate a pre-configured profile that installs helpful extensions for writing documentation.

1. Once the Codespace has loaded, click the **Gear icon** (`⚙️`) in the bottom-left corner.

2. Select **Profiles > New Profile**.

!![](../assets/images/codespaces_steps_003.png,850px)

3. In the "Copy from..." dropdown, select **"Doc Writer"** and click **Create**.

!![](../assets/images/codespaces_steps_004.png,850px)

4. If a pop-up appears asking for trust, click **"Trust Publisher and Install"**.

!![](../assets/images/codespaces_steps_005.png,850px)

### 4. Find and Edit Files

You are now ready to make your changes.

- The documentation source files are located in the `documentation/` directory in the file explorer panel on the left.

- You will primarily edit the Markdown (`.md`) files within the `get-started/`, `how-to/`, and `reference/` subdirectories.

- Place any new or edited images or videos in the `documentation/assets/images/` or `documentation/assets/videos/` folders, respectively,
by drag and drop the files directly on the directory file explorer panel.

To see a live preview of your changes, right-click the file tab of the document you are editing and select **"Open Preview"** (or use the shortcut `Ctrl+Shift+V`).
You can drag this preview tab to the side to see your edits update in real-time.

!![](../assets/images/codespaces_steps_006.png,850px)

!![](../assets/images/codespaces_steps_007.png,850px)

Please ensure your contributions adhere to the writing style and formatting conventions of [MkDocs](https://www.mkdocs.org/user-guide/writing-your-docs/) and [MkDocs Material](https://squidfunk.github.io/mkdocs-material/reference/).

### 5. Run a Local Preview Server

To see how your changes will look on the final documentation website, you can run a local server within your Codespace.

1. Open a new terminal by going to the top menu and selecting **Terminal > New Terminal**.

2. Run the following commands:

    ```bash
    export BUILD_ONLY_LOCALE="en"
    python3 -m mkdocs serve
    ```

!![](../assets/images/codespaces_steps_008.png,850px)

3. A notification will appear in the bottom-right corner.
Click **"Open in Browser"** to view the live documentation site.
The page will automatically reload whenever you save a file.

!![](../assets/images/codespaces_steps_009.png,850px)

!![](../assets/images/codespaces_steps_010.png,850px)

### 6. Save Your Work (Commit and Push)

Once you are satisfied with your changes, you need to save them to Git and push them to GitHub.

A. Stage Your Changes

Stage all modified files, preparing them for a commit.
You can do this using the integrated terminal:

```bash
git add .
```

Alternatively, go to the **"Source Control"** tab (the icon with three connected dots)
(or by using the Shortcut `CTRL+Shift+G`) on the left sidebar and click the `+` icon next to each file or next to the "Changes" heading.

!![](../assets/images/codespaces_steps_011.png,850px)

B. Run Pre-Commit Checks

We use a tool called pre-commit to automatically check your files for formatting errors, broken links, and other common issues.
This helps maintain code quality and avoids errors.

Run it from the terminal:

```bash
pre-commit run
```

If the tool reports any errors, it may fix them automatically.
In that case, you will need to **stage the changes again** (`git add .`).
If it reports errors it cannot fix, please correct them manually and then run the command again until all checks show as **"Passed"** in green.

!![](../assets/images/codespaces_steps_012.png,850px)

- Is pre-commit not installed?

The Codespace environment should install pre-commit automatically.
If you see a "Bash command not found" error, you can install it manually by running:

```bash
python3 -m pip install pre-commit
```

C. Commit Your Changes

A commit is a snapshot of your staged changes.
Each commit has a message describing the work you did.

In the terminal, run:

```bash
git commit -m "Your descriptive message here"
```

Example: git commit -m "Fix typos on the Welcome Page"

Alternatively, use the Source Control tab: type your message in the text box at the top and click the "Commit" button.

!![](../assets/images/codespaces_steps_013.png,850px)

D. Push Changes to GitHub

Push your commit from the Codespace to your branch on GitHub.

In the terminal, run:

```bash
git push
```

Or, in the Source Control tab, click the **"Sync Changes"** button.

!![](../assets/images/codespaces_steps_014.png,850px)

### 7. Create a Pull Request

The final step is to create a Pull Request (PR), which is a formal request to merge your changes into the main `master` branch.

1. Go back to the [QField Docs repository page](https://github.com/opengisch/QField-docs) on GitHub.

2. You should see a yellow banner with your branch name.
Click the **"Compare & pull request"** button.

3. Give your Pull Request a descriptive title and write a brief summary of the changes you made in the description box.

4. Click **"Create pull request"**.

!![](../assets/images/codespaces_steps_015.png,850px)

!![](../assets/images/codespaces_steps_016.png,850px)

### 8. Address Review Feedback

A maintainer will review your contribution.
If they request changes, you can easily make updates:

1. Re-open your Codespace for that branch (you can find it in the "Codespaces" tab of the repository).

2. Make the requested edits.

3. Follow [**Step 6**](#6-save-your-work-commit-and-push) again to stage, run pre-commit, commit, and push your new changes.
The Pull Request will update automatically.

Thank you for contributing to the QField documentation!
