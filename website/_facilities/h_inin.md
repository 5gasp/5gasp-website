---
title: ININ
subtitle: Internet Institute Ltd.
name: ININ
complete-name: internet Institute Ltd.
country: Slovenia
---

![]({{ site.url }}/assets/img/facilities/inin/inin_logo.png)


# ININ:
INTERNET INSTITUTE Ltd. (ININ, www.iinstitute.eu) is an innovation-intensive SME, highly specialized in 5G, PPDR, Future Internet, Internet of Things, and Cloud-based solutions and services, with a particular focus on end-to-end network and services monitoring, QoE and QoS testing, quality assurance systems, and on Emergency Response and Intervention Management tools, application and solutions for corporate and public safety domains. The company is engaged in industrial-grade research and development, as well as product and solution integration and management. ININ will be primarily involved with integration of the PPDR ONE facility into the 5GASP environment, with the system adaptation to support multi-domain fabric related to the PPDR vertical and to provide the NetApp components for radio and core mobile network for the PPDR isolated operational mode (5G IOPS).


# Location:
Internet Institute is located in Ljubljana, the capital city of Slovenia.

![]({{ site.url }}/assets/img/facilities/inin/inin_location.png)


# Available Infrastructure:
The Public Protection and Disaster Relief facility for Outdoor and Indoor 5G Experiments (PPDR ONE) is an environment supporting experimentation with 5G network architectures and services for the PPDR and critical-communications verticals. The facility comprises an SDR- and CPRI-based radio and mobile core system (4G and 5G) with flexible configuration options powered by NFV, cloud backend infrastructure, a set of reference PPDR services and apps, a PPDR IoT kit, industrial and ruggedized end user devices as well as a test and validation toolkit. It provides indoor and outdoor experimentation sites as well as a compact portable mobile node for field-based network testing and services verification. The facility was developed with the support of Horizon 2020 program and is used as part of several 5G-PPP projects: 5GASP, 5G-LOGINNOV, Int5Gent, EVOLVED-5G, 5G-INDUCE, 5G-IANA.

![]({{ site.url }}/assets/img/facilities/inin/inin_infra.png)

The core infrastructure deployed at ININ site in Ljubljana:  

## Research graded
- KVM/OpenStack Cluster
	- 5 host machines
	- 	200 cores
	- 	500GB RAM
	- 	1Gbps/10Gbps Ethernet
	- 	1000/100 internet speed
- Kubernetes/Docker
- Orchestration
	- 	Open Source MANO
	- 	ONAP (planned 2021)
- Mobile Network
    - 	4G/LTE with ENDC (5G NSA), 5G/NR with 5G CN (5G SA)
	- 	SDR based eNb and gNb (70 MHz up to 6 GHz, up to 100Mhz 5G NR bandwidth)
- Mobile UE
	-	SierraWireless EM9191 5G modem development kit

![]({{ site.url }}/assets/img/facilities/inin/inin_reasearch_graded_sierra.png)

## Industry graded
- Mobile Network
	- 	4G and 5G NR Cell (CPRI/RRH), n78, 2x2 MIMO, NSA and SA 5G Core Network
- Mobile UE
	- 	Network appliance (Advantech) with integrated 5G modem (Sierra Wireless EM9191)
- Drone   
	-	DJI Mavic Air 2
- Environmental/industrial sensors
	- 	Ultrasonic water level sensor (SENIX - ToughSonic REMOTE 14)
	- 	Ultrasonic water level sensor (SENIX - ToughSonic REMOTE 30)

![]({{ site.url }}/assets/img/facilities/inin/inin_industry_graded.png)


## Mobile Network Testing System (qMON)

Telco-grade end-to-end network monitoring and testing solution. qMON components are deployed in a distributed system architecture with modular capabilities (mobile, fixed and cloud deployment) that provides redundant local and centralized storage of network and services metrics and test results, flexible results exporting, advanced visualizations and more. 

qMON System Components:
-	System Management
	-	centralized cloud management of the qMON Agent probes
-	Reference Servers (VM/VNF/Docker)
	-	reference test endpoints, can be deployed in various formats
- 	Test Agents (PNF/VNF/Docker/Android)
	-	test probes, can be deployed in various formats and supports various environments (mobile, fixed and cloud)
-	Results Collector (VM/VNF/Docker)
	-	collects the test results gathered from qMON Agent probes 
- 	qMON Analytics (VM/VNF/Docker)
	-	Grafana- and Tableau based dashboards for real-time and off-line test results visualisations

![]({{ site.url }}/assets/img/facilities/inin/inin_qmon.png)

## PPDR Services Toolset

** iMON Solution ** 
Tactical Dashboard exposing real-time PPDR services for a common operational picture, situational awareness, and intervention management. It features a rich client HTML5/PHP web application, supporting: RT common operational picture, RT assets tracking and backlog, data analytics, and visualisations, intervention reports, and logs; Backend: RT notifications, exposed APIs, automated hierarchical (group) user and device management.

** iMON Mobile App **
Android-based Mobile application for triage and tracking from the field. Native mobile app with field sensing, time and distance-based location tracking, automated triage reporting (official procedural reporting formats, image attachments, automatically retrieved location data); automatic sync with COP; use of COTS mobile devices with IP67.

![]({{ site.url }}/assets/img/facilities/inin/inin_imon.png)


# **Testbed Description:**  
Private/Public: Private  
Software Stack:  
-   NFVO: OSM / ONAP (planned 2021)  
-   NFVI: OpenStack (VNF)/Kubernetes (KNF)
Mobile Network:
-   4G/LTE with ENDC (5G NSA mode) and 5G NR with Core Network (5G SA mode) 
-   5G NR Cell Site (CPRI/RRH 20 W), n78, 2x2 MIMO, SA/NSA
-	SDR based eNb/gNb  (70 MHz up to 6 GHz, up to 100Mhz 5G NR bandwidth, 3 x CA LTE)
- 	Fixed/portable deployment
5G UEs (User Equipment):  
-	5G Smart Phones with NSA and SA support (Samsung s20 5G, Samsung s21 5G, OnePlus 8T)
- 	Industrial 5G Gateways with NSA and SA support (Network appliance with industrial modems from Sierra Wireless)
 
Telemetry / Monitoring mechanisms in place:
-   qMON Monitoring and Testing Suite
-   Prometheus-based infrastructure monitoring (Hosts, VMs)

