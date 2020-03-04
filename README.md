# CMPE 492 - Senior Project
> - Ahmet Gedemenli
> - Advisor: Fatma Başak Aydemir
## RESTful Spring Initializr
**Aim:** Generate RESTful Spring Boot applications with RESTful endpoints, services and customizations.

**Motivation:** Get rid of repetitive coding effort for web service initializations.

* Spring initializr will be used for creating an empty project with just basic Apache Maven dependencies.
* User will run the project with a txt file given as input which indicates user's design choices such as endpoints with REST methods, database url and credentials, entities with fields, codestyle preferences like indentation with two or four spaces and `if(a==b){` or `if(a == b) {` etc. and of course project name and basic information.
* All the initial coding will be done by the project and the user will be able to start implementing complex features and business logics necessary for the created project.

##### Additional Notes
* Exceptions and even exception handlers may be possible to be generated likewise. Will think about that.
* Database connection is problem that needs to be focused. Even the syntax differences between database engines is a problem. Will figure it out.
* Probably more Apache Maven dependencies will be required than the ones that Spring initializr defaultly provides, will hard-code them.
* Codestyle preferences will be the second top priority after the basic functionalities, will be trying to customize as much as possible.

### Requirements
**Functional Requirements**
 * 1 . Users shall be able to provide an input file in txt format.
   * 1.1. The input file shall contain project entities with their fields and required CRUD endpoints.
   * 1.2. The input file shall contain codestyle customizations such as indentation and spaces.
 * 2 . System shall parse the input file and create the infrastructure accordingly.
 * 3 . System shall download the project template from [Spring Initializr](https://start.spring.io/)
 * 4 . System shall generate Java classes for basic CRUD endpoints.
   * 4.1. The endpoints should be described in the input file with Http verbs.
 * 5 . System shall generate Java classes for basic CRUD services.
 * 6 . System shall generate SQL queries for basic CRUD operations.
 * 7 . System shall generate SQL queries for creating database tables.
**Non-Functional Requirements**
 * 1 . System shall report briefly in any case of error or wrong input.
 * 2 . System shall create the project in at most 5 seconds.
 * 3 . The input file shall be as simple and user-friendly as possible.
