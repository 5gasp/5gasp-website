---
title: 5GUKTest 
subtitle: University of Bristol	
name: 5GUKTest 
complete-name: University of Bristol
country: United Kingdom

---
# 5GUKTest Network for 5GASP project

This test network is located within Bristol city centre as shown in the Figure 1 with the key network entities hosted at the Smart Internet Lab, “We The Curious” (WTC), MShed Museum, Millennium Square (MSq).

![]({{ site.url }}/assets/img/facilities/bristol/Fig1.png)


![]({{ site.url }}/assets/img/facilities/bristol/Fig2.png)


A more detailed view of the network connectivity is shown in Figure 2 depicting the connection across sites through dark fibre network. The Smart Internet lab hosts the cloud network functions for the management and operation of the 5G Cellular network as well as providing a virtualised network infrastructure for hosting 5G ASP Software components, including UNIVBRIS MANO: OSM release 9 and monitoring server. 
This location also hosts the 3rd party technologies under test as part of a given research project connected to various hosting sites across Bristol. Here, we only show the WTC and MShed as way of illustrating the creation of a test network and service slices for demonstrating typical use cases and field trials that are carried out at MSq.

The hosting sites WTC, MSq. and MShed at the edge of network provide IT rack and space for the compute nodes, switches as well as the access technologies to deliver end to end communication services demonstrating 5G technologies. The urban city centre outdoor 5G coverage area provides two radios cells with overlapping coverage area at the edges of the MSq offering opportunities for service mobility/wireless handover at pedestrian speed. 

Summary of technologies deployed as part of the Smart Internet Lab test network include:

* 4G/5G Core network 
* 4G & 5GNR 
* SDN enabled switches and service routers
* Wi-Fi access points and management network
* OpenStack and Kubernetes based Virtual Infrastructure Managers (VIMs)
* In house developed measurement and monitoring tool

<br>

This test facility can demonstrate 5GASP use cases with these technologies:

* Edge computing with servers hosted at each site co-located with UPF
* NFV orchestration where MANO can be hosted at the Smart Internet Lab facility
* O-RAN and xApp research and development of new functions 
* ML use cases can be realized, where the monitoring server can host ELK stack. The monitoring will have access to compute infrastructure monitoring (OpenStack or Kubernetes). It can also receive UE radio parameters:
    * via the UE 
    * via the near Real Time RAN Intelligent Controller (nRT-RIC) based on ORAN (under study for development)
* Hosting partner technologies for evaluation and field trial 


