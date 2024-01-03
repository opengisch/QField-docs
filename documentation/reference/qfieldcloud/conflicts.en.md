---
title: Manage Conflicts
tx_slug: documentation_reference_qfieldcloud_manage_conflicts
---

## Understanding Conflicts in Data Synchronization

Conflicts occur when any of these conditions is met:

1) distinct users set the same attribute on the same feature to different values, and the second patch of changes arrives before the first is applied to the project;
2) a primary key is employed twice.
Preventing, mitigating and resolving conflicts is crucial to maintaining data integrity in a healthy QGIS project. Here are some tips and tricks to do just that.

### How to Avoid Conflicts?

1. **Unique "fid" Serial Numbers:**
   - When creating a feature, it is recommended to assign a unique "fid" serial number to each feature in the layers.
   - Use the expression "epoch(now())" (without the double quote) in the "fid" to generate a unique identifier per millisecond, reducing the possibility of duplicate "fid" numbers.

2. **Planning and Designation:**
   - For updating existing features based on field conditions, plan and designate the features each user will update.
   - Users should avoid changing the "fid" or identifier numbers.

### How to Resolve Conflicts?

- By default, QFieldCloud overwrites conflicts using a _last wins_ policy (the latest patch of changes to the attribute(s) involved in the conflict replaces all earlier patches of changes to these attributes). Alternatively, admins can set a project's conflict resolution policy to _manual_. Doing so will require the project manager to manually resolve conflicts, picking those to be applied to the project.

- When dealing with delta conflicts:
   - Navigate to the DELTAS section.
   - Filter the deltas with the "Not_applied" status.
   - For each conflicted delta, select it and set the status to "Set status pending" from the "Action" dropdown menu, then press "Go."
   - Check the details of changes in the conflict and click "APPLY DELTA" at the end of the page.
   - Refer to our official documentation [Delta apply](https://docs.qfield.org/reference/qfieldcloud/jobs/#delta-apply-delta_apply-job) for additional guidance.
