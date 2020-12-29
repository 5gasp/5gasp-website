---
experiment-title: 5G-SAFTEY
author: Allbesmart Lda.
country: Portugal
experiment-complete-title: 5G-SAFTEY – Testing network slicing for the 5G Public Safety vertical

---
The 5G-SAFETY experiment has deployed a use case on top of the NITOS testbed, providing two services over two network slices, with a focus on the QoS-aware control and Network Functions Virtualization. The main goal has been the implementation of two competing network slices on NITOS’ LTE infrastructure: one emulating a MVNO Public Safety slice with high throughput and reduced latency requirements and the other emulating an OTT service provider (delay tolerant – best effort slice). Different resource management algorithms were implemented and evaluated in terms of performance gains when operating under computational resource limitations. The main conclusion of this experiment is that in NFV scenarios with two concurrent network slices sharing the same NFVI, dynamic allocation of resources based on QoS parameters observed by virtual probes is indeed an effective strategy to improve the network performance of the priority slice when it is subjected to heavy load.