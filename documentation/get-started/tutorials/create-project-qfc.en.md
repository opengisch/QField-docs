---
title: Project creation in QFieldCloud
tx_slug: documentation_get-started_tutorials_create-project-qfc
---

## Project creation

In general, there are multiple options how to create a QFieldCloud project:

- [Using QGIS](my-first-project.md)
- [Using QFieldCloud](#creating-a-project-in-qfieldcloud)
- [Directly from QField](../../how-to/project-setup/create-project.md)

## Creating a project in QFieldCloud

!!! Workflow

     1. On your landing page on QField Cloud click on "Create  project".

        !![](../../assets/images/project_organization_01_landing_page.png,800px)

        - Add your project name, give a description and select the required settings regarding conflict management and project file restriction.
        - Choose your preferred project creation method:
            - **Create an empty project:** This will create a complete empty project without any basemap.
            - **Use a basic template:** This will allow you to select a dedicated basemap provider either OpenStreetMap (by default) or your preffered basemap provider for which you need to provide the URL and define your project extent.
            You can do this by clicking on the little map icon on the right of the Project extent line.

        ![Template Project](../../assets/images/project_organization_03_template.png)

        Once you have entered all your details click *Create* at the bottom right of the screen

    2. You can now see the new project in the overview.

        ![New project created](../../assets/images/project_organization_04_new_project_created.png)

    3. In QGIS open QFieldSync and you will see the new project listed, click on "Edit Selected Cloud Project".

        ![QFieldSync](../../assets/images/project_organization_05_qfield_sync.png)

    4. Choose the folder where you want to save the project.

        ![Selecting folder](../../assets/images/project_organization_06_selecting_folder.png)

    5. In the selected folder, you can either paste an already worked-on project or save a new one.

        ![Copy to project folder](../../assets/images/project_organization_07_copy_project_to_folder.png)

    6. Once the folder contains the project, you can synchronize it.

        ![QFieldSync Overview](../../assets/images/project_organization_08_qfield_sync_overview.png)

    7. Finally, push the changes to the cloud.

        ![Pushing changes to QFieldCloud](../../assets/images/project_organization_09_pushing_changes_to_cloud.png)

    8. You can verify that the files are present in the Organization project.

        ![Project files over view in QFieldCloud](../../assets/images/project_organization_10_files_overview_in_cloud.png)

    ![type:video](../../assets/videos/creating_empty_project_from_qfc.webm)


## Cloning Projects

If you do not want to use the basic basemap template you also have the possibility to duplicate existing projects through its cloning functionality.
This feature is highly useful when you need to establish project templates, duplicate a survey project for a different team, or start a new data collection campaign using an identical QGIS configuration to a previous successful project.

### How Cloning Works

When you clone a project, QFieldCloud creates a brand new project and duplicates the following elements from the source project:

- The QGIS project file (e.g., `.qgs` or `.qgz`).
- All associated project files and datasets (GeoPackages, images, etc.).
- Project settings, including description, public status, offline editing configurations, conflict resolution, and attachment download policies.

The newly cloned project is completely independent.
Any subsequent changes, file uploads, or data collection done within the cloned project will not affect the original source project.

!!! Workflow

    1. On your QFieldCloud landing page click on the three dots next to the project that you wish to clone.
    2. Choose an alternative name to your original project.
    3. Add the parameters and configuration settings you would like.
    4. At the bottom zou have to select the project extent for which you would like to clone the project.
    5. Once done, click "Create"

    ![type:video](../../assets/videos/clonning_projects_in_qfc.webm)



### Overriding Project Parameters

While cloning effectively duplicates the source project, you can override specific parameters during the creation process:

- **Project Name:** You must provide a unique name for the new cloned project (e.g., `survey_zone_b`, `survey_zone_n`).
- **Owner:** You can assign the cloned project to a different owner (e.g., a specific organization or user account), with the appropriate permissions.
- **Extent:** By providing new extent for the cloned project (for easy moving the zoom to the new extend zone).

### Constraints and Limitations

To ensure system stability and security, project cloning is subject to the following technical rules:

- **Permissions:** You must have admin, manager role to the source project to be able to clone it.
- **Storage availability:** The target owner account must have enough free storage available to accommodate the entire file size of the source project.
    If the storage limit is exceeded, the clone operation will fail.
- **XLSForms:** Project cloning is mutually exclusive with XLSForm project creation. You cannot provide an XLSForm file and clone an existing project simultaneously.
- **Seed Configuration:** When cloning, you cannot configure new basemaps via the project seed. The seed data is strictly limited to updating the project's `extent`.
- **Shared Datasets:** The system-level `shared_datasets` project cannot be used as a source for cloning. Attempting to clone it will raise a `NotCloneableProjectError`.

### API Usage

Users and developers can easily clone projects using the QFieldCloud API. To clone a project, send a `POST` request to the `/api/v1/projects/` endpoint.
Include the `clone_from_project` parameter with the UUID of the source project.

**Example Request:**
```bash
curl --location 'https://app.qfield.cloud/api/v1/projects/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token {MY_TOKEN}' \
--data '{
    "name" : "clone-me-public",
    "is_public": true,
    "description": "Hello from the cloned public project",
    "owner": "{USERNAME}",
    "seed": {
        "extent": "-180, -90, 180, 90"
    },
    "clone_from_project": "{PROJECT_UUID}"
}'
```

!!! note
    The seed object is optional and only accepts the extent field when utilizing the clone functionality.
