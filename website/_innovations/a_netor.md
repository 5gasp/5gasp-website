---
title: NetOr
name: NetOr
---

In the fast-evolving world of 5G technology, orchestrating vertical services across multiple domains remains a significant challenge. We will explore an innovative solution offered by the 5GASP project: NetOr, a microservice-oriented inter-domain vertical service orchestrator for 5G networks.

### Introducing NetOr

NetOr, developed through the 5GASP project, addresses the limitations of traditional 5G vertical service orchestrators by providing a flexible, scalable, and maintainable solution through a microservice architecture. It supports complex use cases by ensuring adequate inter-domain support, adhering to network slicing standards, and enabling run-time operations on vertical services.

### Key Features and Architecture

NetOr's microservice architecture is designed to handle each entity within the system as a unique component. These components communicate via a centralized message bus, facilitating asynchronous message exchange. This design offers several advantages:

1. **Flexibility**: NetOr allows seamless replacement or updating of components without affecting the entire system, ensuring that the architecture remains adaptable to new technologies and requirements.
2. **Scalability**: Each microservice is stateless and can be scaled independently, allowing the system to handle many services efficiently.
3. **Maintainability**: NetOr simplifies maintenance and updates by isolating each component, ensuring high availability and reliability.

### Inter-Domain Orchestration with NetOr

One of the standout features of NetOr is its ability to orchestrate vertical services across multiple administrative domains. This ability is particularly valuable for sectors like transportation, where geographically distributed assets often fall under different operators. NetOr facilitates the creation of E2E network slices that span multiple domains, ensuring comprehensive coverage and service delivery.

NetOr employs two approaches for inter-domain orchestration:

1. **Approach A**: The VSI/NSI Lifecycle Manager (LCM) component configures VPN tunnels, maintaining centralized control and monitoring.
2. **Approach B**: Delegates the configuration to VPN nodes, utilizing NetOr's DNS server for service discovery and information sharing among nodes.

### Performance and Comparison

NetOr has been benchmarked against one of the most mature vertical service orchestrators, the 5Growth Vertical Slicer. The results demonstrate that NetOr not only matches but sometimes exceeds the performance of 5Growth, particularly in handling complex inter-domain services. The microservice architecture of NetOr allows for parallel processing, significantly reducing the time required for service instantiation and configuration.

### APIs and Standards

NetOr's Northbound and Southbound Interfaces are designed to comply with widely accepted NFV standards, ensuring interoperability and seamless integration with third-party platforms. This adherence to standards also facilitates the adoption of NetOr by other platforms, ensuring that necessary parameters are always available.

### Conclusion

NetOr represents a significant advancement in the orchestration of vertical services in 5G networks. Its microservice architecture, adherence to standards, and robust inter-domain support make it a valuable tool for operators looking to leverage the full potential of 5G technology. By addressing the limitations of existing solutions, NetOr paves the way for more efficient, scalable, and maintainable 5G network services.

The innovative approach and performance of NetOr highlight its potential to become a cornerstone in the deployment and management of complex 5G services, ensuring that operators can meet the demands of modern digital ecosystems.

For more detailed information, you can visit the [NetOr GitHub repository](https://github.com/5gasp/netor).