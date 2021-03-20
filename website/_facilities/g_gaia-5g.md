---
title: Gaia-5G
subtitle: University of Murcia/OdinS
name: Gaia-5G
complete-name: University of Murcia/OdinS
country: Spain
---





![]({{ site.url }}/assets/img/facilities/gaia/logo-odin-solutions.png?classes=center)![]({{ site.url }}/assets/img/facilities/gaia/umu-logo.jpg?classes=center)


# Gaia-5G
Gaia-5G is a laboratory for experimentation located in the Computer Science Faculty in the University of Murcia. Its research purposes are focused on the area of 5G technologies with virtualization and backhaul infrastructure for the Wireless connectivity, including 5G, LoRaWAN and 802.11p self-managed infrastructure that allows experimentation in different fields. 


# Location
Gaia-5G is located in the city of Murcia, in Spain. The core infrastructure is located in two different buildings (ATICA and the Computer Science Faculty), but there are more devices deployed on different parts along the Campus, as the Luis Vives site. 

![Map Localization]({{ site.url }}/assets/img/facilities/gaia/map.png?classes=center)


![UMU Campus multiaccess]({{ site.url }}/assets/img/facilities/gaia/multiaccesscampus.png?classes=center)


## Wired Network Equipment
Gaia-5G laboratory counts with a network infrastructure based on CWDM which provides a bandwidth of 10 Gbps fully available and customizable with QinQ/802.1ad allowing the isolation of different traffic.  MEC functionality, including the virtualisation of edge devices. SDN is provided thanks to two Delta AG7648-R with the latest PiCOS operating system in the core and HPE 2920 for leaf nodes switches supporting OpenFlow technology, in addition network programmability is granted by two barefoot Tofino-powered switches EdgeCore WEDGE100BF-32X-O-AC-F and Stordis BF2556X-1T-A1F. Connectivity between OpenFlow enabled switches and Programmable switches (P4) work at 6x40Gbps while programmable switches can work up to 100Gbps.

## Virtualization infrastructure
The laboratory is currently equipped with a cloud platform which hosts core network components, as well as SDN, NFV and MEC deployments. Two OpenStack are deployed; rocky, a full-fledged deployment offering 160 vcpus (Intel(R) Xeon(R) Gold 6138 CPU based) and 512 GB RAM splitted into two compute nodes one on each side and queens, a lightweight deployment offering 12 x86_64 vcpus (Intel(R) Xeon(R) CPU E5-2603 v3) based with 48 GB RAM and some ARM  RPI 4 nodes with 4 vcpu each (Broadcom BCM2711B0 quad-core A72 based) and 8GB RAM each. Hyper-Converged Infrastruture with a 4-node cluster with 128vCores and 4TB RAM and two edge clusters providing 24vCores and 512GB RAM each is also available for extending the VIM capabilities. OSM is the chosen orchestrator for providing NFV. 

![Gaia-Lab concept]({{ site.url }}/assets/img/facilities/gaia/5G-GaiaSDR_conHuerta_resized.png?classes=center)

## Features
- OSM Rel NINE (Rel EIGHT also available)
- 2x OpenStack 80Thread 256G RAM RAID5 SSD
- Proxmox 164Core 1TB RAM 35T RAID6 HDD
- 2x Nutanix Cluster 24 Cores 512 GB SSD + HDD HyperConvergence
- OpenFlow PicOs based 96x10G/12x40G Switching
- P4 capable 16x1/10/25G, 32x 10/25G, 104x 100G
- 2x Openflow Switch 48+6
- APS Networks BF2556x1t P4 Tofino-based switch 48x25Gb + 8x100Gb (PTP capable)
- Wedge 100BF-32X 100GbE P4 Tofino-based switch 32x100Gb
- Wedge 100BF-65X 100GbE switch 65x100Gb

## Wireless connectivity

### 3GPP
5G and LTE provision is done by using SDR technology, in particular, 2 ETTUS B210 and one ETTUS N310 are available for experimentation. These SDR devices are accompanied with a 4 Core (I7-8700 based) with 8GB RAM the B210s and a 16 Core (AMD EPYC 7302P based) with 32GB RAM server the N310. 

![Lab equipment]({{ site.url }}/assets/img/facilities/gaia/lab.jpg?classes=center)

Besides, a commercial core has been recently acquired from Amarisoft with the associated RAN hardware and both systems are being fully integrated for having a completely functional and multi-site 5G solution. The deployment consist on two sites located in the Campus of Espinardo of the University of Murcia, and two cores are available, one turnkey solution by Amarisoft, and an experimental one which can implement multiple open source 5G cores. 

![5G Sites]({{ site.url }}/assets/img/facilities/gaia/5gsites.png?classes=center)

### IoT
Gaia-5G also has LoRaWAN capabilities based on the 868MHz band. At the moment, the infrastructure relies on a Kerlink iStation gateway, located in the Luis Vives bulding. This gateway is connected to our own deployed LoRaWAN network server (Chirpstack), the received data is also forwarded to The Things Network LoRaWAN network servers. In the future, it is planned to deploy two more gateways in the campus, in order to achieve full coverage of the Espinardo campus and also to cover Murcia area. Also, NB-IoT could be integrated into the platform provided by external providers . 

![LoRaWAN Luis Vives]({{ site.url }}/assets/img/facilities/gaia/kerlinkluisvives.png?classes=center)

### C-ITSs
To complete the multi-access infrastructure, 802.11p networking is available with dual role (RSU/BSU capable PCEngines APU3d2 devices) units which can be deployed alongside Espinardo campus on demand for vehicular experimentation integrated in the current infrastructure.

### Features

- 2x USRP B210 SDR - Dual Channel Transceiver (70 MHz - 6GHz) - Ettus Research
- 1x USRP N310 SDR (ZYNQ-7100, 4 CHANNELS, 10 MHZ - 6 GHZ, 10 GIGE) - Ettus Research
- 2X RRH band 78
- 2x Amarisoft licenses gNB+core
- 1x Amarisoft UE Simbox 64 (up to 64 5G UEs)
- 1x Amarisoft Callbox (AIO solution with gNB, core and SDRs)
- Assorted antennas, filters and amplifiers for SDR scenarios

![APU3d2]({{ site.url }}/assets/img/facilities/gaia/apu3d.png?classes=center)


### 5G Coverage map
The preliminary 5G coverage plan of the two installed sites is approximately as shown in the next image.

![UMU Campus 5G Coverage]({{ site.url }}/assets/img/facilities/gaia/coverageMap-min.png?classes=center)

### LoRaWAN Coverage maps
Once the three LoRaWAN gateways are installed, the expected coverage is the following, as simulated using [Radio Mobile Online](https://www.ve2dbe.com/rmonline_s.asp).

![UMU LoRaWAN Coverage]({{ site.url }}/assets/img/facilities/gaia/loracover-min.png?classes=center)