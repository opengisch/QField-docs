---
title: Secrets
tx_slug: documentation_reference_qfieldcloud_secrets
---

# Secrets

Secrets are project settings that are securely stored in an encrypted way.
Jobs will automatically have access to the project's secrets, allowing for secure connections to external services without exposing credentials in your project files.

## Types of Secrets

There are two types of secrets you can create in QFieldCloud:

- **Environment variables:** These will be available to QGIS as environment variables while your project jobs are running. You need to provide a name (capitals only) and a value.

- **pg_service configurations:** This allows you to add a PostgreSQL/PostGIS connection as defined in a `pg_service.conf` configuration file.

!![Project secret page after pressing the **Add a new secret** button.](../../assets/images/secrets.png)

!!! warning
    QFieldCloud makes sure your credentials are stored in a secured and encrypted manner. Nevertheless, we advice our users to use roles with the least privileges in shared environments to prevent potential leakage.
    Also note all users with upload file permissions can potentially access the values of those credentials too.

## Secret Levels and Precedence

To provide granular control over data access, secrets in QFieldCloud can be defined at three different hierarchical levels. When a job runs, QFieldCloud will use the most specific secret available according to the following order of precedence:

1. **User-Assigned Secret (Highest Precedence):** A secret defined within a project and assigned to a specific user. This is the most specific level and overrides all others for that user.

2. **Project-Level Secret:** A general secret defined for a specific project. It applies to all project members unless a user-assigned secret is present.

3. **Organization-Level Secret (Lowest Precedence):** A secret defined at the organization level. It is used as a fallback for all projects within the organization that require it, provided no project or user-level secret has been set.

This hierarchical system allows an administrator to set a general, low-privilege database role at the organization level, while assigning more privileged roles for specific projects or trusted individual users.

## Adding a Secret

The process involves navigating to the correct context (Organization or Project), adding a new secret, and storing its contents.

You can add secrets at the following levels:

- **Organization Level:** Navigate to your organization's settings and select the **Secrets** tab. Secrets added here will be available to all projects within the organization unless overridden.

- **Project Level:** Navigate to your project's settings and select the **Secrets** tab. Secrets added here will override any organization-level secrets with the same name.

- **User-Assigned Level:** Within a project's **Secrets** tab, you can add a new secret and explicitly assign it to a specific project member.
This provides the highest level of precedence.

!!! note
    Once added, a secret can only be removed, but cannot be edited.

## pg_service configuration

Adding a PostgreSQL/PostGIS connection as defined in `pg_service.conf` configuration file. The "Advanced editor" allows to paste the `pg_service.conf` file contents directly. If you use multiple service definitions, you should add multiple secrets for each of them.

!!! note
    QFieldCloud secrets are available only during project's job runs, which allows you to configure your PostgreSQL layers as "Offline editing". You **cannot** use QFieldCloud secrets to distribute `pg_service.conf` files across devices. For security reasons, you have to do this manually. You can read [how to configuring QField to use a `pg_service.conf`](../../how-to/pg-service.md) file.

To add a PostgreSQL service you can use either the simple visual editor, or directly edit the service configuration as plain text.

- service name
- database name
- database user
- database password
- database host
- database port
- database SSL connection

For other service settings you can use the **Add extra pgservice field** button to add pairs of settings and their values. Alternatively, you can edit the service configuration directly as plain text.

!![Adding a PostgreSQL service - Simple editor.](../../assets/images/secrets-pgservice-simple.png)

The advanced configuration allows you to directly edit the settings as plain text. This is convenient in cases you want to copy and paste your settings directly from a `pg_service.conf` file.

!![Adding a PostgreSQL service - Advanced editor.](../../assets/images/secrets-pgservice-advanced.png)

## Use Case: Verifying Secret Precedence with PostgreSQL

This example demonstrates how to set up and verify the secret hierarchy. By creating features in QField, we can confirm the feature's provenance by checking which PostgreSQL user role was used for its creation, validating that the correct secret was applied at each level.

!!! note
    The following steps are a case example that can be adapted to your organization's requirements.

### Part 1: PostgreSQL Database Configuration

First, we'll configure the database, define user roles, and set up a table with an automated trigger.

#### 1. Database and Extension Instantiation

Create a new database and enable the necessary `postgis` and `uuid-ossp` extensions.

```sql
-- Create a new database with a specified name, owner, and encoding.
CREATE DATABASE db-og-secrets OWNER qfield ENCODING 'UTF8';

-- Connect to the newly created database.
\c db-og-secrets

-- Install the required extensions if they do not already exist.
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

#### 2. Establishment of Roles

Create three distinct user roles to simulate the tiered permission structure that QFieldCloud secrets will manage.

```sql
-- Create three roles, each with login privileges and an assigned password.
CREATE ROLE ninja_org LOGIN PASSWORD 'your_strong_password_for_org';
CREATE ROLE ninja_project LOGIN PASSWORD 'your_strong_password_for_project';
CREATE ROLE ninja_user LOGIN PASSWORD 'strong_password_for_user_001';
```

#### 3. Schema and Table Definition

Create a schema and a table for point geometries. The table will include a `pg_user` field to automatically record which role was responsible for the data insertion.

```sql
-- Create a schema named 'ninja' if it does not already exist.
CREATE SCHEMA IF NOT EXISTS ninja;

-- Create a table within the 'ninja' schema with the specified columns.
CREATE TABLE IF NOT EXISTS ninja.ninja_point (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  pg_user TEXT,
  some_value TEXT NOT NULL,
  geom GEOMETRY(POINT, 4326)
);
```

#### 4. Implementation of an Automated User-Attribution Trigger

This trigger automatically populates the `pg_user` field with the identifier of the `current_user` whenever a record is inserted or updated.

```sql
-- Define a trigger function to update the pg_user field.
BEGIN;
SET LOCAL SEARCH_PATH TO ninja, public;

CREATE OR REPLACE FUNCTION update_pg_user() RETURNS TRIGGER AS $$
BEGIN
  NEW.pg_user := current_user;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SET search_path FROM CURRENT;

COMMIT;

-- Assign the trigger to the ninja_point table for INSERT or UPDATE events.
BEGIN;
SET LOCAL SEARCH_PATH TO ninja, public;

DROP TRIGGER IF EXISTS trg_ninja_point_update_pg_user ON ninja.ninja_point;

CREATE TRIGGER trg_ninja_point_update_pg_user
  BEFORE INSERT OR UPDATE ON ninja_point
  FOR EACH ROW EXECUTE FUNCTION update_pg_user();

COMMIT;
```

#### 5. Permission Granting

Grant the necessary permissions to the three roles.

```sql
-- Grant usage and data manipulation privileges on the schema and its tables.
GRANT USAGE ON SCHEMA ninja TO ninja_org, ninja_project, ninja_user;
GRANT SELECT, REFERENCES, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA ninja
  TO ninja_org, ninja_project, ninja_user;
```

### Part 2: QFieldCloud and QGIS Project Configuration

Now, configure your QGIS project to use the PostgreSQL service connection and set the secrets at different levels in QFieldCloud.

#### Scenario 1: Organization-Level Secret Application

1. **Secret Instantiation:** In the QFieldCloud web interface, navigate to your organization's settings -> **Secrets** tab. Add a new `pg_service` secret using the credentials for the **`ninja_org`** role.

2. **Verification:** After configuring your QGIS project to use this service, create a new feature in the `ninja_point` layer from QField. When you synchronize the data, the `pg_user` attribute for the new feature is expected to be **`ninja_org`**.

#### Scenario 2: Project-Level Secret Application (Precedence over Organization)

1. **Secret Instantiation:** Navigate to the project's settings in QFieldCloud and go to the **Secrets** tab. Add a new `pg_service` secret with the same service name as the organization-level one, but this time use the credentials for the **`ninja_project`** role.

2. **Verification:** Create another feature from QField. The `pg_user` attribute for this new feature is expected to be **`ninja_project`**, demonstrating that the project-level secret correctly superseded the organization-level one.

#### Scenario 3: User-Level Secret Application (Highest Precedence)

1. **Secret Instantiation:** Within the project's settings -> **Secrets** tab on QFieldCloud, add a new `pg_service` secret. Use the credentials for the **`ninja_user`** role and explicitly assign this secret to your user account.

2. **Verification:** Create a final feature from QField. The `pg_user` attribute for this feature is expected to be **`ninja_user`**, confirming that a user-assigned secret holds the highest level of precedence in the hierarchy.

## Environment variable

Environment variables will be available to QGIS while your project jobs are running.

You need to fill in the environment variable name (capitals only) and the environment variable value as free text.

!![Adding an environment variable.](../../assets/images/secrets-envvar.png)
