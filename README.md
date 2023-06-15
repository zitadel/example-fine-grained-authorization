# example-fine-grained-authorization
Leverage actions, custom metadata, and claims for attribute-based access control

## Set up ZITADEL

### 1/ Create Media House Organization, Newsroom Project and Article API

1. Create the Media House organization and go to **Projects** and create a new project called Newsroom.

<img
    src="screenshots/1 - New Org.png"
    width="75%"
    alt="Create org, project and API app"
/>

2. In the Newsroom project, click the **New** button to create a new application. 

<img
    src="screenshots/2 - New Project.png"
    width="75%"
    alt="Create org, project and API app"
/>

3. Add a name and select type **API**.

<img
    src="screenshots/3 - New API.png"
    width="75%"
    alt="Create org, project and API app"
/>

4. Select **Basic** as the authentication method and click **Continue**. 

<img
    src="screenshots/4 - New API.png"
    width="75%"
    alt="Create org, project and API app"
/>

5. Now review your configuration and click **Create**. 
 
<img
    src="screenshots/5 - New API.png"
    width="75%"
    alt="Register the API"
/>

6. You will now see the API’s **Client ID** and the **Client Secret**. Copy them and save them. Click **Close**. 

<img
    src="screenshots/7 - API Client ID and Secret.png"
    width="75%"
    alt="Create org, project and API app"
/>

7. When you click **URLs** on the left, you will see the relevant OIDC URLs. Note down the **issuer** URL, **token_endpoint** and **introspection_endpoint**.  

<img
    src="screenshots/8 - URLs.png"
    width="75%"
    alt="Create org, project and API app"
/>

### 2/ Create Roles in the Newsroom Project

1. Also note down the **Resource ID** of your project (go to the project and copy the Resource ID)  

<img
    src="screenshots/9 - Create Roles.png"
    width="75%"
    alt="Project settings"
/>

2. Select the **Assert Roles on Authentication** checkbox on the project dashboard and click **Save**.

<img
    src="screenshots/2.1 - Tick the box.png"
    width="75%"
    alt="Project settings"
/>

3.

<img
    src="screenshots/10 - Create Roles.png"
    width="75%"
    alt="Project settings"
/>

<img
    src="screenshots/11 - Create Roles.png"
    width="75%"
    alt="Create roles"
/>

<img
    src="screenshots/12 - Create Roles.png"
    width="75%"
    alt="Create roles"
/>



