---
title: OpenSlice
name: OpenSlice
---

As the 5G standards mature, industry verticals are increasingly eager to test and develop new services to meet market demands. One significant innovation in this space is OpenSlice, an open-source Operations Support System (OSS) that delivers Network Slice as a Service (NSaaS).

### Introduction to OpenSlice

OpenSlice is an open-source platform designed to facilitate the delivery of NSaaS. It leverages emerging standards from Standards Development Organizations (SDOs) to provide a flexible, cost-efficient mechanism for managing multiple virtual networks running on a shared infrastructure. This model is particularly advantageous for vertical industries that require isolated and tailored network environments(Openslice).

### Key Features of OpenSlice

OpenSlice stands out due to several innovative features:

1. **Service Abstraction**: OpenSlice defines abstractions over the complexities of Virtual Network Functions (VNFs), Containerized Network Functions (CNFs), and Network Services (NSs). This allows verticals to request and deploy services seamlessly, focusing solely on the service logic without worrying about underlying technical complexities.
2. **Service Catalog Management**: It offers comprehensive service catalog management, enabling Communication Service Providers (CSPs) to manage, organize, and expose service catalog items to customers. This includes the ability to create and manage both Customer Facing Services (CFS) and Resource Facing Services (RFS)(nef).
3. **TMForum Open APIs**: OpenSlice utilizes TMForum's Open APIs to facilitate service catalog management, ordering, inventory management, and more. These APIs ensure interoperability and ease of integration with other systems.
4. **Service Ordering and Fulfillment**: The platform allows customers to place service orders through a well-defined process. Service specifications are translated into resource requirements, which are then processed by the Network Function Virtualization Orchestrator (NFVO) to instantiate the network slice.

### OpenSlice Architecture

OpenSlice employs a microservice-based architecture that enhances flexibility, scalability, and maintainability. The architecture includes the following key components:

- **Service Portal**: Provides a user-friendly interface for browsing and ordering services.
- **NFV Portal**: Allows users to manage NFV artifacts and onboard them to a target MANO/NFV orchestrator.
- **API Gateway**: Facilitates communication between internal APIs and external services.
- **Message Bus**: Enables asynchronous communication between microservices.
- **Authentication Server**: Implements OAuth2 for secure authentication.
- **Service Orchestrator (OSOM)**: Manages and propagates service orders to the appropriate service orchestrators and NFVOs.

### 5GASP Integration: Enhancing OpenSlice's Capabilities

5GASP's related activities resulted in the development of various OpenSlice capabilities, particularly to support the project's innovative use cases. One of the most notable contributions is the **Network Applications Validation and Certification Platform**, which includes an **Application Store**. This platform enables developers to validate and certify their applications within a 5G environment, ensuring they meet the necessary standards and performance metrics before deployment.

- **Network Applications Validation**: By leveraging OpenSlice, 5GASP provides a comprehensive environment for testing network applications. This involves detailed performance analysis, security checks, and interoperability testing, ensuring that the applications seamlessly integrate with existing 5G networks. The starting point for conducting testing processes is the 5GASP Network Application Onboarding and Deployment Service (NODS), offered through OpenSlice.
- **Application Store**: The Application Store within the 5GASP platform allows third-parties access to a catalog of Network Applications for different verticals. These applications, when on the Application Store, have been thoroughly tested and certified against 5G, security, and performance standards, which ensures they are robust, reliable, and ready for real-world. The Application Store is also offered through OpenSlice, which exposes several available Network Applications via its Products Catalog.

These use cases from the 5GASP project have been instrumental in evolving OpenSlice into ETSI's first Software Development Group, highlighting its potential to support extensive application development and deployment in the 5G ecosystem.

### Conclusion

OpenSlice, powered by the innovative use cases from the 5GASP project, represents a significant advancement in the orchestration and management of network slices in 5G networks. By offering a flexible, scalable, and open-source solution, OpenSlice simplifies the deployment of complex network services, making it an invaluable tool for industry verticals looking to leverage the full potential of 5G technology.

The integration with 5GASP enhances OpenSlice's functionality and provides a robust platform for validating and certifying network applications, ensuring readiness for deployment in the 5G ecosystem. As OpenSlice continues to evolve, it is well-positioned to support the growing demands of 5G networks and beyond.

For more detailed information, you can visit the [OpenSlice documentation](http://openslice.io/).