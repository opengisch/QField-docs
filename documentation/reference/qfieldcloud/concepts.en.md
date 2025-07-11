---
title: Basic concepts
tx_slug: documentation_reference_qfieldcloud_concepts
---

# Basic concepts

## Users

To interact with QFieldCloud you need to be a registered user. Each user can create, modify and delete **projects** and **organizations**.

## Projects

Projects are the main data container within QFieldCloud.
Each user can create one or more QFieldCloud projects.
Each project contains a single `.qgs`/`.qgz` QGIS project file, the geospatial files - GeoPackages, TIFs, and additional data such as photos, PDFs etc.
All project data files must be within a single QFieldCloud project.

Read more about [QFieldCloud Projects](./projects.md).

### Project collaborators

A project collaborator is another QFieldCloud user invited to contribute to a project.
One project may have multiple collaborators.
Collaborators can either have the role **owner** or **admin**. Depending on their role collaborators can add more users.
If the project is owned by an organization, whole **teams** can also be added as collaborators.
Read more about [collaborator roles](permissions.md).

## Organizations

Organizations are shared accounts where multiple QFieldCloud users can collaborate across many projects at once.
Owners and administrators can manage member access to the organization's projects and projects with sophisticated security and administrative features.
Any QFieldCloud user can own or participate in one or more organizations.
Each organization owns one or more projects.

### Organization members

Organization membership allows access to projects within an organization.
Members with **owner** or **admin** role can add other members.

### Organization teams

Teams allow organization members with a **owner** or **admin** role to easily assign permissions to multiple users at once.
A team consists of one or more organization members within the organization.
When a team is assigned a role in a project, all the team members automatically have that role too.
Teams can be added as collaborators only to projects owned by the same organization.
One organization member can be part of multiple teams.
If an organization member is a project collaborator directly or through multiple teams, that organization member has the highest possible role.
