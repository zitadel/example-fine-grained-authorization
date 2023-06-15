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

3. Go to **Roles** (from the left menu) and click **New** to add new roles. 

<img
    src="screenshots/10 - Create Roles.png"
    width="75%"
    alt="Project settings"
/>

4. Enter the roles **editor** and **journalist** as shown below and click **Save**. 

<img
    src="screenshots/11 - Create Roles.png"
    width="75%"
    alt="Create roles"
/>

5. You will now see the created roles. 

<img
    src="screenshots/12 - Create Roles.png"
    width="75%"
    alt="Create roles"
/>

### 3/ Create Users in the Newsroom Project

1. Go to the **Users** tab in your organization as shown below and go to the **Service Users** tab. We will be creating service users in this demo. To add a service user, click the **New** button.

<img
    src="screenshots/14 - Create Service User.png"
    width="75%"
    alt="Create service user"
/>

2. Next, add the details of the service user and select **JWT** for **Access Token Type** and click **Create**. 

<img
    src="screenshots/15 - Create Service User 1.png"
    width="75%"
    alt="Create service user"
/>

3.  Click the **Actions** button on the top right corner. Select **Generate Client Secret** from the drop-down menu. 

<img
    src="screenshots/16 - Create Service User and Generate CC.png"
    width="75%"
    alt="Create service user"
/>

4. Copy your Client ID and Client Secret. Click **Close**. 

<img
    src="screenshots/17 - Service user CC.png"
    width="75%"
    alt="Create service user"
/>

5. Now you have a service user, along with their client credentials. 

### 4/ Add Authorizations for the Users

1. Go to **Authorizations**. Click **New**. 

<img
    src="screenshots/19 - Service user authorizations.png"
    width="75%"
    alt="Add authorization"
/>

2. Select the user and the project for which the authorization must be created. Click **Continue**. 

<img
    src="screenshots/20 - SU auhorization.png"
    width="75%"
    alt="Add authorization"
/>

3. You can select a role here. Select the role **journalist** for the current user. Click **Save**. 

<img
    src="screenshots/21 - SU authorization .png"
    width="75%"
    alt="Add authorization"
/>

4. You can see the service user **Lois Lane** now has the role **journalist** in the **Newsroom** project. 

<img
    src="screenshots/22 - SU authorization.png"
    width="75%"
    alt="Add authorization"
/>

### 5/ Add Metadata to the Users

Now, let's add metadata to the user profile to indicate their level of seniority. Use 'experience_level' as the key, and for its value, choose from 'junior', 'intermediate', or 'senior'. Although we can typically assume this metadata is set through an API call made by the HR application, for simplicity and ease of understanding, we will set the metadata directly in the console.

<img
    src="screenshots/23 - SU metadata.png"
    width="75%"
    alt="Add metadata"
/>

<img
    src="screenshots/24 - SU metadata.png"
    width="75%"
    alt="Add metadata"
/>

<img
    src="screenshots/25 - SU metadata.png"
    width="75%"
    alt="Add metadata"
/>

<img
    src="screenshots/26 - Users and roles list.png"
    width="75%"
    alt="Add metadata"
/>

