---
title: 5GASP Approach
---


## The 5GASP DevOps experimentation and certification readiness lifecycle

To accomplish our objectives, we propose the development of an experimentation and "certification-ready" environment based on the knowledge gathered by partners in previous  successful projects such as 5GinFIRE and currently running projects such as 5GMOBIX, 5G EVE and 5GVINNI.

The 5GASP approach defines the following functionalities and services, mostly designed and developed in WP2, WP3, WP5 and WP6:
* **NetApp onboarding and Experiment Management UI**: The Experimenter facing services, in terms of a centralized NetApps experimentation portal, that allows to manage tenant’s NetApps, trigger and monitor the experimentation lifecycle.
* **5GASP Experimentation APIs service**: The backend service services that exposes standardized OpenAPIs for providing programmatic access to the lifecycle and to the internal NetApp catalogue. This catalogue will contain various NetApps versions and candidate NetApps for publishing.
* **NetApp model transformation service**: This service will automatically translate and enhance the NetApp archive model and embedded entities for the target facility NFV Orchestrator, depending on the defined model (YANG or TOSCA).
* **Issue Management**: A generic service, that notifies all the related stakeholders (NetApp tenants, facility and platform owners) for any issues during the operation and testing lifecycle.
* **Central Logging**: A central logging service which gathers timestamped information from various services across the platform providing means of issue traceability.
* **5GASP Service Orchestrator**: A service orchestrator for supporting deployment decisions to facilities, solving inter-dependencies and co-ordination between the various services.
* **MANO Client API (SOL005) service**: A service that interfaces the operation and experimentation services with the NFV orchestrators of the facilities. The service will implement the ETSI NFV SOL005 interface found in compliant NFVOs.
* **5GASP facilities**: The 5GASP facilities, tailored to support the specificities of NetApps and acting as their hosts for testing. Each facility will host the following services:
  * **Testcase Execution Engine**: An engine capable of performing automated test, based on defined test scripts, against the installed NetApp in the facility. 
  * **Monitoring repository per facility**: A monitoring service in the facility, providing telemetry data from various resources of the facility (e.g. the NFVI, the NFVO, the 5G System, etc).
* **CI/CD service**: A service based on Open source solutions which will support CI/CD pipelines and coordinate the execution of test by properly interacting with the Service Orchestrator and the Test Execution Engine of each facility.
* **5GASP NetAppStore**: The 5GASP open marketplace which will contain validated and tested NetApps for every specified vertical.


The following Figure illustrates the 5GASP approach on DevOps experimentation and certification readiness Lifecyle.


![]({{ site.url }}/assets/img/5gasp_architecture.png)


The experimentation and certification-readiness Lifecyle is envisaged and will be realized by the following interactions:

1.	The NetApp developer (5GASP tenant), via the **NetApp onboarding and Experiment Management UI** Onboards the NetApp under test to the NetApp Catalogue in **5GASP Experimentation APIs service**.
2.	A NetApp Model enhancement follows by the **NetApp model transformation service**.
3.	The NetApp CI/CD main testing pipeline is triggered to the **CI/CD service**.
4.	A Service Choreography follows between the **CI/CD service** and NetApp **Service Orchestrator** to properly manage the deployment to target facilities.
5.	The **Service Orchestrator** resolves dependencies and Onboard NetApps to target facilities NFVO repositories
6.	The Onboarding & Lifecycle Management towards the facilities is realized via the **MANO Client API (SOL005) service**.
7.	The **CI/CD service** from information exchanged with the **Service Orchestrator** execute tests via the facility’s **Testcase Execution Engine**.
8.	During testing **Monitoring** takes place.
9.	After testing execution, Testcases results from facility are available.
10.	Testcases results are made available to **CI/CD service** for assessment. 
11.	CI/CD service makes available Testcases results to **5GASP Experimentation Service** so 5GASP tenants are aware for the testing results and assessment.
12.	If the NetApp is passed successfully the full lifecycle and all the defined testing pipelines is Publish to **5GASP NetAppStore**.

## The 5GASP NetAppStore/NetAppCommunity

To support both business and development, a platform which includes two complementary portals named NetAppStore and NetAppCommunity will be developed. The NetAppStore will support business around NetApps, Network Functions, and Network Services. It will provide a public registry of SMEs and their reusable products: NetApps, Network Functions, and Network Services. Any useful information and documentation for SMEs will be available at this portal as well. The NetAppCommunity will support developers of NetApps, Network Functions, and Network Services. It will provide developers’ forum, technical documentation, user guides, and other related information for developers, operators, verticals, etc
