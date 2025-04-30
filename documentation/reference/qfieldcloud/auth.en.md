---
title: Authentication
tx_slug: documentation_reference_qfieldcloud_auth
---

# Authentication

QFieldCloud and QField / QFieldSync clients allow authentication using regular username and password, or, if configured, **OpenID Connect** with a third-party identity provider.

## OpenID Connect authentication

[OpenID Connect](https://openid.net/developers/how-connect-works/) (OIDC) is an industry standard authentication protocol on top of [OAuth2](https://oauth.net/2/) that allows to delegate authentication to an identity provider (IDP) such as Google, Microsoft, or any other OpenID Connect compliant provider. This allows users to log in to QFieldCloud using their existing accounts with these providers, without needing to create a separate account for QFieldCloud.

OIDC can be used directly for signing up with QFieldCloud, or for signing in to an existing QFieldCloud account (matched via verified email address).

Here is a sequence diagram of how a third-party login happens in QFieldCloud (in the browser):

```mermaid
sequenceDiagram
    autonumber

    actor User as User (Browser)
    participant QFC as QFieldCloud

    User ->> QFC: Access login page
    QFC -->> User: Display login form with configured third-party login buttons

    User ->> QFC: Click third-party login button

    QFC -->> User: Redirect to IDP for login
    create participant IDP as Identity Provider
    User ->> IDP: Follow redirect to IDP login page
    IDP -->> User: Display IDP's login page

    User ->> IDP: Authenticate using IDP credentials

    IDP -->> User: Redirect to QFieldCloud callback URL with authorization code
    User ->>+ QFC: Hand authorization code to QFieldCloud
    QFC ->> IDP: Exchange authorization code for access token and ID token
    IDP -->> QFC: Return access token + ID token

    Note over QFC: Validate ID token signature

    QFC ->> IDP: Request user profile information
    destroy IDP
    IDP -->> QFC: Return user profile information

    alt If user does not already have a QFieldCloud account
    note over QFC: QFieldCloud account is created using IDP profile infos
    end

    QFC -->>- User: Log user in (establish session)
```

Here is a sequence diagram of how third-party authentication happens in QField and QFieldSync:

```mermaid
sequenceDiagram
    autonumber

    participant IDP as Identity Provider
    actor User
    participant QF as QField / QFieldSync
    participant QFC as QFieldCloud

    User ->>+ QF: Open the QFieldCloud login dialog

    QF ->> QFC: Ask for configured third-party ID providers
    QFC -->> QF: Answer with the list of configured third-party ID providers
    QF -->>- User: Display a button for each third-party ID provider

    User ->>+ QF: Click on 'Login with XYZ' provider button

    Note over QF: A QgsAuthMethodConfig of type OAuth2 is created<br/>QGIS auth manager recognizes that the user is not authenticated yet<br/> QGIS auth manager then redirects to the IDP for authenticating the user

    QF ->>+ IDP: Redirect to IDP for login
    IDP -->> User: Display IDP's login form in a browser
    User ->> IDP: Log in using IDP's credentials in the browser
    IDP ->>- QF: Answer with auth details and an id_token token

    QF ->>+ QFC: Ask for current user's informations
    Note over QF,QFC: The id_token provided by IDP is in in the X-QFC-ID-Token HTTP header<br/>The IDP provider type (e.g. "google") is in the X-QFC-IDP-ID header

    QFC -->>- QF: Answer with user information (username, avatar, etc.)
    QF -->>- User: User is logged in and authenticated

    loop send HTTP regular requests (e.g. file synchronization)
        QF ->> QFC: Send a request (e.g. file Download/Upload)
        Note over QF,QFC: The id_token provided by IDP is in in the X-QFC-ID-Token HTTP header<br/>The IDP provider type (e.g. "google") is in the X-QFC-IDP-ID header
        QFC -->> QF: Reply to the request
    end

    loop refresh token regularly
        QF ->> IDP: Ask for a new token
        IDP -->> QF: Send a refreshed token
    end
```
