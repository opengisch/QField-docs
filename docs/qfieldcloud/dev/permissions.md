# Permissions


<a id="org78d6e71"></a>

## Actors

1.  Unregistered user
2.  Simple registered user, neither collaborator of the concerned project nor member of the concerned organization nor the concerned user
3.  Project owner of the concerned project, the conerned user, but not collaborator nor organization member
4.  Project collaborator role admin of the concerned project
5.  Project collaborator role manager of the concerned project
6.  Project collaborator role editor of the concerned project
7.  Project collaborator role reporter of the concerned project
8.  Project collaborator role reader of the concerned project
9.  Organization owner of the concerned organization or the organization that owns the concerned project or to which belongs the user
10. Organizaton member role admin of the concerned organization or the organization that owns the concerned project or to which belongs the user
11. Organization member role member of the concerned organization or the organization that owns the concerned project or to which belongs the user


<a id="orgc74e255"></a>

## Actions

`0` -> Not allowed

`1` -> Allowed

`-` -> Irrelevant

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Action</th>
<th scope="col" class="org-right">1</th>
<th scope="col" class="org-right">2</th>
<th scope="col" class="org-right">3</th>
<th scope="col" class="org-right">4</th>
<th scope="col" class="org-right">5</th>
<th scope="col" class="org-right">6</th>
<th scope="col" class="org-right">7</th>
<th scope="col" class="org-right">8</th>
<th scope="col" class="org-right">9</th>
<th scope="col" class="org-right">10</th>
<th scope="col" class="org-right">11</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">List/query project's collaborator roles</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
</tr>


<tr>
<td class="org-left">Create project's collaborator (i.e. define new collaborator)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Update project's collaborator's info (i.e. role)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Delete project's collaborator (i.e. remove user as collaborator)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">List organization's members</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">Create organization's member (i.e. define a new member)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Get organization's member info (i.e. role)</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">Update organization's member info (i.e. role)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Delete organization's member info (i.e. remove user as organization's member)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">List/query public projects</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">List/query private projects</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Update project's info</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Create a project</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Delete project</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Add deltafile</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">List project's deltafiles</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Get deltafile's status</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">List project's files (qfieldsync)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Download project's files (qfieldsync)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Upload project's files (qfieldsync)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Delete project's files (qfieldsync)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">List project's files (qfield)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Download project's files (qfield)</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">List users and organizations</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
</tr>


<tr>
<td class="org-left">Get user's public informations</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
</tr>


<tr>
<td class="org-left">Get user's detailed informations</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Update user's informations</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Delete user</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
<td class="org-right">0</td>
</tr>


<tr>
<td class="org-left">Get API status</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
<td class="org-right">-</td>
</tr>
</tbody>
</table>


<a id="org870aec3"></a>

## Roles


<a id="orgc2a25e0"></a>

### ProjectCollaborator

A collaborator of an normal user project can only be reporter or
reader. Editor or manager can only be set to an organization's project.

1.  Roles

    A higher role always include also the lowest ones
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">admin</td>
    <td class="org-left">The owner of a project is always admin of the project. He can add and remove collaborators</td>
    </tr>
    
    
    <tr>
    <td class="org-left">manager</td>
    <td class="org-left">Can add or remove collaborators</td>
    </tr>
    
    
    <tr>
    <td class="org-left">editor</td>
    <td class="org-left">Can edit data</td>
    </tr>
    
    
    <tr>
    <td class="org-left">reporter</td>
    <td class="org-left">Can only insert data (no update nor delete). (Don't have to be a collaborator?)</td>
    </tr>
    
    
    <tr>
    <td class="org-left">reader</td>
    <td class="org-left">Can read data. (Don't have to be a collaborator?)</td>
    </tr>
    </tbody>
    </table>


<a id="org7ba1ec4"></a>

### OrganizationMember

1.  Roles

    A higher role always include also the lowest ones
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Name</th>
    <th scope="col" class="org-left">Description</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">admin</td>
    <td class="org-left">She can add and remove members and create project</td>
    </tr>
    
    
    <tr>
    <td class="org-left">member</td>
    <td class="org-left">(difference compared to an other user is for billing reasons only)</td>
    </tr>
    </tbody>
    </table>

