---
title: Permissions
---

# Permissions
## Actors
   1. Unregistered user
   2. Simple registered user, neither collaborator of the concerned project nor member of the concerned organization nor the concerned user
   3. Project owner of the concerned project, the conerned user, but not collaborator nor organization member
   4. Project collaborator role admin of the concerned project
   5. Project collaborator role manager of the concerned project
   6. Project collaborator role editor of the concerned project
   7. Project collaborator role reporter of the concerned project
   8. Project collaborator role reader of the concerned project
   9. Organization owner of the concerned organization or the organization that owns the concerned project or to which belongs the user
   10. Organizaton member role admin of the concerned organization or the organization that owns the concerned project or to which belongs the user
   11. Organization member role member of the concerned organization or the organization that owns the concerned project or to which belongs the user

## Actions
   *0* -> Not allowed

   *1* -> Allowed

   *-* -> Irrelevant

<div class="special_table"></div>
| Action                                                                        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |   |
|-------------------------------------------------------------------------------|---|---|---|---|---|---|---|---|---|----|----|---|
| List/query project's collaborator roles                                       | 0 | 1 | - | - | - | - | - | - | - | -  | -  |   |
| Create project's collaborator (i.e. define new collaborator)                  | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1  | 0  |   |
| Update project's collaborator's info (i.e. role)                              | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1  | 0  |   |
| Delete project's collaborator (i.e. remove user as collaborator)              | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1  | 0  |   |
| List organization's members                                                   | 0 | 1 | - | - | - | - | - | - | 1 | 1  | 1  |   |
| Create organization's member (i.e. define a new member)                       | 0 | 0 | - | - | - | - | - | - | 1 | 1  | 0  |   |
| Get organization's member info (i.e. role)                                    | 0 | 1 | - | - | - | - | - | - | 1 | 1  | 1  |   |
| Update organization's member info (i.e. role)                                 | 0 | 0 | - | - | - | - | - | - | 1 | 1  | 0  |   |
| Delete organization's member info (i.e. remove user as organization's member) | 0 | 0 | - | - | - | - | - | - | 1 | 1  | 0  |   |
| List/query public projects                                                    | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1  |   |
| List/query private projects                                                   | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 0  |   |
| Update project's info                                                         | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1  | 0  |   |
| Create a project                                                              | 0 | 1 | - | - | - | - | - | - | 1 | 1  | 0  |   |
| Delete project                                                                | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1  | 0  |   |
| Add deltafile                                                                 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1  | 0  |   |
| List project's deltafiles                                                     | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1  | 0  |   |
| Get deltafile's status                                                        | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1  | 0  |   |
| List project's files (qfieldsync)                                             | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 0  |   |
| Download project's files (qfieldsync)                                         | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 0  |   |
| Upload project's files (qfieldsync)                                           | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1  | 0  |   |
| Delete project's files (qfieldsync)                                           | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1  | 0  |   |
| List project's files (qfield)                                                 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 0  |   |
| Download project's files (qfield)                                             | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 0  |   |
| List users and organizations                                                  | 0 | 1 | - | - | - | - | - | - | - | -  | -  |   |
| Get user's public informations                                                | 0 | 1 | - | - | - | - | - | - | - | -  | -  |   |
| Get user's detailed informations                                              | 0 | 0 | - | - | - | - | - | - | 1 | 1  | 0  |   |
| Update user's informations                                                    | 0 | 0 | 1 | - | - | - | - | - | 0 | 0  | 0  |   |
| Delete user                                                                   | 0 | 0 | 1 | - | - | - | - | - | 0 | 0  | 0  |   |
| Get API status                                                                | 1 | 1 | - | - | - | - | - | - | - | -  | -  |   |


## Roles

### ProjectCollaborator

A collaborator of an normal user project can only be reporter or
reader. Editor or manager can only be set to an organization's project.

#### Roles

A higher role always include also the lower ones

| Name     | Description                                                                                           |
|----------|-------------------------------------------------------------------------------------------------------|
| admin    | Rename or delete the project. The same rights as the owner of the project, except ownership transfer. |
| manager  | Can add or remove collaborators.                                                                      |
| editor   | Can edit data                                                                                         |
| reporter | Can only insert data (no update nor delete).                                                          |
| reader   | Can read data.                                                                                        |


### OrganizationMember

#### Roles

A higher role always include also the lower ones

| Name   | Description                                                        |
|--------|--------------------------------------------------------------------|
| admin  | She can add and remove members and create project                  |
| member | (difference compared to an other user is for billing reasons only) |
