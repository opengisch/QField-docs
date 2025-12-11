---
title: QFieldCloud Django Administration
tx_slug: documentation_reference_qfieldcloud_django_administration
---

# How to manage Organizations in QFieldCloud on-premise

## Managing Users

### Adding

!!! Workflow

    1. From the homepage, scroll down to find the "Core" pages and select the "People" page.
    2. Click on "Add Person".
    !![](../../../assets/images/self_hosted/managing_organization_django_01.png,800px)

    3. Fill in the required fields, including the "Username", "Password", "Email address", and any additional user information.

    !!! Tip

        You can also set the user's "Timezone" and email notification preferences for project and organization changes.

    4. Click "Save" to add the user, and you'll be redirected to the "People" page with a success message.
     !![](../../../assets/images/self_hosted/managing_organization_django_02.png,800px)

    !!! Tip

        The "Password" field will show the hashed version of any password.
        If a system administrator wants to change it, just replace the contents with the new password, QFieldCloud will handle it automatically.

### Deleting

!!! Workflow

    1. In the "Core" pages, click on "People".
    2. Select the user by clicking on its "Username".
    3. Click the "Delete" button.
    !![](../../../assets/images/self_hosted/managing_organization_django_03.png,800px)

    4. The screen will show you all the related objects that will be deleted.
    Once you are sure that you wish to complete the deletion click "Yes, I'm sure".
    !![](../../../assets/images/self_hosted/managing_organization_django_04.png,800px)

    5. You will be redirected to the "People" Section and a message should appear at the top of the page indicating the successful deletion.
    !![](../../../assets/images/self_hosted/managing_organization_django_05.png,800px)

### Generating a Reset Password URL

!!! Workflow

    1. Access the "People" Page under the "Core" pages section.
    2. Click on the "Username" of the user for whom you want to generate a new password URL.
    3. On the user's page to find the "Generate reset password URL" option.
    !![](../../../assets/images/self_hosted/managing_organization_django_06.png,800px)

    4. The manager should send the URL to the user via email for password reset.
    !![](../../../assets/images/self_hosted/managing_organization_django_07.png,800px)

## Managing Organizations

### Adding

!!! Worflow

    1. Click on "Organizations" under the "Core" section.
    2. Click "Add Organization".
    !![](../../../assets/images/self_hosted/managing_organization_django_08.png,800px)

    3. Fill in the organization details, including "Username" for the organization name, "Email address" for the admin, and select the owner from the dropdown list.
    !![](../../../assets/images/self_hosted/managing_organization_django_09.png,800px)

    4. Click "Save" to create the organization, and a success message should be shown at the top of the browser.

### Deleting

!!! Workflow

    1. Click on "Organizations" under the "Core" section.
    2. Click on the organization's name.
    !![](../../../assets/images/self_hosted/managing_organization_django_10.png,800px)

    3. Find the "Delete" button.
    !![](../../../assets/images/self_hosted/managing_organization_django_11.png,800px)

    4. The screen will show you all the related objects that will be deleted.
    Once you are sure that you wish to complete the deletion click "Yes, I'm sure".
    !![](../../../assets/images/self_hosted/managing_organization_django_12.png,800px)

    5.You will be redirected to the "Organization" Section and a message should appear at the top of the page indicating the successful deletion.
    !![](../../../assets/images/self_hosted/managing_organization_django_13.png,800px)

### Adding Members

!!! Workflow

    1. Go to the "Organizations" page and select the organization where you want to add a new member.
    2. Open the "Organization members" tab and click on "Add another Organization member".
    !![](../../../assets/images/self_hosted/managing_organization_django_14.png,800px)

    3. In the search bar, type the username of the user you want to add.
    !![](../../../assets/images/self_hosted/managing_organization_django_15.png,800px)

    4. After finding the user, click on the name and add them to the "Organization Members" list.

    5. Once all desired members are added, click on "Save".
    !![](../../../assets/images/self_hosted/managing_organization_django_16.png,800px)

    6. You will be redirected to the "Team" Section and a message should appear at the top of the page indicating the successful addition of members.

### Remove Members

!!! Worfklow

    1. Go to the "Organizations" page and select the organization where you want to remove one or multiple members.
    2. Open the "Organization members" tab.
    3. Check the "Delete?" checkbox for the user you want to remove.
    !![](../../../assets/images/self_hosted/managing_organization_django_17.png,800px)

    4. Click "Save".
    !![](../../../assets/images/self_hosted/managing_organization_django_18.png,800px)

    5. You will be redirected to the "Organization Member" Section and a message should appear at the top of the page indicating the successful removal of the selected members.

### Changing Roles of Members

!!! Workflow

    1. Find the organization where you wish to change the role of the member.
    2. Open the "Organization members" tab.
    3. In the "Role" field of the user, click the dropdown and choose "Member" or "Admin".
    !![](../../../assets/images/self_hosted/managing_organization_django_19.png,800px)

    4. Select the role you want to assign to the user and click to "Save" the updated data for the "Organization".
    5. You will be redirected to the "Team" Section and a message should appear at the top of the page indicating the successful role change of the selected members.

### Creating Teams

!!! Workflow

    1. Access the "Teams" pages under the "Core" section.
    2. Click on "Add Team".
    !![](../../../assets/images/self_hosted/managing_organization_django_20.png,800px)

    3. Provide a name for the team in the "Username" field and select the organization where the team should belong.
    !![](../../../assets/images/self_hosted/managing_organization_django_21.png,800px)

    4. In the "Team members" section, click on "Add another Team member".
    !![](../../../assets/images/self_hosted/managing_organization_django_23.png,800px)

    5. Search for the team members you wish to add.
    The people added to the Team must be members of the Team's Organization.
    !![](../../../assets/images/self_hosted/managing_organization_django_22.png,800px)

    6. Once all members are added, click "Save".
    7. You will be redirected to the "Teams" section and a message should appear at the top of the page indicating the successful addition of the selected members to the team.

### Deleting Teams

!!! Worfklow

    1. Access the "Teams" page under the "Core" section
    2. Find the team which you wish to delete.
    3. Select the "Delete Button".
    !![](../../../assets/images/self_hosted/managing_organization_django_24.png,800px)

    3. The screen will show you all the related objects that will be deleted.
    Once you are sure that you wish to complete the deletion click "Yes, I'm sure".
    !![](../../../assets/images/self_hosted/managing_organization_django_26.png,800px)

    4. You will be redirected to the "Teams" section and a message should appear at the top of the page indicating the successful deletion of the selected members.

### Removing Members from the Team

!!! Workflow

    1. Enter the team where you want to delete users.
    2. In the team, activate the "Delete?" checkbox for the users you want to remove.
    !![](../../../assets/images/self_hosted/managing_organization_django_25.png,800px)

    3. Click to "Save" the updated data for the "Team".
    4. You will be redirected to the "Teams" section and a message should appear at the top of the page indicating the successful removal of the selected members.

## Managing Projects

### Creating Projects

There are two ways in which you can create projects, follow either Method 1 or Method 2.

#### Method 1: Convert a Local Project to a QFieldCloud Project

!!! Workflow

    1. In QGIS, access your project and open the QFieldSync plugin.
    2. Click on "QFieldCloud Projects Overview".
    3. Click "Create New Project".
    4. Choose the first option "Convert the currently open project to a cloud project".
    !![](../../../assets/images/self_hosted/managing_organization_django_27.png,800px)

    5. Provide project details and select the organization.
    6. Click "Create".
    !![](../../../assets/images/self_hosted/managing_organization_django_28.png,800px)

    7. Once completed, click "Ok".
    8. The project will be listed in the "QFieldCloud Projects Overview".
    9. In the Admin view, navigate to the "Projects" and inspect the project's information.
    !![](../../../assets/images/self_hosted/managing_organization_django_29.png,800px)

#### Method 2: Creating an Empty Project

You can create Empty projects by using QFieldSync or directly in QFieldCloud.

**2.1. Creating an empty project QFieldCloud method**

!!! Workflow

    1. Go to the "Projects" Section and click on "Add Project".
    !![](../../../assets/images/self_hosted/managing_organization_django_30.png,800px)

    2. Fill in the project details and select an organization as the owner.
    3. Click to "Save" the updated data for the project.
    !![](../../../assets/images/self_hosted/managing_organization_django_31.png,800px)

    4. In QGIS use QFieldSync to access the "QFieldCloud Projects Overview".
    5. Select the newly created project and synchronize it.
    6. Choose the path for storing the project files and complete the synchronization.
    !![](../../../assets/images/self_hosted/managing_organization_django_34.png,800px)

    7. Click "Ok".
    8. Edit the project in an external file browser.
    9. Paste the necessary project files into the folder.
    10. Return to QFieldSync and complete the synchronization.
    !![](../../../assets/images/self_hosted/managing_organization_django_35.png,800px)

    11. Once finished, inspect the files in the project.
    !![](../../../assets/images/self_hosted/managing_organization_django_36.png,800px)

**2.2. Creating an empty project QFieldSync Method**

!!! Workflow

    1. In QGIS and the QFieldSync plugin, go to the "QFieldCloud Projects Overview."
    2. Click the "Create New Project" button.
    !![](../../../assets/images/self_hosted/managing_organization_django_37.png,800px)

    3. Select "Create a new empty QFieldCloud project" and click "Next".
    !![](../../../assets/images/self_hosted/managing_organization_django_38.png,800px)

    4. Fill in the project name and select the organization as the project owner.
    !![](../../../assets/images/self_hosted/managing_organization_django_39.png,800px)

    5. For the "Local Directory," you can select an existing project or an empty folder, then click the "Create" button.
    6. If you choose an empty folder, copy the project files into it.
    7. Go back to QFieldSync and finish the synchronization.
    !![](../../../assets/images/self_hosted/managing_organization_django_40.png,800px)

### Deleting Projects

!!! Workflow

    1. Enter to the "Projects" Section in QFieldCloud Admin.
    2. Select the project you want to delete and click "Delete".
    !![](../../../assets/images/self_hosted/managing_organization_django_41.png,800px)

    3. The screen will show you all the related objects that will be deleted.
    Once you are sure that you wish to complete the deletion click "Yes, I'm sure"
    !![](../../../assets/images/self_hosted/managing_organization_django_42.png,800px)

### Adding Project Collaborators

!!! Workflow

    1. Enter the project and access the "Project collaborators" section, click "Add another Project collaborator".
    2. Search for the user or team you wish to add.
    3. Assign the corresponding [permissions](../permissions.md#roles) roles to the different users.
    !![](../../../assets/images/self_hosted/managing_organization_django_43.png,800px)

    4. Click "Save".
    5. You will be redirected to the "Collaborator" section and a message should appear at the top of the page indicating the successful addition of the selected prject collaborators

### Changing Roles of Collaborators

!!! Workflow

    1. Enter the project and access the "Project collaborators" section.
    2. Change the roles of collaborators by selecting the desired role from the dropdown.
    !![](../../../assets/images/self_hosted/managing_organization_django_44.png,800px)

    4. Click "Save".
    5. You will be redirected to the "Project" section and a message should appear at the top of the page indicating the successful Role change of the selected members

### Making and Reviewing Changes

!!! Workflow

    1. Enter to "Deltas" section in the "Core" pages.
    !![](../../../assets/images/self_hosted/managing_organization_django_45.png,800px)

    2. Click on the delta you want to inspect.
    You will see the content in JSON format, showing the corresponding changes.
    !![](../../../assets/images/self_hosted/managing_organization_django_46.png,800px)

    3. In QGIS and the QFieldSync plugin, synchronize the current cloud project changes.
    4. Once the synchronization is complete, check the changes downloaded from QFieldCloud in the "Attribute table" of the layers and attachments folders.

### Managing PostGIS secrets

!!! Workflow

    1. In "Projects", select the project.
    2. Open the "Secrets" tab.
    !![](../../../assets/images/self_hosted/managing_organization_django_47.png,800px)

    3. Click on "Add Secret".
    !![](../../../assets/images/self_hosted/managing_organization_django_48.png,800px)

    4. Fill in the "Name" of the secret (this should be in all uppercase). In the "Type" field, choose "pg_service" from the dropdown list.
    5. Fill the "Value" field with the credentials of the `pg_service` connection established on the layers.
    !![](../../../assets/images/self_hosted/managing_organization_django_49.png,800px)

    6. Click to "Save" the updated data for the project.
    7. You will be redirected to the "Secrets" page with a success message.
