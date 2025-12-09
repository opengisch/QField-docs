---
title: QFieldCloud Django Administration
tx_slug: documentation_reference_qfieldcloud_django_administration
---

# How to manage Organizations in QFieldCloud on-premise

## Managing Users

### Adding

!!! Workflow

    1. From the homepage, scroll down to find "Core" pages and select "People" page.
    2. Click "Add Person".

     !![](../../../assets/images/self_hosted/managing_organization_django_01.png,800px)
     3. Fill in the required fields, including "Username", "Password", "Email address", and any additional user information.

    !!! Tip
        You can also set the user's "Timezone" and email notification preferences for project and organization changes.
     4. Click "Save" to add the user, and you'll be redirected to the "People" page with a success message.

     !![](../../../assets/images/self_hosted/managing_organization_django_02.png,800px)

    !!! Tip

        The "Password" field will show the hashed version of the password.
        If a system administrator wants to change it, just replace the contents with the new password, QFieldCloud will automatically handle it.

### Deleting

!!! Workflow

    1. In the "Core" pages, click on "People".
    2. Select the user by clicking on their "Username".
    3. Click the "Delete" button.

    !![](../../../assets/images/self_hosted/managing_organization_django_03.png,800px)
    4. The screen will show you all the related objects that will be deleted. When you double check this is what you want, proceed with deletion by clicking "Yes, I'm sure".

    !![](../../../assets/images/self_hosted/managing_organization_django_04.png,800px)
    5. You will be redirected to the "People" page with a success message.

    !![](../../../assets/images/self_hosted/managing_organization_django_05.png,800px)

### Generating a Reset Password URL

!!! Workflow

    1. Access the "People" in the "Core" pages.
    2. Click on the "Username" of the user for whom you want to generate a reset password URL.
    3. On the user's page to find the "Generate reset password URL" option.

    !![](../../../assets/images/self_hosted/managing_organization_django_06.png,800px)
    4. The manager should send the URL to the user via email for password reset.

    !![](../../../assets/images/self_hosted/managing_organization_django_07.png,800px)

## Managing Organizations

### Adding

!!! Worflow

    1. Click on "Organizations" in the "Core" pages.
    2. In the "Organizations" page, click "Add Organization".

    !![](../../../assets/images/self_hosted/managing_organization_django_08.png,800px)
    3. Fill in the organization details, including "Username" for the organization name, "Email address" for the admin, and select the owner from the dropdown list.

    !![](../../../assets/images/self_hosted/managing_organization_django_09.png,800px)
    4. Click "Save" to create the organization, and you'll receive a success message.

### Deleting

!!! Workflow

    1. In the "Organizations" page, click on the organization's name.

    !![](../../../assets/images/self_hosted/managing_organization_django_10.png,800px)
    2. Find the "Delete" button.

    !![](../../../assets/images/self_hosted/managing_organization_django_11.png,800px)
    3. The screen will show you all the related objects that will be deleted.
    When you double check that this is what you want, proceed with deletion by clicking "Yes, I'm sure".

    !![](../../../assets/images/self_hosted/managing_organization_django_12.png,800px)
    4. You will be redirected to the "Organizations" page with a success message.

    !![](../../../assets/images/self_hosted/managing_organization_django_13.png,800px)

### Adding Members

!!! Workflow

    1. Go to the "Organizations" page and select the organization where you want to add members.
    2. Open the "Organization members" tab and click "Add another Organization member".

    !![](../../../assets/images/self_hosted/managing_organization_django_14.png,800px)
    3. In the search bar, type the usernames of the users you want to add.

    !![](../../../assets/images/self_hosted/managing_organization_django_15.png,800px)
    4. After finding the users, click on their names to add them to the "Organization Members" list.

    5. Once all desired members are added, click to "Save" the updated data for the "Organization".

    !![](../../../assets/images/self_hosted/managing_organization_django_16.png,800px)
    6. You will be redirected to the "Organizations" page with a success message.

### Remove Members

!!! Worfklow

    1. Go to the "Organizations" page and select the organization where you want to remove members.
    2. Open the "Organization members" tab.
    3. Activate the "Delete?" checkbox for the user you want to remove.

    !![](../../../assets/images/self_hosted/managing_organization_django_17.png,800px)
    4. Click to "Save" the updated data for the "Organization".

    !![](../../../assets/images/self_hosted/managing_organization_django_18.png,800px)
    5. You will be redirected to the "Organizations" with a success message.

### Changing Roles of Members

!!! Workflow

    1. Enter the organization where the user's role you want to change is located.
    2. Open the "Organization members" tab.
    3. In the "Role" field, click the dropdown and choose "Member" or "Admin".

    !![](../../../assets/images/self_hosted/managing_organization_django_19.png,800px)
    4. Select the role you want to assign to the user and click to "Save" the updated data for the "Organization".
    5. You will be redirected to the "Organizations" with a success message.

### Creating Teams

!!! Workflow

    1. Access the "Teams" pages in the "Core" pages.
    2. Click "Add Team".

    !![](../../../assets/images/self_hosted/managing_organization_django_20.png,800px)
    3. Provide a name for the team in the "Username" field and select the organization where the team should belong.

    !![](../../../assets/images/self_hosted/managing_organization_django_21.png,800px)
    4. In the "Team members" section, click "Add another Team member".
    5. Search for and add the usernames of users you want in the team.
    6. The people added to the Team must be member of the Team's Organization.

    !![](../../../assets/images/self_hosted/managing_organization_django_22.png,800px)
    7. Once all members are added, lick to "Save" the updated data for the "Team".
    8. You will be redirected to the "Teams" page with a success message.

### Deleting Teams

!!! Worfklow

    1. Enter the team by clicking on its name.
    2. Click the "Delete" button.

    !![](../../../assets/images/self_hosted/managing_organization_django_23.png,800px)
    3. The screen will show you all the related objects that will be deleted. When you double check this is what you want, proceed with deletion by clicking "Yes, I'm sure".

    !![](../../../assets/images/self_hosted/managing_organization_django_24.png,800px)
    4. You will be redirected to the Teams page with a success message.

### Removing Members from the Team

!!! Workflow

    1. Enter the team where you want to delete users.
    2. In the team, activate the "Delete?" checkbox for the users you want to remove.

    !![](../../../assets/images/self_hosted/managing_organization_django_25.png,800px)
    3. Click to "Save" the updated data for the "Team".
    4. You will be redirected to the "Teams" page with a success message.

## Managing Projects

### Creating Projects

There are two ways in which you can create projects, follow either Method 1 or Method 2.

!!! Workflow

    **Method 1: Convert a Local Project to a QFieldCloud Project**

    1. In QGIS, access your project and open the QFieldSync plugin.
    2. Click the "QFieldCloud Projects Overview" button.
    3. Click "Create New Project".

    !![](../../../assets/images/self_hosted/managing_organization_django_26.png,800px)

     4. Choose the option to "Convert the currently open project to a cloud project".

    !![](../../../assets/images/self_hosted/managing_organization_django_27.png,800px)

    5. Provide project details and select the organization.
    6. Click "Create" to initiate the conversion.

    !![](../../../assets/images/self_hosted/managing_organization_django_28.png,800px)

    7. Once completed, click "Ok".
    8. The project will be listed in the "QFieldCloud Projects Overview".
    9. In QFieldCloud, navigate to the "Projects" and inspect the project's information.

     !![](../../../assets/images/self_hosted/managing_organization_django_29.png,800px)

**Method 2: Creating an Empty Project**

You can create Empty projects by using QFieldSync or directly in QFieldCloud.

#### 2.1. Creating an empty project QFieldCloud method

* Go to the "Projects" page and click "Add Project".

!![](../../../assets/images/self_hosted/managing_organization_django_30.png,800px)

* Fill in project details and select the organization as the owner.

* Click to "Save" the updated data for the project.

!![](../../../assets/images/self_hosted/managing_organization_django_31.png,800px)

* In QGIS and the QFieldSync plugin, access the "QFieldCloud Projects Overview".
* Select the new project and synchronize it.
* Choose the path for storing the project files and complete the synchronization.

!![](../../../assets/images/self_hosted/managing_organization_django_34.png,800px)

* Click "Ok".
* Edit the project in an external file browser.
* Paste the necessary project files into the folder.
* Return to QFieldSync and complete the synchronization.

!![](../../../assets/images/self_hosted/managing_organization_django_35.png,800px)

* Once finished, inspect the files in the project.

!![](../../../assets/images/self_hosted/managing_organization_django_36.png,800px)

##### 2.2. Creating an empty project QFieldSync Method

* In QGIS and the QFieldSync plugin, go to the "QFieldCloud Projects Overview."
* Click the "Create New Project" button.

!![](../../../assets/images/self_hosted/managing_organization_django_37.png,800px)

* Select "Create a new empty QFieldCloud project" and click "Next".

!![](../../../assets/images/self_hosted/managing_organization_django_38.png,800px)

* Fill in the project name and select the organization as the project owner.

!![](../../../assets/images/self_hosted/managing_organization_django_39.png,800px)

* For the "Local Directory," you can select an existing project or an empty folder, then click the "Create" button.
* If you choose an empty folder, paste the project files into it.
* Go back to QFieldSync and finish the synchronization.

!![](../../../assets/images/self_hosted/managing_organization_django_40.png,800px)

#### Deleting Projects

* Enter to the "Projects".
* Select the project you want to delete and click "Delete".

!![](../../../assets/images/self_hosted/managing_organization_django_41.png,800px)

* The screen will show you all the related objects that will be deleted. When you double check this is what you want, proceed with deletion by clicking "Yes, I'm sure".

!![](../../../assets/images/self_hosted/managing_organization_django_42.png,800px)

#### Adding Project Collaborators

* Enter the project and access the "Project collaborators" section, click "Add another Project collaborator".
* Search for users or teams and add them.
* Assign the corresponding [permissions](../permissions.md#roles) roles.

!![](../../../assets/images/self_hosted/managing_organization_django_43.png,800px)

* Click to "Save" the updated data for the project.
* You will be redirected to the "Projects" page with a success message.

#### Changing Roles of Collaborators

* Enter the project and access the "Project collaborators" section.
* Change the roles of collaborators by selecting the desired role from the dropdown.

!![](../../../assets/images/self_hosted/managing_organization_django_44.png,800px)

* Click to "Save" the updated data for the project.
* You will be redirected to the "Projects" page with a success message.

#### Making and Reviewing Changes

* Enter to "Deltas" page in the "Core" pages.

!![](../../../assets/images/self_hosted/managing_organization_django_45.png,800px)

* Click on the delta you want to inspect. You will see the content in JSON format, showing the corresponding changes.

!![](../../../assets/images/self_hosted/managing_organization_django_46.png,800px)

* In QGIS and the QFieldSync plugin, synchronize the current cloud project changes.
* Once the synchronization is complete, check the changes downloaded from QFieldCloud in the "Attribute table" of the layers and attachments folders.

#### Managing PostGIS secrets

* In "Projects", select the project, and open the "Secrets" tab.

!![](../../../assets/images/self_hosted/managing_organization_django_47.png,800px)

* Click on "Add Secret".

!![](../../../assets/images/self_hosted/managing_organization_django_48.png,800px)

* Fill in the "Name" of the secret (this should be in all uppercase). In the "Type" field, choose "pg_service" from the dropdown list.
* Fill the "Value" field with the credentials of the `pg_service` connection established on the layers.

!![](../../../assets/images/self_hosted/managing_organization_django_49.png,800px)

* Click to "Save" the updated data for the project.
* You will be redirected to the "Secrets" page with a success message.
