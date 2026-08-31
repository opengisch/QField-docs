---
title: Basic concepts
tx_slug: documentation_reference_qfieldcloud_concepts
---

# Basic concepts

## Users

To interact with QFieldCloud you need to be a registered user. Each user can create, modify and delete **projects** and **organizations**.
## Organizations

Organizations are shared accounts where multiple QFieldCloud users can collaborate across many projects at once.
Owners and administrators can manage member access to the organization's projects and projects with sophisticated security and administrative features.
Any QFieldCloud user can own or participate in one or more organizations.
Each organization owns one or more projects.

### Organization members

Organization membership allows access to projects within an organization.
Members with **owner** or **admin** role can add other members.

### Organization teams

Teams allow organization members with an **owner** or **admin** role to easily assign permissions to multiple users at once.
A team consists of one or more organization members within the organization.
When a team is assigned a role in a project, all the team members automatically have that role too.
Teams can be added as collaborators only to projects owned by the same organization.
One organization member can be part of multiple teams.
If an organization member is a project collaborator directly or through multiple teams, that organization member has the highest possible role.

## Projects

Projects are the main data container within QFieldCloud.
Each user can create one or more QFieldCloud projects.
Each project contains a single `.qgs`/`.qgz` QGIS project file, the geospatial files - GeoPackages, TIFs, and additional data such as photos, PDFs etc.
All project data files must be within a single QFieldCloud project.

Read more about [QFieldCloud Projects](../../reference/qfieldcloud/projects.md).

!![](../../assets/images/qfc_roles.svg,800px)

### Project collaborators

A project collaborator is another QFieldCloud user invited to contribute to a project.
One project may have multiple collaborators.
Collaborators can have the roles **Admin**, **Manager**, **Editor**, **Reporter**, and **Reader**.
Only users with the roles of **Admin** and **Manager** can add more users as collaborators to the project.
If the project is owned by an organization, whole **teams** (e.g. `@organization/team`) can also be added as collaborators.
Read more about [collaborator roles](../../reference/qfieldcloud/permissions.md).

### Adding collaborators to a project

:material-monitor: Desktop preparation

In order to add users to your projects, they need to be part of your organization.
You can add collaborators to your projects under app.qfield.cloud in the corresponding project page.

!!! Workflow

    1. Direct to the *project overview page* > *collaborator*
    2. Add the desired user or teams.

    ![type:video](../../assets/videos/multi_select.webm)

    **Note:**
    You can add up to 20 users/teams at once.
    Collaborators must first be a Member of the Organization.
