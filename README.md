# example-fine-grained-authorization
Leverage actions, custom metadata, and claims for attribute-based access control

## ToC
1. [Set up ZITADEL](#1)
 - [1/ Create Media House Organization, Newsroom Project and Article API](#1.1)
 - [2/ Create Roles in the Newsroom Project](#1.2)
 - [3/ Create Users in the Newsroom Project](#1.3)
 - [4/ Add Authorizations for the Users](#1.4)
 - [5/ Add Metadata to the Users](#1.5)
 - [6/ Create an Action to Capture Role and Metadata in Custom Claim](#1.6)
2. [Set up the API Project](#2)


## Set up ZITADEL <a name="1"></a>

### 1/ Create Media House Organization, Newsroom Project and Article API <a name="1.1"></a>

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

### 2/ Create Roles in the Newsroom Project <a name="1.2"></a>

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

### 3/ Create Users in the Newsroom Project <a name="1.3"></a>

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

### 4/ Add Authorizations for the Users <a name="1.4"></a>

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

### 5/ Add Metadata to the Users <a name="1.5"></a>

Now, let's add metadata to the user profile to indicate their level of seniority. Use 'experience_level' as the key, and for its value, choose from 'junior', 'intermediate', or 'senior'. Although we can typically assume this metadata is set through an API call made by the HR application, for simplicity and ease of understanding, we will set the metadata directly in the console.

1. Go to **Metadata**. Click **Edit**.

<img
    src="screenshots/23 - SU metadata.png"
    width="75%"
    alt="Add metadata"
/>

2. Provide **experience_level** as the key and **senior** as the value. Click the save icon and click the **Close** button. 

<img
    src="screenshots/24 - SU metadata.png"
    width="75%"
    alt="Add metadata"
/>

3. The user now has the required metadata associated with their account. 

<img
    src="screenshots/25 - SU metadata.png"
    width="75%"
    alt="Add metadata"
/>

You can also add a few more service users with different roles and experience_levels (using metadata) to test the demo using the previous steps. 

<img
    src="screenshots/26 - Users and roles list.png"
    width="75%"
    alt="Add metadata"
/>

### 6/ Create an Action to Capture Role and Metadata in Custom Claim <a name="1.6"></a>

1. Click on **Actions**. Click **New** to create a new action.

<img
    src="screenshots/27 - Action.png"
    width="75%"
    alt="Add action"
/>

2. In the **Create an Action** section, give the action the same name as the function name, i.e., assignRoleAndExperienceClaims. In the script field, copy/paste the code in [assignRoleAndExperienceClaims.js](https://github.com/zitadel/example-fine-grained-authorization/blob/main/zitadel_actions/assignRoleAndExperienceClaims.js). Click **Add**.

<img
    src="screenshots/28 - Action.png"
    width="75%"
    alt="Add action"
/>

3. The **assignRoleAndExperienceClaims** will now be listed as an action. 

<img
    src="screenshots/29 - Action.png"
    width="75%"
    alt="Add action"
/>

4. Next, we must select a **Flow Type**. Go to the **Flows** section below. Select **Complement Token** from the dropdown.

<img
    src="screenshots/30 - Action.png"
    width="75%"
    alt="Add action"
/>

5. Now, you must choose a trigger. Click **Add trigger**. Select **Pre access token creation** as the trigger type and select **assignRoleAndExperienceClaims** as the associated action.

<img
    src="screenshots/31 - Action.png"
    width="75%"
    alt="Add action"
/>


6. And now you will see the trigger listed.

<img
    src="screenshots/32 - Action.png"
    width="75%"
    alt="Add action"
/>

Now, when a user requests an access token, the action will be executed, transforming the user roles and metadata into the required format and adding them as a custom claim to the token. This custom claim can then be used by third-party applications to manage fine-grained user access.

## 2. Set up the API Project <a name="2"></a>

**Clone the Project from GitHub:**

Run the command below to clone the project from this GitHub repository: 
- `git clone https://github.com/zitadel/example-fine-grained-authorization.git`  

**Navigate to the Project Directory:**

After cloning, navigate to the project directory with 
- `cd example-fine-grained-authorization`.

**Setup a Python Environment:**

Ensure you have Python 3 and pip installed. You can check this by running 
- `python --version`
and 
- `pip --version` 

in your terminal. If you don't have Python or pip installed, you will need to install them.

Next, create a new virtual environment for this project by running 
- `python3 -m venv env`.

Activate the environment by running:
- On Windows: `.\env\Scripts\activate`
- On Unix or MacOS: `source env/bin/activate`

After running this command, your terminal should indicate that you are now working inside the env virtual environment.

**Install Dependencies:**

With the terminal at the project directory (the one containing requirements.txt), run 
- `pip3 install -r requirements.txt` 

to install the necessary dependencies.

**Configure Environment Variables:**

The project requires certain environment variables. Fill in the `.env` file with the values we retrieved from ZITADEL.

**Run the Application:**

The Flask API (in [`app.py`](https://github.com/zitadel/example-fine-grained-authorization/blob/main/app.py)) uses JWT tokens and custom claims for fine-grained access control. It checks the custom claim experience_level for the roles `journalist` and `editor` on every request, using this information to decide if the authenticated user can access the requested endpoint. Run the Flask application by executing: 
- `python3 app.py`

If everything is set up correctly, your Flask application should now be running.

This project was developed and tested with Python 3. If you encounter any issues, please ensure you're using a Python 3 interpreter.

## 3. Run and Test the API <a name="3"></a>

### Run the API

1. Ensure you have cloned the repository and installed the necessary dependencies as described earlier.
2. Run the `client_credentials_token_generator.py` script to generate an access token. Open your terminal and navigate to the project directory, then run the script using python3:
- `python3 client_credentials_token_generator.py`
3. If successful, this will print an access token to your terminal. This is the token you'll use to authenticate your requests to the API.
4. If you didn't stat the Flask API earlier, run the API by opening another terminal in the project directory and running:
- `python3 app.py`
5. The API server should be now running and ready to accept requests.

Now you can use cURL or any other HTTP client (like Postman) to make requests to the API. Remember to replace your_access_token in the curl commands with the access token you obtained in step 2.

### Test the API

**Scenario 1: Junior Editor Tries to Edit an Article (Success)**
User with `editor` role and `junior` experience_level tries to call `edit_article` endpoint.

- `curl -H "Authorization: Bearer <your_access_token>" -X POST http://localhost:5000/edit_article`
- Expected Output: `{"message": "Article edited successfully"}`


**Scenario 2: Junior Editor Tries to Publish an Article (Failure)**
User with `editor` role and `junior` experience_level tries to call `publish_article` endpoint.

- `curl -H "Authorization: Bearer <your_access_token>" -X POST http://localhost:5000/publish_article`
- Expected Output: `{"message": "Access denied! \nYou are a junior editor and therefore cannot access publish_article"}`


**Scenario 3: Senior Journalist Tries to Write an Article (Success)**
User with `journalist` role and `senior` experience_level tries to call `write_article` endpoint.

- `curl -H "Authorization: Bearer <your_access_token>" -X POST http://localhost:5000/write_article`
- Expected Output: `{"message": "Article written successfully"}`


**Scenario 4: Junior Journalist Tries to Review Articles (Failure)**
User with `journalist` role and 'junior' experience_level tries to call `review_articles` endpoint.

- `curl -H "Authorization: Bearer <your_access_token>" -X POST http://localhost:5000/review_articles`
- Expected Output: `{"message": "Access denied! \nYou are a junior journalist and therefore cannot access review_articles"}`


**Scenario 5: Senior Editor Tries to Review Articles (Success)**
User with `editor` role and `senior` experience_level tries to access `review_articles` endpoint.

- `curl -H "Authorization: Bearer <your_access_token>" -X POST http://localhost:5000/review_articles`
- Expected Output: `{"message": "Article reviewed successfully"}`


**Scenario 6: Intermediate Journalist Tries to Publish an Article (Success)**
User with `journalist` role and `intermediate` experience_level tries to access `publish_article` endpoint.

- `curl -H "Authorization: Bearer <your_access_token>" -X POST http://localhost:5000/publish_article`
- Expected Output: `{"message": "Article published successfully"}`

