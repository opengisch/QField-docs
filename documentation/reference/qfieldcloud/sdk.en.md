---
title: The official QFieldCloud SDK and CLI
tx_slug: documentation_reference_qfieldcloud_sdk
---

`qfieldcloud-sdk` is the official client to connect to [QFieldCloud API](api.md) either as a python module, or directly from the command line.

!!! note
    `qfieldcloud-sdk` requires Python >=3.6

## Install

`pip install qfieldcloud-sdk`

## Module usage

```python
import requests
from qfieldcloud_sdk import sdk

client = sdk.Client(
    url="https://app.qfield.cloud/api/v1/",
    username="user1",
    password="pass1",
)

try:
    projects = client.list_projects()
except requests.exceptions.RequestException:
    print("Oops!")
```

## CLI usage

The official QFieldCloud CLI tool.

### Usage

```bash
qfieldcloud-cli [OPTIONS] COMMAND [ARGS]...
```

### Examples

```bash
# logs in user "user" with password "pass"
qfieldcloud-cli login user pass

# gets the projects of user "user" with password "pass" at "https://localhost/api/v1/"
qfieldcloud-cli -u user -p pass -U https://localhost/api/v1/ list-projects

# gets the projects of user authenticated with token `QFIELDCLOUD_TOKEN` at "https://localhost/api/v1/" as JSON
export QFIELDCLOUD_URL=https://localhost/api/v1/
export QFIELDCLOUD_TOKEN=017478ee2464440cb8d3e98080df5e5a
qfieldcloud-cli --json list-projects
```

### Filters

Some commands allow you to define a filter on the results based on the filename with the `--filter` option (e.g. the `download-files`
command).

The filters support Unix shell-style wildcards. The special characters used in shell-style wildcards are:


| Pattern | Meaning                          |
|---------|----------------------------------|
| *       | matches everything               |
| ?       | matches any single character     |
| [seq]   | matches any character in seq     |
| [!seq]  | matches any character not in seq |

For a literal match, wrap the meta-characters in brackets. For example, `'[?]'` matches the character `'?'`.
#### Examples

- `qfieldcloud-cli --filter 'DCIM/*.jpg'`
- `qfieldcloud-cli --filter 'attachments/documentation-??.pdf'`

### Global options overview

```bash
-U, --url TEXT                  URL to the QFieldCloud API endpoint. If not
                                passed, gets the value from QFIELDCLOUD_URL
                                environment variable. Default:
                                https://app.qfield.cloud/api/v1/
-u, --username TEXT             Username or email.
-p, --password TEXT
-t, --token TEXT                Session token.
--json / --human                Output the result as newline formatted json. Default: False
--verify-ssl / --no-verify-ssl  Verify SSL. Default: True
--help                          Show this message and exit.
```

Environment variables can be used instead of passing some common global options.

- `QFIELDCLOUD_API` - QFieldCloud API endpoint URL
- `QFIELDCLOUD_USERNAME` - QFieldCloud username or email. Requires `QFIELDCLOUD_PASSWORD` to be set.
- `QFIELDCLOUD_PASSWORD` - Password. Requires `QFIELDCLOUD_USERNAME` to be set.
- `QFIELDCLOUD_TOKEN` - Token that can be used instead of passing username and password. It can be obtained by running `qfieldcloud-cli login`.
- `QFIELDCLOUD_VERIFY_SSL` - When set to `0` has the same effect as passing `--no-verify-ssl`.

### Commands overview

```bash
  login             Login to QFieldCloud.
  logout            Logout and expire the token.
  list-projects     List QFieldCloud projects.
  list-files        List QFieldCloud project files.
  create-project    Creates a new empty QFieldCloud project.
  delete-project    Deletes a QFieldCloud project.
  upload-files      Upload files to a QFieldCloud project.
  download-files    Download QFieldCloud project files.
  delete-files      Delete QFieldCloud project files.
  list-jobs         List project jobs.
  job-trigger       Triggers a new job.
  job-status        Get job status.
  package-latest    Check project packaging status.
  package-download  Download packaged QFieldCloud project files.
```

#### login

Login to QFieldCloud.

```bash
qfieldcloud-cli login [OPTIONS] USERNAME PASSWORD
```

#### logout

Logout from QFieldCloud.

```bash
qfieldcloud-cli logout
```

#### list-projects

List QFieldCloud projects.

```bash
qfieldcloud-cli list-projects [OPTIONS]

Options:
  --include-public / --no-public  Includes the public project in the list. Default: False
```

#### list-files

List QFieldCloud project files.

```bash
qfieldcloud-cli list-files [OPTIONS] PROJECT_ID
```

#### create-project

Creates a new empty QFieldCloud project.

```bash
qfieldcloud-cli create-project [OPTIONS] NAME

Options:
  --owner TEXT                Owner of the project. If omitted, the current
                              user is the owner.
  --description TEXT          Description of the project.
  --is-public / --is-private  Mark the project as public.
```

#### delete-project

Deletes a QFieldCloud project.

```bash
qfieldcloud-cli delete-project [OPTIONS] PROJECT_ID
```

#### upload-files

Upload files to a QFieldCloud project.

```bash
qfieldcloud-cli upload-files [OPTIONS] PROJECT_ID PROJECT_PATH

Options:
  --filter TEXT                   Do not upload the whole project, but only
                                  the files which match the glob.
  --throw-on-error / --no-throw-on-error
                                  If any project file upload fails stop
                                  uploading the rest. Default: False
```

#### download-files

Download QFieldCloud project files.

```bash
qfieldcloud-cli download-files [OPTIONS] PROJECT_ID LOCAL_DIR

Options:
  --filter TEXT                   Do not download the whole project, but only
                                  the files which match the glob.
  --throw-on-error / --no-throw-on-error
                                  If any project file downloads fails stop
                                  downloading the rest. Default: False
  --force-download/--no-force-download
  ￼                               Download file even if it already exists locally.
                                  Default: False
```

#### delete-files

Delete QFieldCloud project files.

```bash
qfieldcloud-cli delete-files [OPTIONS] PROJECT_ID PATHS...

Options:
  --throw-on-error / --no-throw-on-error
                                  If any project file delete operations fails
                                  stop, stop deleting the rest. Default: False
```

#### job-list

List project jobs.

```bash
qfieldcloud-cli list-jobs [OPTIONS] PROJECT_ID

Options:
  --type JOBTYPES  Job type. One of package, delta_apply or
                   process_projectfile.
```

#### job-trigger

Triggers a new job.

```bash
qfieldcloud-cli job-trigger [OPTIONS] PROJECT_ID JOB_TYPE

Options:
  --force / --no-force  Should force creating a new job. Default: False
```

#### job-status

Get job status.

```bash
qfieldcloud-cli job-status [OPTIONS] JOB_ID
```

#### package-latest

Check project packaging status.

```bash
qfieldcloud-cli package-latest [OPTIONS] PROJECT_ID
```

#### package-download

Download packaged QFieldCloud project files.

```bash
qfieldcloud-cli package-download [OPTIONS] PROJECT_ID LOCAL_DIR

Options:
  --filter TEXT                   Do not download the whole packaged project,
                                  but only the files which match the glob.
  --throw-on-error / --no-throw-on-error
                                  If any packaged file downloads fails stop
                                  downloading the rest. Default: False
  --force-download/--no-force-download
  ￼                               Download file even if it already exists locally.
                                  Default: False
```
