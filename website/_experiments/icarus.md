---
title: Experiments
subtitle: ICARUS
experiment-title: ICARUS
author: INFOLYSIS P.C.
country: Greece
experiment-complete-title: ICARUS
---

# Title
ICARUS

# Organization
INFOLYSIS P.C., Greece

# Idea and Concept
ICARUS experiment relied on the use of the PPDR ONE infrastructure, while the inclusion of the qMON network sensors was necessary mainly for the IoT data provision. Within this 5GINFIRE experimental framework, ICARUS experiment aimed at researching the 5G opportunity for Internet of Things (IoT) interoperability and openness framework through the agility provided by the use of SDN and NFV as engineering tools, which provide the distributed intelligence to analyze and manage traffic flows. In specific, ICARUS combined the agility of a virtual Deep Packet Inspection (vDPI) function with the flexibility of data protocol mapping functions (e.g. CoAP, MQTT, HTTP to generic UDP), allowing to the overlay IoT services to be automatically deployed and programmed by a single domain coordinator/orchestrator/experimenter. Our main objective of the SDN/NFV-enabled IoT ICARUS experiment was to expand the interoperability level of the 5GINFIRE/PPDR ONE by providing an agile manner for data interoperability. By coupling a vDPI-based protocol detection process with the automatic applicability of the appropriate SDN steering commands of the heterogeneous IoT traffic to the correct IoT protocol-mapping VNFs, ICARUS can achieve interoperable communications by providing to 5GINFIRE infrastructure the proposed interoperability functionalities.

Overall, by adding SDN/NFV- based features at the PPDR ONE testbed, ICARUS managed to provide an agile manner for data interoperability provision. More specifically, the 5GINFIRE project gained from the ICARUS experiment an expansion to the functionalities of the current system, complementing the existing 5GINFIRE infrastructure, by utilizing heterogeneous IoT data protocols and then the proposed vDPI to take the role to identify the heterogeneous protocols and map them to a generic data protocol. Upon a proper integration, both systems (i.e. 5GINFIRE/PPDR-ONE and ICARUS) can complement each other and provide a fully interoperable IoT solution for a variety of IoT data protocols.

Thus, the 5GINFIRE with the ICARUS extensions can be mutually improved and met the user/experimenters requirements for more advanced and realistic use-cases. For this reason an API is provided, where further systems can integrate with ICARUS (as a building block of 5GINFIRE system), where future experiments can benefit from the ICARUS-driven homogeneous IoT data domain.

Moreover, INFOLYSiS evaluated all the experience gained from the execution of the ICARUS experiment at the 5GINFIRE testbeds, assessing the different phases involved in the experiment, starting from the design of the experiment up to the configuration and finally the execution of it. In this document, INFOLYSiS provides the experimental results as a feedback considering the whole lifecycle of the experimental process, identifying these 5GINFIRE tools that facilitated the experimentation process, contributing positively to the overall execution of the work plan and contributed to a successful outcome.


# Experiment Details and Objectives

It must be noted that for the execution of the ICARUS experiment, INFOLYSiS relies on the use of the PPDR ONE infrastructure, while the inclusion of the qMON network sensors mainly for the IoT data provision is expected. These data communicated and then, in order to create conditions of non-interoperability, the data flows encapsulated to different IoT protocols (e.g. CoAP, MQTT, HTTP, etc.) through the INFOLYSiS encapsulator nodes, which will be deployed as VNFs at the PPDR-ONE infrastructure, in order to perform the ICARUS experiment with real data streams and different data protocols. The experimental methodology also includes the stressing of the vDPI and the mapping functions for different data rate values and traffic volumes.

Thus, the traffic received by PPDR-ONE encapsulated in MQTT, CoAP and HTTP protocols respectively, creating a mix of heterogeneous streams, which is further used for the execution of ICARUS experiment. So, ICARUS experiment considered these IoT multi-protocol flows that passed through the INFOLYSiS vDPI, which was instantiated as a VNF in a Virtual Server of PPDR-ONE testbed. Based on the classification of the flows to the different protocols, then appropriate SDN rules applied in order each classified IoT traffic (e.g. the CoAP traffic, the MQTT traffic and the HTTP traffic) to be forwarded to the suitable mapping function (which will be also instantiated as VNF at the server with virtualization capabilities), and each one of them were mapped each IoT-protocol specific data flow to a generic/interoperable data protocol flow (such as UDP). Thus, the traffic of the three different protocols were mapped to a generic data protocol, making all IoT data interoperable under the UDP IoT protocol.

At the end and upon ICARUS successful IoT forward and mapping actions, the produced IoT sensor data flows were interoperable based on the generic UDP protocol, ready for further use by third-party applications through the API of the INFOLYSiS interoperable vGW

![ICARUS 1](https://5ginfire.eu/wp-content/uploads/2019/11/icarus1-1024x426.png)


Figure 1 describes the concept of the ICARUS experiment, providing a direct map with PPDR ONE Testbed architecture and the ICARUS expansion. The data flows originate from the PPDR ONE qMON network sensors and are of the following types:

* PING (round trip time)
* DNS response time
* DL speed
* UL speed
* IPERF DL/UL speed
* WEB response time

As per Figure 1, following the receipt of qMON network sensor data and the encapsulation phase, these IoT multi-protocol flows were passed through the INFOLYSiS vDPI VNF, which was instantiated at the PPDR ONE SDN/NFV testbed. Based on the different IoT protocol classification of the flows, then appropriate SDN rules were applied in order each classified IoT traffic (e.g. the CoAP traffic, the MQTT traffic and the HTTP traffic) to be forwarded to the suitable mapping function (which will be also instantiated as VNF at the server with virtualization capabilities of PPDR ONE), where each one of them mapped each IoT-protocol specific data flow to a generic/interoperable data protocol flow.
Thus, the traffic of the three different protocols were mapped to a generic data protocol (UDP), making all processed IoT data interoperable. In this framework, specific objectives of the ICARUS experiment included:

1. To assess the effectiveness of using on top of an SDN/NFV-enabled testbed/network, a DPI function combined with virtual functions that map IoT protocols (such as MQTT, CoAP, HTTP) to generic data protocol in order to provide an agile platform for data interoperability.
2. To design and develop appropriate SDN-app, which provides an agile logic in the automatic provision of interoperability on top of PPDR ONE testbed, based on the automatic sensing of the data protocols by the DPI.
3. To abstract the PPDR ONE sensor data domains into one homogeneous data domain by exploiting the deployed and instantiated mapping VNFs.

The following table summarizes ICARUS objectives, associating them with specific deliverables and success criteria:


| OBJECTIVE | MEANS OF VERIFICATION | SUCCESS CRITERIA (SC)/KPIS |
|--|--|--|
| Objective 1 | Deliverables: <br> D1, D2, D3 | SC1.1 Automatic sensing by the vDPI of 3 IoT protocols. <br> SC1.2 Success rate higher than 95% in the appropriate SDN-based traffic steering of each IoT data flow to the suitable mapping function. <br> SC1.3 Mapping of each data packet to a generic data protocol with zero packet loss (confidence interval 95%). |
| Objective 2 | Deliverables: <br> D2, D3 | SC2.1 Design and development of an SDN-app suitable for providing in an automatic way data interoperability <br> SC2.2 The SDN-app should be capable of handling 3 different IoT data protocols. <br> SC2.3 Successful service chaining of each mapping function and the vDPI of the ICARUS platform for 4 different combinations of IoT data (CoAP/MQTT, COAP/HTPP, MQTT/HTTP, COAP/MQTT/HTTP). |
| Objective 3 | Deliverables: <br> D2, D3 | SC3.1 Provision of GUI for the successful representation of the unified data flows in real time for 4 different combinations of IoT data (CoAP/MQTT, COAP/HTPP, MQTT/HTTP, COAP/MQTT/HTTP). <br> SC3.2 Extensibility of ICARUS platform by providing API access to the homogenized data. <br> SC3.3 Stress Tests |

With the successful execution and completion of the ICARUS experiment, INFOLYSiS had the opportunity to illustrate and describe the key components of IoT interoperability provision.
