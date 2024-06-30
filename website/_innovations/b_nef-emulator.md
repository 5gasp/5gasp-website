---
title: NEF Emulator
name: NEF Emulator
---

In the evolving landscape of 5G technology, the Network Exposure Function (NEF) is pivotal in ensuring seamless and secure integration between external applications and the 5G core network. Further, we will delve into the intricacies of the NEF, highlighting its functionalities, the significance of the NEF Emulator, and the APIs it offers.

### Understanding the Network Exposure Function (NEF)

The NEF is a crucial component of the 5G core network, responsible for managing and facilitating connections from external applications that seek access to internal data. Acting as an interface gateway, the NEF enables secure communication channels, ensuring that third-party applications can interact with the 5G core network efficiently and safely. Its service-aware functionality allows it to cater to the specific requirements of different applications, making it an essential tool for developers and network operators.

### NEF Emulator: Bridging the Gap for Developers

The NEF Emulator is an open-source simulator designed to provide application developers a platform to experiment with the NEF. Utilizing standardized APIs in a simulated, configurable environment, the NEF Emulator replicates the capabilities of the NEF, allowing users to interact with and test its northbound APIs. Initially implemented in the EVOLVED-5G European project, the NEF Emulator has been further extended by the 5GASP project, mainly by adding testing-related capabilities. This emulator is integral to the 5GASP project's efforts to conduct 5G Readiness Test Cases, ensuring that applications are well-prepared for deployment in a 5G environment.

### Key APIs Offered by the NEF Emulator

The NEF Emulator provides a range of standardized APIs, allowing for comprehensive testing and interaction with the NEF. Some of the key APIs — ****that follow standards ****29.122 - 17.8.0 ****— include:

1. **Monitoring Event** : Implemented by EVOLVED-5G, this API allows the monitoring of specific network events.
2. **AsSessionWithQoS**: Also implemented by EVOLVED-5G, it manages session quality of service.
3. **Resource Management of Background Data Transfer (BDT)**: Implemented by 5GASP, this API manages background data transfer resources.
4. **Chargeable Party**: This API, implemented by 5GASP, deals with identifying and managing chargeable parties within the network.
5. **Network Status Reporting**: Allows for network status reporting, implemented by 5GASP.
6. **Traffic Influence**: Implemented by 5GASP, this API manages the influence of traffic within the network.
7. **Analytics Exposure**: Another API by 5GASP that exposes analytics data from the network.

### Enhancing Testing with the Report API

In addition to the APIs above, 5GASP has developed a Report API that monitors and records all requests made by network applications to the NEF. This API is crucial for the continuous integration and continuous deployment (CI/CD) services, as it verifies that network applications can effectively communicate with the NEF. Every request and the corresponding response received by the NEF is recorded in a report file, ensuring transparency and reliability in communication.

## Conclusion

The 5GASP's NEF Emulator further enhances the testing capabilities, ensuring that applications are ready for real-world deployment. As 5G technology continues to evolve, tools like the NEF and its emulator will play an increasingly important role in shaping the future of network communications.

For more detailed information, you can visit the [NEF GitHub repository](https://github.com/5gasp/NEF-Emulator).