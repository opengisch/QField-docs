---
title: Permissions and Roles
tx_slug: documentation_reference_qfieldcloud_permissions
---

# Permissions and Roles

QFieldCloud provides fine-grained access control over projects and organizations using **Project Collaborator** roles and **Organization Member** roles.

Access permissions follow a strict hierarchy: **a higher role automatically inherits all capabilities of lower roles.**


## Project Roles (Collaborators)

Project roles determine what a user can do within a specific project.

| Role | Summary |
| :--- | :--- |
| **Owner / Admin** | Full control over the project, including renaming, deleting, managing secrets, and modifying restricted project files (`.qgz`/`.qgs`). |
| **Manager** | Can manage project collaborators and dataset files. *(Organization projects only)* |
| **Editor** | Can create, update, and delete features and their attributes in the field.
*(Organization projects only)* |
| **Reporter** | Can download the project and collect **new** features in the field, but cannot edit or delete existing features. |
| **Reader** | Read-only access to view and download the project. Cannot upload edits or changes. |

!!! note
    **"Personal vs. Organization Projects"**

    Collaborators on **Personal (Pro)** projects can only add one other collaborator with a **Personal (Pro)**.
    To assign more than one collaborator, the project must belong to an **Organization Plan**.


### Project Capabilities Matrix

The following table details what each project role can do:

| Capability | Reader | Reporter | Editor | Manager | Admin / Owner |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **View and download project files** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Collect NEW features in the field** | ❌ | ✅ | ✅ | ✅ | ✅ |
| **UPDATE or DELETE existing features** | ❌ | ❌ | ✅ | ✅ | ✅ |
| **Upload datasets (e.g., GeoPackages)** | ❌ | ❌ | ✅ | ✅ | ✅ |
| **Manage project collaborators** | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Manage project secrets & service credentials** | ❌ | ❌ | ❌ | ❌| ✅ |
| **Modify restricted project files (`.qgz`, styles)** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Rename or delete the project** | ❌ | ❌ | ❌ | ❌ | ✅ |


## Organization Roles

Within an organization you can be assigned either as an admin or a general member.
Depending on your role you will have access and the ability to modify the billing page, the member list, and all projects owned by that organization.

| Role | Description | Capabilities |
| :--- | :--- | :--- |
| **Owner / Admin** | Full administrative control over the organization. | - Add and remove organization members<br>- Change member roles<br>- Create projects under the organization<br>- Access billing, subscription, and active user details (Owner only)|
| **Member** | Standard member of the organization. | - View the organization member list<br>- Access specific organization projects where they have been assigned a project collaborator role |


## Key Security Features

### Restricted Project Files

When the **"Restrict project files"** setting is enabled on a project, standard **Editors** and **Managers** can continue updating datasets (such as GeoPackages), but they are blocked from modifying or replacing core project files (such as `.qgz` or `.qgs` project files and style templates).
Only **Admins** and **Owners** can modify restricted files.

### Public vs. Private Projects
- **Public Projects:** Can be viewed and downloaded by any registered QFieldCloud user.
- However, editing features or uploading changes still requires an explicit **Reporter**, **Editor**, **Manager**, or **Admin** role on the project.
- **Private Projects:** Visible only to the project owner, organization admins, and explicitly added project collaborators.
