# Salesforce API for watsonx Orchestrate

This simple Python API provides basic fetch operations against Salesforce.  These are used to create demo skills 
for use with watsonx Orchestrate (wxo), the skill endpoints are defined in the OpenAPI file. The endpoints simplfy the returned 
data and make it easier to consume directly in wxo. 

To host this API and run it against your SF instance you will need to provide the following environment variables.

* TOKEN_URL : Where to fetch the SF bearer token for your instance.
* CLIENT_ID : The client ID configured for the 'connected app' in your SF instance.
* CLIENT_SECRET: The client  secret for the 'connected app' in your SF instance.
* QUERY_URL: The query URL endpoint for your SF instance.

Note, you will also need to configure your SF instance for OAUTH and whitelist the wxo domain... 