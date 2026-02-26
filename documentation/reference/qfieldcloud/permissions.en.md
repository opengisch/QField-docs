---
title: Permissions
tx_slug: documentation_reference_qfieldcloud_permissions
---

# Permissions

QFieldCloud provides a fine grained access control over projects with the concepts of project collaborators, organization members and organization teams.

## Actors

   1. Unregistered user.
   2. Simple registered user, neither collaborator of the concerned project nor member of the concerned organization nor the concerned user.
   3. Project owner of the concerned project, the concerned user, but not collaborator nor organization member.
   4. Project collaborator role admin of the concerned project.
   5. Project collaborator role manager of the concerned project.
   6. Project collaborator role editor of the concerned project.
   7. Project collaborator role reporter of the concerned project.
   8. Project collaborator role reader of the concerned project.
   9. Organization owner of the concerned organization or the organization that owns the concerned project or to which belongs the user.
   10. Organization member role admin of the concerned organization or the organization that owns the concerned project or to which belongs the user.
   11. Organization member role member of the concerned organization or the organization that owns the concerned project or to which belongs the user.

## Actions

- ❌ Not allowed
- ✅ Allowed
- *‒* Irrelevant

<div class="special_table"></div>
| Action                                                                        | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10  | 11 |   |
|-------------------------------------------------------------------------------|----|----|----|----|----|----|----|----|----|-----|----|---|
| List/query project's collaborator roles                                       | ❌ | ✅ | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  |   |
| Create project's collaborator (i.e. define new collaborator)                  | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |   |
| Update project's collaborator's info (i.e. role)                              | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |   |
| Delete project's collaborator (i.e. remove user as collaborator)              | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |   |
| List organization's members                                                   | ❌ | ✅ | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ✅ | ✅ | ✅ |   |
| Create organization's member (i.e. define a new member)                       | ❌ | ❌ | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ✅ | ✅ | ❌ |   |
| Get organization's member info (i.e. role)                                    | ❌ | ✅ | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ✅ | ✅ | ✅ |   |
| Update organization's member info (i.e. role)                                 | ❌ | ❌ | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ✅ | ✅ | ❌ |   |
| Delete organization's member info (i.e. remove user as organization's member) | ❌ | ❌ | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ✅ | ✅ | ❌ |   |
| List/query public projects                                                    | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |   |
| List/query private projects                                                   | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |   |
| Update project's info                                                         | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |   |
| Create a project                                                              | ❌ | ✅ | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ✅ | ✅ | ❌ |   |
| Delete project                                                                | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |   |
| Add deltafile                                                                 | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |   |
| List project's deltafiles                                                     | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |   |
| Get deltafile's status                                                        | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |   |
| List project's files (qfieldsync)                                             | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |   |
| Download project's files (qfieldsync)                                         | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |   |
| Upload project's files (qfieldsync)                                           | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |   |
| Delete project's files (qfieldsync)                                           | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |   |
| List project's files (qfield)                                                 | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |   |
| Download project's files (qfield)                                             | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |   |
| Read synced features from layers in the project on QField                     | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |   |
| Create synced features from layers in the project on QField                   | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |   |
| Delete synced features from layers in the project on QField                   | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ |   |
| Update synced features from layers in the project on QField                   | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ |   |
| List users and organizations                                                  | ❌ | ✅ | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  |   |
| Get user's public information                                                | ❌ | ✅ | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  |   |
| Get user's detailed information                                              | ❌ | ❌ | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ✅ | ✅ | ❌ |   |
| Update user's information                                                    | ❌ | ❌ | ✅ | ‒  | ‒  | ‒  | ‒  | ‒  | ❌ | ❌ | ❌ |   |
| Delete user                                                                   | ❌ | ❌ | ✅ | ‒  | ‒  | ‒  | ‒  | ‒  | ❌ | ❌ | ❌ |   |
| Get API status                                                                | ✅ | ✅ | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  | ‒  |   |
| Add and remove secrets                                                        | ‒  | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ‒  | ‒  | ‒  |   |

## Roles

### ProjectCollaborator

A collaborator of a normal user project can only be reporter or
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
