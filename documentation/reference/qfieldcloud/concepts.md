---
title: Concepts
---

## Users

To interact with QFieldCloud you need a registered user. Each user can create, modify and delete **projects** and **organizations**.

## Projects

Projects are the main data container within QFieldCloud. Each user can create one or more QFieldCloud projects. Each project contains a single `.qgs`/`.qgz` QGIS project file, the geospatial files - geopackages, shapefiles, tiffs, and additional data such as photos, PDFs etc. Note all the project data should be within a single QFieldCloud project.

### Project collaborators

A project collaborator is a user invited to contribute to a project. One project may have multiple collaborators. Collaborators with role **owner** or **admin** can add more users as collaborators. If the project is owned by an organization, you can also add **teams** as collaborators.

## Organizations

Organizations are special type of users that allow easy collaboration of multiple users. Organizations can be created by any user and they can add **organization memebrs** to it. Each organization can own projects.

### Organization members

Organization membership allows automatic access to all projects within an organization. Members with **owner** or **admin** role can add other members.

### Organization teams

Teams allow organization members with **owner** or **admin** role to easily assign permissions to multiple users at once. A team consists of one or more organization members within the organization. When a team is assigned a role in a project, all the team members automatically have that role too. Teams can be added as collaborators only to projects owned by the same organization. One organization member can be part of multiple teams. If an organization member is a project collaborator directly or trough multiple teams, that organization member has the highest possible role.
