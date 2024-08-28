---
title: The official QFieldCloud SDK and CLI
tx_slug: documentation_reference_qfieldcloud_sdk
---

`qfieldcloud-sdk` is the official client to connect to [QFieldCloud API](api.md) either as a python module, or directly from the command line.

!!! note
    `qfieldcloud-sdk` requires Python >=3.6

## Install

`pip install qfieldcloud-sdk`

## QFieldCloud SDK Module

The QFieldCloud SDK provides a set of classes and utilities to interact with the QFieldCloud platform. This SDK enables developers to manage file transfers, handle project collaborations, and organize members within the platform, all while maintaining compatibility with Python.

DEFAULT_PAGINATION_LIMIT: Defines the default limit for pagination, set to `20`.

```python
DEFAULT_PAGINATION_LIMIT = 20
```

FileTransferStatus: Represents the status of a file transfer.

- `PENDING`: The transfer is pending.
- `SUCCESS`: The transfer was successful.
- `FAILED`: The transfer failed.

```python
class FileTransferStatus(str, Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
```

FileTransferType: Represents the type of file transfer.

- `PROJECT`: Refers to a project file.
- `PACKAGE`: Refers to a package Type.

```python
class FileTransferType(Enum):
    PROJECT = "project"
    PACKAGE = "package"
```

JobTypes: Represents the types of jobs that can be processed on QFieldCloud.

- `PACKAGE`: Refers to a packaging job.
- `APPLY_DELTAS`: Refers to applying deltas (differences).
- `PROCESS_PROJECTFILE`: Refers to processing a project file.

```python
class JobTypes(str, Enum):
    PACKAGE = "package"
    APPLY_DELTAS = "delta_apply"
    PROCESS_PROJECTFILE = "process_projectfile"
```

ProjectCollaboratorRole: Defines roles for project collaborators.

- `ADMIN`: Administrator role.
- `MANAGER`: Manager role.
- `EDITOR`: Editor role.
- `REPORTER`: Reporter role.
- `READER`: Reader role.

```python
class ProjectCollaboratorRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    EDITOR = "editor"
    REPORTER = "reporter"
    READER = "reader"
```

OrganizationMemberRole: Defines roles for organization members.

- `ADMIN`: Administrator role.
- `MEMBER`: Member role.

```python
class OrganizationMemberRole(str, Enum):
    ADMIN = "admin"
    MEMBER = "member"
```

### Models QFieldCloud

CollaboratorModel: Represents the structure of a project collaborator in the QFieldCloud system.

- `collaborator`: The collaborator's identifier.
- `role`: The role of the collaborator, represented by `ProjectCollaboratorRole`.
- `project_id`: The associated project identifier.
- `created_by`: The user who created the collaborator entry.
- `updated_by`: The user who last updated the collaborator entry.
- `created_at`: The timestamp when the collaborator entry was created.
- `updated_at`: The timestamp when the collaborator entry was last updated.

```python
class CollaboratorModel(TypedDict):
    collaborator: str
    role: ProjectCollaboratorRole
    project_id: str
    created_by: str
    updated_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
```

OrganizationMemberModel: Represents the structure of an organization member in the QFieldCloud system.

- `member`: The member's identifier.
- `role`: The role of the member, represented by `OrganizationMemberRole`.
- `organization`: The associated organization identifier.
- `is_public`: A boolean indicating if the membership is public.

```python
class OrganizationMemberModel(TypedDict):
    member: str
    role: OrganizationMemberRole
    organization: str
    is_public: bool
```

### Pagination

The `Pagination` class allows for controlling and managing pagination of results within the QFieldCloud SDK.

Attributes

- `limit`: The maximum number of items to return.
- `offset`: The starting point from which to return items.

Methods

- `__init__(self, limit: Optional[int] = None, offset: Optional[int] = None)`: Initializes the pagination settings.
- `is_empty`: A property that returns `True` if both `limit` and `offset` are `None`, indicating no pagination settings.

```python
class Pagination:
    limit = None
    offset = None

    def __init__(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> None:
        self.limit = limit
        self.offset = offset

    @property
    def is_empty(self):
        return self.limit is None and self.offset is None
```

### Client Class

The `Client` class is the core component of the QFieldCloud SDK. It provides methods for authenticating users, managing sessions, and interacting with various endpoints of the QFieldCloud platform, such as projects, files, members and collaborators.

#### Initialization

The `Client` class is initialized with optional parameters for the base URL, SSL verification, and an authentication token. If these are not provided, the class will attempt to retrieve them from environment variables.

:material-arrow-right-circle: `__init__(self, url: str = None, verify_ssl: bool = None, token: str = None) -> None`

Initializes a new `Client` instance. If the `verify_ssl` is set to `False`, SSL warnings will be disabled. The session is configured with retries for GET requests on specific 5xx HTTP status codes.

Parameters:

- `url` (str, optional): The base URL for the QFieldCloud API. Defaults to `QFIELDCLOUD_URL` environment variable if not provided.
- `verify_ssl` (bool, optional): Whether to verify SSL certificates. Defaults to `True` if not specified.
- `token` (str, optional): The authentication token for API access. Defaults to `QFIELDCLOUD_TOKEN` environment variable if not provided.

Raises

- `QfcException`: If the `url` is not provided either directly or through the environment variable.

```python
class Client:
    def __init__(
        self, url: str = None, verify_ssl: bool = None, token: str = None
    ) -> None:
        # Implementation details...
```

#### Authentication Methods

:material-arrow-right-circle: `login(self, username: str, password: str) -> Dict`

  Logs in with the provided username and password, and retrieves an authentication token.

Parameters:

- `username` (str): The username or email used to register.
- `password` (str): The password associated with the username.

Returns:

- A dictionary containing the authentication token and additional metadata.

Example:

```python
client = Client()
login_response = client.login("ninjamaster", "secret_password123")
```

:material-arrow-right-circle: `logout(self) -> None`

Logs out from the current session, invalidating the authentication token.

Returns: None.

Example:

```python
client.logout()
```

#### Project Management Methods

:material-arrow-right-circle: `create_project(self, name: str, owner: str = None, description: str = "", is_public: bool = False) -> Dict`

Creates a new project on QFieldCloud.

Parameters:

- `name` (str): The name of the project.
- `owner` (str, optional): The owner of the project. If not provided, defaults to the current user.
- `description` (str, optional): A description of the project. Defaults to an empty string.
- `is_public` (bool, optional): Whether the project should be public. Defaults to `False`.

Returns: A dictionary containing details of the newly created project.

Example:

```python
new_project = client.create_project(name="my_project", is_public=False)
```

:material-arrow-right-circle: `delete_project(self, project_id: str)`

Deletes an existing project from QFieldCloud.

Parameters:

- `project_id` (str): The ID of the project to be deleted.

Returns: The response object from the delete request.

Example:

```python
response = client.delete_project("project_id")
```

#### File Management Methods

:material-arrow-right-circle: `upload_files(self, project_id: str, upload_type: FileTransferType, project_path: str, filter_glob: str, throw_on_error: bool = False, show_progress: bool = False, force: bool = False, job_id: str = "") -> List[Dict]`

Uploads multiple files to a QFieldCloud project.

Parameters:

- `project_id` (str): The ID of the project to which files are uploaded.
- `upload_type` (FileTransferType): The type of file transfer (e.g., `PROJECT` or `PACKAGE`).
- `project_path` (str): The local path to the project files.
- `filter_glob` (str): A glob pattern to filter which files to upload.
- `throw_on_error` (bool, optional): Whether to raise an error if a file upload fails. Defaults to `False`.
- `show_progress` (bool, optional): Whether to show a progress bar for the upload. Defaults to `False`.
- `force` (bool, optional): Whether to force the upload of all files. Defaults to `False`.
- `job_id` (str, optional): The job ID for package uploads. Required if `upload_type` is `PACKAGE`.

Returns:

- A list of dictionaries, each representing a file that was uploaded.

Example:

```python
uploaded_files = client.upload_files("project_id", FileTransferType.PROJECT, "/path/to/files", "*.qgz")
```

:material-arrow-right-circle: `upload_file(self, project_id: str, upload_type: FileTransferType, local_filename: Path, remote_filename: Path, show_progress: bool, job_id: str = "") -> requests.Response`

Uploads a single file to a QFieldCloud project.

Parameters:

- `project_id` (str): The ID of the project.
- `upload_type` (FileTransferType): The type of file transfer (e.g., `PROJECT` or `PACKAGE`).
- `local_filename` (Path): The local file path to be uploaded.
- `remote_filename` (Path): The destination file name in QFieldCloud.
- `show_progress` (bool): Whether to show a progress bar for the upload.
- `job_id` (str, optional): The job ID for package uploads. Required if `upload_type` is `PACKAGE`.

Returns:

- The response object from the upload request.

Example:

```python
response = client.upload_file("project_id", FileTransferType.PROJECT, Path("local/file.qgz"), Path("remote/file.qgz"), show_progress=True)
```

:material-arrow-right-circle: `download_project(self, project_id: str, local_dir: str, filter_glob: str = None, throw_on_error: bool = False, show_progress: bool = False, force_download: bool = False) -> List[Dict]`

Downloads all or selected files of a project into a specified local directory.

Parameters:

- `project_id` (str): The ID of the project to be downloaded.
- `local_dir` (str): The local directory where the files will be downloaded.
- `filter_glob` (str, optional): A glob pattern to filter which files to download. If not provided, all files are downloaded.
- `throw_on_error` (bool, optional): Whether to raise an error if a file download fails. Defaults to `False`.
- `show_progress` (bool, optional): Whether to show a progress bar for the download. Defaults to `False`.
- `force_download` (bool, optional): Whether to download the file even if it already exists locally. Defaults to `False`.

Returns:

- A list of dictionaries, each representing a file that was downloaded.

Example:

```python
downloaded_files = client.download_project("project_id", "/local/dir")
```

#### Job Management Methods

:material-arrow-right-circle: `list_jobs(self, project_id: str, job_type: JobTypes = None, pagination: Pagination = Pagination()) -> List[Dict[str, Any]]`

Lists all jobs associated with a specific project.

Parameters:

- `project_id` (str): The ID of the project whose jobs are to be listed.
- `job_type` (JobTypes, optional): The type of job to filter by (e.g., `PACKAGE`, `APPLY_DELTAS`). Defaults to `None`.
- `pagination` (Pagination, optional): Pagination settings for the request. Defaults to no pagination.

Returns:

- A list of dictionaries, each representing a job.

Example:

```python
jobs = client.list_jobs("project_id", JobTypes.PACKAGE)
```

:material-arrow-right-circle: `job_trigger(self, project_id: str, job_type: JobTypes, force: bool = False) -> Dict[str, Any]`

Triggers a new job for a specific project.

Parameters:

- `project_id` (str): The ID of the project for which the job is triggered.
- `job_type` (JobTypes): The type of job to trigger.
- `force` (bool, optional): Whether to force the job initiation. Defaults to `False`.

Returns:

- A dictionary containing details of the triggered job.

Example:

```python
job = client.job_trigger("project_id", JobTypes.PACKAGE)
```

:material-arrow-right-circle: `job_status(self, job_id: str) -> Dict[str, Any]`

Retrieves the status of a specific job.

Parameters:

- `job_id` (str): The ID of the job whose status is to be retrieved.

Returns:

- A dictionary containing the job status and related information.

Example:

```python
status = client.job_status("job_id")
```

:material-arrow-right-circle: `delete_files(self, project_id: str, glob_patterns: List[str], throw_on_error: bool = False, finished_cb: Callable = None) -> Dict[str, Dict[str, Any]]`

Deletes files from a project based on glob patterns.

Parameters:

- `project_id` (str): The ID of the project.
- `glob_patterns` (List[str]): A list of glob patterns to filter which files to delete.
- `throw_on_error` (bool, optional): Whether to raise an error if file deletion fails. Defaults to `False`.
- `finished_cb` (Callable, optional): A callback function to be called after each file deletion. Deprecated and defaults to `None`.

Returns:

- A dictionary with the glob patterns as keys and the list of deleted files as values.

Example

```python
deleted_files = client.delete_files("project_id", ["*.qgz", "*.shp"])
```

#### Project Management Collaborators

:material-arrow-right-circle: `get_project_collaborators`

Retrieves a list of collaborators for a specified project.

Parameters:

- `project_id` (str): The unique identifier of the project.

Returns:

- `List[CollaboratorModel]`: A list of collaborators for the project.

Example:

```python
collaborators = client.get_project_collaborators("your_project_id")
```

:material-arrow-right-circle: ``add_project_collaborator``

Adds a collaborator to a specified project.

Parameters:

- `project_id` (str): The unique identifier of the project.
- `username` (str): The username of the collaborator to be added.
- `role` (ProjectCollaboratorRole): The role of the collaborator (e.g., `reader`, `reporter`, `editor`, `manager`, `admin`).

Returns:

- `CollaboratorModel`: The added collaborator.

Example:

```python
collaborator = client.add_project_collaborator("your_project_id", "new_user", ProjectCollaboratorRole.EDITOR)
```

:material-arrow-right-circle: ``remove_project_collaborators``

Removes a collaborator from a specified project.

Parameters:

- `project_id` (str): The unique identifier of the project.
- `username` (str): The username of the collaborator to be removed.

Example:

```python
client.remove_project_collaborators("your_project_id", "user_to_remove")
```

:material-arrow-right-circle: ``patch_project_collaborators``

Updates the role of an existing collaborator in a specified project.

Parameters:

- `project_id` (str): The unique identifier of the project.
- `username` (str): The username of the collaborator to be updated.
- `role` (ProjectCollaboratorRole): The new role of the collaborator.

Returns:

- `CollaboratorModel`: The updated collaborator.

Example:

```python
updated_collaborator = client.patch_project_collaborators("your_project_id", "existing_user", ProjectCollaboratorRole.MANAGER)
```

#### Organization Management Methods

:material-arrow-right-circle: `get_organization_members(self, organization: str) -> List[OrganizationMemberModel]`

Retrieves a list of members associated with a specified organization.

Parameters:

- `organization` (str): The username of the organization.

Returns:

- A list of `OrganizationMemberModel` objects representing the organization members.

Example:

```python
members = client.get_organization_members("org_username")
```

:material-arrow-right-circle: `add_organization_member(self, project_id: str, username: str, role: OrganizationMemberRole, is_public: bool) -> OrganizationMemberModel`

Adds a new member to the organization with a specified role.

Parameters:

- `project_id` (str): The unique identifier of the project.
- `username` (str): The username of the member to be added.
- `role` (OrganizationMemberRole): The role to assign to the member. Possible values are `admin` or `member`.
- `is_public` (bool): Indicates whether the member should be publicly accessible.

Returns:

- An `OrganizationMemberModel` object representing the newly added member.

Example:

```python
new_member = client.add_organization_member("project_id", "new_user", "member", True)
```

:material-arrow-right-circle: `remove_organization_members(self, project_id: str, username: str) -> None`

Removes a member from the organization.

Parameters:

- `project_id` (str): The unique identifier of the project.
- `username` (str): The username of the member to be removed.

Returns: `None`.

Example:

```python
client.remove_organization_members("project_id", "user_to_remove")
```

:material-arrow-right-circle: `patch_organization_members(self, project_id: str, username: str, role: OrganizationMemberRole) -> OrganizationMemberModel`

Updates the role of an existing member in the organization.

Parameters:

- `project_id` (str): The unique identifier of the project.
- `username` (str): The username of the member whose role is to be updated.
- `role` (OrganizationMemberRole): The new role to be assigned to the member.

Returns:

- An `OrganizationMemberModel` object representing the updated member.

Example:

```python
updated_member = client.patch_organization_members("project_id", "existing_user", "admin")
```

#### Internal Helper Methods

:material-arrow-right-circle: `_request_json(self, method: str, path: str, data: Any = None, params: Dict[str, str] = {}, headers: Dict[str, str] = {}, files: Dict[str, Any] = None, stream: bool = False, skip_token: bool = False, allow_redirects=None, pagination: Pagination = Pagination()) -> Union[List, Dict]`

Makes an HTTP request and returns the JSON response. Supports pagination for large datasets.

Parameters:

- `method` (str): HTTP method (e.g., "GET", "POST").
- `path` (str): API endpoint path.
- `data` (Any, optional): Data to send with the request.
- `params` (Dict[str, str], optional): Query parameters for the request.
- `headers` (Dict[str, str], optional): HTTP headers to include in the request.
- `files` (Dict[str, Any], optional): Files to upload.
- `stream` (bool, optional): Whether to stream the response.
- `skip_token` (bool, optional): Whether to skip the authorization token.
- `allow_redirects` (optional): Whether to follow redirects.
- `pagination` (Pagination, optional): Pagination parameters.

Returns:

- The JSON response, either as a list or a dictionary.

Example:

```python
response = client._request_json("GET", "uri")
```

:material-arrow-right-circle: `_request(self, method: str, path: str, data: Any = None, params: Dict[str, str] = {}, headers: Dict[str, str] = {}, files: Dict[str, Any] = None, stream: bool = False, skip_token: bool = False, allow_redirects=None, pagination: Optional[Pagination] = None) -> requests.Response`

Sends an HTTP request and returns the raw response object. Handles request preparation, session management, and error handling.

Parameters:

- `method` (str): HTTP method (e.g., "GET", "POST").
- `path` (str): API endpoint path.
- `data` (Any, optional): Data to send with the request.
- `params` (Dict[str, str], optional): Query parameters for the request.
- `headers` (Dict[str, str], optional): HTTP headers to include in the request.
- `files` (Dict[str, Any], optional): Files to upload.
- `stream` (bool, optional): Whether to stream the response.
- `skip_token` (bool, optional): Whether to skip the authorization token.
- `allow_redirects` (optional): Whether to follow redirects.
- `pagination` (Optional[Pagination]): Pagination parameters.

Returns:

- The raw response object from the request.

Example:

```python
response = client._request("GET", "uri")
```

## Module usage

```python
import requests
from qfieldcloud_sdk import sdk

client = sdk.Client(
    url="https://app.qfield.cloud/api/v1/"
)
client.login(username='me', password='mysecret')

try:
    projects = client.list_projects()
    print(projects)
except requests.exceptions.RequestException:
    print("Oops!")
```

### Example for Automating with a CSV file

#### CSV File

```text
username,org_role,proj_role
ninja_1,member,reader
ninja_2,member,editor
ninja_3,admin,manager
ninja_4,member,reporter
```

#### Python code

```python
def read_csv(csv_path: str, organization: str, project_id: str, is_public: bool):
    with open(csv_path, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for user in reader:
            try:
                client.add_organization_member(
                    organization, user["username"], user["org_role"], is_public
                )
                print(
                    f"Added member {user['username']} with role {user['org_role']} in {organization}"
                )
                client.add_project_collaborator(
                    project_id, user["username"], user["proj_role"]
                )
                print(
                    f"Added collaborator {user['username']} with role {user['proj_role']} to project ID {project_id}"
                )
            except requests.exceptions.RequestException:
                print("Oops!")


if __name__ == "__main__":
    organization = "OPENGIS"
    project_id = "f9b47cb1-ae8b-4f12-b95d-05c189f9a72c"
    is_public = False
    csv_path = 'path/to/files/ninjas_surveyors.csv'
    read_csv(csv_path, organization, project_id, is_public)

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
| ------- | -------------------------------- |
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
  collaborators-get     Get a list of project collaborators.
  collaborators-add     Add a project collaborator.
  collaborators-remove  Remove a project collaborator.
  collaborators-patch   Change project collaborator role.
  members-get           Get a list organization members.
  members-add           Add an organization member.
  members-remove        Remove an organization member.
  members-patch         Change organization member role.
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

#### collaborators-get¶

Get a list of project collaborators for a specific project with `PROJECT_ID`.

```bash
`qfieldcloud-cli collaborators-get [OPTIONS] PROJECT_ID`

Options:
- `PROJECT_ID`
  The ID of the project for which you want to list collaborators.
```

#### collaborators-add¶

Add a collaborator with `USERNAME` and a specific `ROLE` to a project with `PROJECT_ID`.

```bash
qfieldcloud-cli collaborators-add [OPTIONS] PROJECT_ID USERNAME ROLE

Options:
- `PROJECT_ID`
  The ID of the project to which the collaborator will be added.

- `USERNAME`
  The username of the collaborator to add.

- `ROLE`
  The role to assign to the collaborator. Possible values: `admin`, `manager`, `editor`, `reporter`, `reader`.
```

#### collaborators-remove¶

Remove a collaborator with `USERNAME` from a project with `PROJECT_ID`.

```bash
qfieldcloud-cli collaborators-remove [OPTIONS] PROJECT_ID USERNAME

Options:
- `PROJECT_ID`
  The ID of the project from which to remove the collaborator.

- `USERNAME`
  The username of the collaborator to remove.
```

#### collaborators-patch¶

Change the role of a collaborator with `USERNAME` to a new `ROLE` in a project with `PROJECT_ID`.

```bash
qfieldcloud-cli collaborators-patch [OPTIONS] PROJECT_ID USERNAME ROLE

Options:
- `PROJECT_ID`
  The ID of the project in which to change the collaborator’s role.

- `USERNAME`
  The username of the collaborator whose role is to be changed.

- `ROLE`
  The new role to assign to the collaborator. Possible values: `admin`, `manager`, `editor`, `reporter`, `reader`.
```

#### members-get¶

Get a list of members of an `ORGANIZATION`.

```bash
qfieldcloud-cli members-get [OPTIONS] ORGANIZATION

Options:
- `ORGANIZATION`
  The name of the organization for which to list members.
```

#### members-add¶

Add a member with `USERNAME` and `ROLE` to an `ORGANIZATION`.

```bash
qfieldcloud-cli members-add [OPTIONS] ORGANIZATION USERNAME ROLE

Options:
- `ORGANIZATION`
  The name of the organization to which the member will be added.

- `USERNAME`
  The username of the member to add.

- `ROLE`
  The role to assign to the member. Possible values: `admin`, `member`.

- `--public / --no-public`
  Specifies whether the membership should be public.
```

#### members-remove¶

Remove a member with `USERNAME` from an `ORGANIZATION`.

```bash
qfieldcloud-cli members-remove [OPTIONS] ORGANIZATION USERNAME

Options:
- `ORGANIZATION`
  The name of the organization from which to remove the member.

- `USERNAME`
  The username of the member to remove.
```

#### members-patch¶

Change the role of a member with `USERNAME` to a new `ROLE` in an `ORGANIZATION`.

```bash
qfieldcloud-cli members-patch [OPTIONS] ORGANIZATION USERNAME ROLE

Options:
- `ORGANIZATION`
  The name of the organization in which to change the member’s role.

- `USERNAME`
  The username of the member whose role is to be changed.

- `ROLE`
  The new role to assign to the member. Values: `admin`, `member`.
```
