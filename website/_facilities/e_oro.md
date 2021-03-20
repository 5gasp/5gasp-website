---
title: ORO
subtitle: Orange Romania 5G Lab
name: ORO
complete-name: Orange Romania 5G Lab
country: Romania
---


![]({{ site.url }}/assets/img/facilities/oro/oro_logo.png)


# ORO 5G Lab
Orange Romania is the mobile telecommunications market leader in Romania with over 10.7 million customers in 2021 and over 2700 employees. ORO is part of the Orange Group, one of the largest multi-national corporations in the world with a strong leadership in innovation and over 272 million customers over 5 continents. ORO has invested well above 2.5 billion EUR since 1997 and is constantly investing in the network development, new technologies, products and services. ORO launched Orange 5G in Bucharest, Cluj-Napoca and Iasi with plans to expand the coverage in other cities. ORO is first within the Orange footprint to launch 5G. The ORO 5G network offers maximum download speeds of up to 1.2 Gbps and average speeds of 600 Mbps. 
The **Orange 5G Lab** is an advanced 5G experimentation facility, in Bucharest, created in collaboration with the CAMPUS Research Center of UPB - Universitatea POLITEHNICA of Bucharest. The 5G Lab will focus on prototyping, testing and validating new 5G use-cases, new applications and equipment and will play a crucial role in the 5G-PPP / ICT projects where ORO is a partner. A team of highly skilled experts and academics will enable delivery as per the projects DoW. 5G-ASP is one of the first H2020 Projects to be fully supported by the 5G Lab Team.

**The lab will offer the following services**: 

1. End-to-End Testing and validating 5G scenarios/solutions for different verticals 
2. Prototype 5G network applications on different market verticals 
3. Security Assessment for 5G NetApps 
4. Security Implementation for 5G networks
5. Adapt and Implement different use-cases for 5G applications 
6. Research and development of 5G/beyond 5G networks/applications/services
7. 5G/beyond 5G Consultancy for public and private stakeholders (e.g policy implementations, business assessment about 5G implementation, etc.)
8. Business consultancy for scaling up startups or spinoffs
9. Engage as partners in national and international R&D and innovation projects for cybersecurity and beyond 5G infrastructures

![]({{ site.url }}/assets/img/facilities/oro/campus.jpg)


# Location

ORO 5G Lab is located in Bucharest, 6th District, Romania. It is hosted in the CAMPUS builing of Universitatea POLITEHNICA of Bucharest.

![]({{ site.url }}/assets/img/facilities/oro/map.png)


# Available Infrastructure

The Romanian facility integrates different communication technologies for 5G, 4G, LTE-M network  and  LoRaWAN connectivity - that support the growth of the IoT products ecosystem and further 5G vertical’s developments. The 5G facility in these 5 cities is sustained by two infrastructure developments scenarios: (1) 5G developed infrastructure by using 5G commercial network already existing there and (2) 5G developed infrastructure by using 5G-PPP open tools.
The 5G facility - commercial infrastructure - is supporting 5G NSA (option 3X) and SA technological implementation and 5G vertical’s and use cases as described, including a roadmap of network availability and services as described in the picture below:


![]({{ site.url }}/assets/img/facilities/oro/facility2.png)

The 5G facility is providing Release15 and later Release16 capabilities, Core Network functions infrastructure and 5G RAN integration, in phase (1) traditional implementation(based on (v)EPC capabilities already deployed in these cities and further in phase (2) within a virtualized environment for 5G SA services and SBA implementation, supporting different services requirements and network capabilities, as both 5G technical architecture are capable to support network slicing implementations. 


## Computing Infrastructure and devices 

- **Computing capabilities**
	-   240 physical cores  
	-   4 TB of RAM  
	-   100 TB Storage  
	-   1Gbps and 10Gbps Switches  
- **OAI 5G RAN Platform**
	-   OAI implements several 3GPP RAN interfaces in openairinterface5g and is composed by:
	-   Radio Cloud Center(RCC), having the role of NG-RAN Central Unit
	-   Radio Access Unit, multiple MAC-RLC mid-haul entities, having the role of NG-RAN Distributed Unit
	-   Radio Remote Unit, equipment radio at the site level, processing elements, corresponding to a PNF RU software module, L1 software module, MAC-RLC software module, pre-decoder software module, PDCP-U and RRC-PDCP-C module
	-   Software Defined Radio unit is based on National Instruments ETTUS, USRP N310- a networked software defined radio (SDR) that provides reliability and fault-tolerance for deployment in large-scale and distributed wireless systems


- **OpenAirInterface Core Network**
	-   3GPP EPC implementation (HSS, MME, S-GW and P-GW)
	-   5G Service-based Core Network architecture, in 5G EVE will be developed an OpenCN fully compliance with 3GPP 5G CN
	-   Core network running on a virtualized infrastructure, as using Openstack based implementation or K8S
- **Orchestration tool**
	-   ONAP orchestration for design, creation, orchestration, monitoring, and life cycle management of VNFs, SDNs, and higher-level services
	-   VNFs/NSDs catalogues
	-   ETSI-MANO NFVI, OSM 
	-   Virtualized infrastructure using tool components as Openstack and Kubernetes
	-   NFV/VNFs deployments, Life Cycle Management, service and slice instantiation
- **Experimental  5G Network(NSA):**
- - vEPC & 5G RAN
  - 2 5G RAN antennas 
  - vEPC core network integrated with the 5G RAN sites
  - System monitoring and metrics collection
  - IP/Network infrastructure (IPFABRIC)
  - IaaS/CaaS capabilities (Openstack/K8s)
  - Orange spectrum for testing
- **5G  SA Release 16 testbed**

​               5G SA Core(combo core) and RAN


- **Advanced  IPFABRIC Network**, Segment Routing, orchestrated by NSO

  ![]({{ site.url }}/assets/img/facilities/oro/facility4.png)
  
  


# **Testbed Description:**  
- Private/Public: Both
- NFVO: OSM 8  
- NFVI: OpenStack, IaaS, K8s  
- ONAP
- NSO 
- **CPEs (Customer Premise Equipment):** 
    - Huawei / ZTE / HTC (any COTS CPE) 
    - **[Semi-anechoic chamber](https://octoscope.com/English/Products/Ordering/Testbed_Building_Blocks/BOX-18.html)**,  specifically designed for such demanding applications as MIMO testing,  wireless mesh performance analysis, and IoT testing
    - 5G programable devices, [SIM8200EA](https://www.simcom.com/product/SIM8200EA_M2.html) from SIMCOM with Evaluation Kits
- **Telemetry / Monitoring mechanisms in place:** 
    -   Prometheus / Grafana

