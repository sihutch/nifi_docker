# NiFi docker

This is a simple docker project that sets up both NiFi and NiFi registry along with some test users.
The users are simply stored in a file using the [nifi-file-identity-provider-bundle](https://github.com/BatchIQ/nifi-file-identity-provider-bundle) which avoids the need for ldap.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Docker and Docker Compose installed

### Installing

Clone the project

Run: `docker-compose up -d`

You can tail the logs with: `docker-compose logs -f -t`

### Usage

The setup creates the following:

* Three users with the following username:passwords

  * admin:admin

  * user1:user1

  * user2:user2

* A single Test Bucket in NiFi registry
* Configures NiFi to use NiFi registry_config
* Gives all users access policies to the root process group

Access NiFi at: https://localhost:8443 - The cert is self-signed so you will have to accept it in your browser.

Access NiFi registry at: http://localhost:18080 - Registry is not secured.
