---
title: UoP
subtitle: University of Patras	
name: UoP
complete-name: University of Patras
country: Greece

---
# UoP

**The Patras5G facility is an "isolated" Non-public Network for 5G and IoT applications.**

Most of the installed components are offered as Open Source but there are also dedicated components and services to support 5G and IoT scenarios. Numerous partners have deployed their technologies in the Patras 5G /Greece facility, thus creating a unique 5G playground for KPI validation and support on future verticals. 

![Location]({{ site.url }}/assets/img/facilities/upatras/upatras_location.png "Location Overview")


In Patras5G facility site the following tasks are performed:

* Providing 5G standard-conformant components and Core Network infrastructure as extension of the FhG Open5GCore toolkit
* Provide Intracom Telecom mmWave backhaul to link the access to the core network, and Fixed Wireless Access to provide broadband services to the facility
* Integration of FhG Open5GCore with Limemicro SDR platform and the SRS UE and g/eNB
* Enabling the E2E deployment of multiple customized-slices over the whole network – access, transport and core. This will further include the slicing of the IoT devices at the edge of the network.
* Supporting MEC orchestration and mobility management features for the support of interactive mobile streaming edge services.

Our portal is located at: [https://patras5g.eu](https://patras5g.eu)


# Patras5G facility infrastructure: Onboarding and access for Vertical Applications

![Onboarding Overview]({{ site.url }}/assets/img/facilities/upatras/onboarding-overview.png "Onboarding Overview")

**Summary of capabilities**
With our OSS, NFV and experimentation enabled services, like Openslice and Open Source MANO, we enable E2E automated deployment of multiple customized-slices over the whole network – access, transport and core. This further includes the slicing of the IoT devices at the edge of the network. Patras 5G facility is equipped with a cloud platform, able to host core network components, as well as NFV and MEC deployments. The cloud platform offers a total computing power of 300 CPUs and 1TB of RAM and 50 TB of storage. 10GbE NICs DPDK enabled are also available. Patras 5G provides 5G standard-conformant components and Core Network infrastructure and Integration of 5G Core and 5G RAN with our Opensource based NFV platform.  We support various flavors and installations of the 5G System, that are both NSA and SA depending on the scenarios that the customer 
* 	5G Core and EPC solutions that are available and can be orchestrated in the facility:  FhG Open5GCore, AMARISOFT EPC, SRS EPC, NextEPC
* 	5G and 4G RAN: AMARISOFT 5G RAN (Classic boxes), 5G RAN open source radio (Lime, SRS)-700-800MHz, 3.5.-3.8GHz, 4G NB-IoT, LTE-M (FhG NB-IOT core) based on AMARISOFT, Various SDR equipment (ETTUS)
* 	UEs based on Limemicro’s SDR and SRS software, as well as commercial UEs: Mobile phones LG and Samsung, Huawei CPE, Various SDR equipment, a Drone for URLLC testing
* 	Monitoring is available through: Graphana, Prometheus,Netdata while OSM also configure with VNF telemetry support
* 	Patras 5G has mmWave backhaul to link the access to the core network, and Fixed Wireless Access to provide broadband services to the facility from various locations in the region of Patras and beyond. 
* 	GEANT connectivity is also available


Vertical applications can access the Patras 5G Service Catalogue through the Patras Facility site portal: https://patras5g.eu .  Vertical applications can self-manage and onboard their artifacts through our portal or access programmatically available services.
Various artifacts can be managed through the facility portal https://patras5g.eu via standardized TMForum OpenAPIs: Service Catalog,  Service Order and Service Inventory, Partner Management and Users, Service Orchestration, VNFs/NSDs catalogue, NFVO endpoints via OSM NBI, Service and NFV Deployment requests. 

![Openslice Logo Small]({{ site.url }}/assets/img/facilities/upatras/openslice-logo-small.png "Openslice Logo Small")
The Patras Facility site portal is based on Openslice (http://openslice.io) a prototype open source, operations support system. Up is the main contributor of OpenSlice. It supports VNF/NSD onboarding to OpenSourceMANO (OSM) and NSD deployment management. It also supports TMFORUM OpenAPIs regarding Service Catalog Management, Ordering, Resource, etc. Openslice offers the following main functionalities:

* 	Service Catalog Management: A CSP will have the ability to manage the Service Catalog Items, their attributes , organize in categories and decide what to make available to Customers
* 	Services Specifications: A CSP will be able to manage Service Specifications
* 	Service Catalog Exposure: A CSP will be able to expose catalog to customers and related parties
* 	Service Catalog to Service Catalog: Openslice able to consume and provide Service Catalog items to other catalogs
* 	Service Order: The Communication Service Customer will be able to place a Service Order
* 	Service Inventory: The Communication Service and Provider will be able to view deployed Services status

Openslice thus support both APIs for programmable access to the infrastructure as well as a web portal for user friendly access.



# Architecture And Components of Patras5G


![greeksitearch]({{ site.url }}/assets/img/facilities/upatras/upatras_arch.png "greeksitearch")


## Cloud/MANO services

Currently, the Patras5G facility is equipped with a cloud platform offered by the University of Patras, able to host core network components, as well as NFV and MEC deployments. The cloud platform offers a total computing power of 340 CPUs and 1TB of RAM and 30 TB of storage. Five servers with 4x10GbE NICs DPDK enabled.

On top of our cloud hardware, a rich set of state-of-the-art SW tools is already available, which comprises our platform for experimentation called Cloudville. These include OpenStack as the cloud operating system but also a Kubernetes cluster install over Openstack, while OSM (but also OpenBaton via FhG) will be available to allow NSD/VNF deployments.  Prometheus alongside with Grafana are installed for monitoring purposes. At the same time, Elastic search and Kibana are installed and being used to collect and visualize data extracted from IoT devices and sensors.



## Access Network, MEC devices and UE

In Patras/Greece facility there will be 3 Outdoor base stations together with MEC devices at the Patras campus and at the City of Patras placed at properly selected places to facilitate the execution of test plans together with around 6 UEs. UoP together with ICOM will implement and integrate any standardized APIs and services to provide MEC functionality, including the virtualization of edge IoT devices, i.e., IoT Slicing, as a VIM component.

LimeMicro’s hardware will be used for both handset and base station. LimeMicro specialises in field programmable RF (FPRF) transceivers and open source LimeSDR, LimeNET platforms for the next generation of wireless broadband systems.  These products offer an unprecedented level of configurability and will be used in the Patras/Greece to create wireless communication networking equipment using commodity hardware, i.e., x86- based machines that can be programmable and reconfigured to run on any wireless communications frequency and mobile standards from 2G to 5G networks of the future.

SRS will integrate its software suite into the LimeMicro SDR hardware platform as well as interworking with the Fraunhofer open5Gcore will be assured.  SRS will provide a set of selected 5G NR features for srsLTE that will be available for KPI validation within the project. SRS will extend their code base for both UE and (g/e)NB to support the 5G NR scalable numerology for configurable subcarrier spacings, integrate the new channel coding, and higher order modulation types supported by 5G. This work will serve as a proof-of-concept and feasibility study of a SDR-based 5G NR implementation. We are intending to adopt the non-standalone (NSA) mode for 5G NR in which a NR gNB will provide user-plane traffic services for a NR-capable UE to a master 4G eNB.


![]({{ site.url }}/assets/img/facilities/upatras/upatras_access_network.png)

## Backhaul

Patras5G facility includes state-of-the-art mmWave backhaul and Fixed Wireless Access (FWA) solutions. The UltraLink™-GX80 all-outdoor mmWave PtP Ethernet radio at 70/80 GHz (E-Band), that provides a 10 Gbps backhaul capacity, will be used to interconnect the g/eNBs with the core network and the data centre at the UoP premises.

Further, ICOM’s FWA solutions will be used to provide broadband access to public organisations’ sites (e.g. University Campus, City Hall, etc.) in the city. The WiBAS™ OSDR PtMP all-outdoor radio, as it has been enhanced to provide >1.5 Gbps aggregate sector capacity and < 1 ms latency  through the phase 1 project SPEED-5G, will be used.

 

## Core 5G /IoT services

In Patras5G, apart from Service Slice life-cycle management services and OSM, the FhHG Open5G Core will be installed. The Fraunhofer Open5GCore implementation is a 5G oriented implementation of the core network (currently 3GPP Release 14 and 15, Release 16 planned in two years). The Open5GCore enables the connectivity service as requested within the 5G networks. To support NB-IoT, the Patras/Greece facility will host the Open5GCore NB-IoT extension, which is the first implementation of the essential 3GPP NB-IoT features (Release 13 ‑ TS 23.682) enabling the demonstration of low energy IoT communication. It addresses the current stringent needs of the 5G use cases to provide low power, low cost efficient communication for a massive number of devices. On the NBIoT, LTE-M radio side there will be both commercial licenced as well as open source solution available.

## MEC

The Patras/Greece facility will provide support for Mobile/Multi-access Edge Computing on two fronts:

(i) IoT Slicing: A Virtualized Infrastructure Management (VIM) (sub-)component will be designed, implemented and integrated within the overall MANO architecture, to enable the virtualization of the available edge IoT resources (sensors/actuators) for access within individual network slices.

(ii) Mobile streaming applications support: The facility will support MANO mechanisms for the realization of high throughput, low latency, mobile types of applications (e.g., gaming, AR/VR) and corresponding test cases. Such mechanisms will include DNS and traffic flow management (on Mp1 ETSI MEC interface) for baseline service orchestration, as well as mobility support mechanisms i.e., mobility management events such as application context transfer, user redirection network/application level), and a subset of the Location Service (ETSI GS MEC 013) for triggering mobility management events.



# Experimentation Process

Read more:
[Experimentation process](https://wiki.patras5g.eu/experimentation-process)
[Telemetry/Monitoring](https://wiki.patras5g.eu/telemetry-monitoring)

# Demo videos


5G end-to-end experimentation: From Service Order to Network Monitoring Service https://www.youtube.com/watch?v=X662lml0p8w
5G-VINNI Patras Facility [video](https://www.youtube.com/watch?v=rASfEuHzhW0) for a quick presentation

# KPIs and Use Cases 

Check in this page some KPIs: [Patras5G-KPIs](https://wiki.patras5g.eu/Patras5G-KPIs)



#  Patras 5G Autonomous Edge


![edge]({{ site.url }}/assets/img/facilities/upatras/upatras_5g_edge.png "Edge")



Patras 5G Autonomous Edges, are mobile boxes, ideal for on-premise 5G deployments , containing everything from the 5G New Radio and 5G Core, Network and Service Orchestrations including a Virtualized environment based on Openstack!

# Features

## Hardware

- XEON D1518 @2.2	4	64	512GB NVMe	6x1Gb + 2 x10Gb
- XEON D2146NT @ 2.3GHz	8	64	512GB NVMe	6x1Gb + 2 x10Gb
- XEON D2146NT @ 2.3GHz	8	64	512GB NVMe	6x1Gb + 2 x10Gb

## Virtualized Infrastructure

- Ubuntu 18.04
- Openstack Stein
- Kubernetes cluster in Openstack
- 
## Network Orchestration

- OSM (Open Source Mano)

## Service Orchestration

- Openslice

## 5G New Radio

- Indoor range

## 5G Core

## Added Services

(These are planned services, not available simultaneously)
- Akraino Edge stack for MEC
- EdgeXFoundry for IoT gateway functionallity
- Intel OpenNESS for MEC

## Monitoring Services

- Graphana
- Prometheus
- Netdata


# Service Catalogue and LCM of Network Slice Services

[Service Catalogue](https://wiki.patras5g.eu/service-catalogue)
[Support and LCM of Network Slice Services](https://wiki.patras5g.eu/support-and-lcm)
[Customer Facing Services](https://wiki.patras5g.eu/customer-facing-services)

[Demo Video for onboarding and deployment of VNFs/NSDs](https://www.youtube.com/watch?v=3-fRuVfe2a4)


# The Patras5G coverage area
the following are the coverage plans of the facility

![Patras]({{ site.url }}/assets/img/facilities/upatras/upatras_coverage_1.png "Patras")
![Patras]({{ site.url }}/assets/img/facilities/upatras/upatras_coverage_2.png "Patras")



For more information please check [http://wiki.patras5g.eu/](http://wiki.patras5g.eu/) )

