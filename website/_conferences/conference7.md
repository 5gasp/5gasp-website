---
paper_type: Conference
title: "Towards Low-latent & Load-balanced VNF Placement with Hierarchical Reinforcement Learning"
authors: Xenofon Vasilakos, Monchai Bunyakitanon, Reza Nejabati and Dimitra Simeonidou
journal_title: IEEE International Mediterranean Conference on Communications and Networking, 7–10 September 2021
doi: 10.1109/MeditCom49071.2021.9647532
repository_link: https://ieeexplore.ieee.org/document/9647532
relevance: "Current orchestration frameworks lack intelligence and handle resources by neglecting service-level and systemwide performance. Towards addressing this gap, we propose a Hierarchical Reinforcement Learning (HRL) design targeting Virtual Network Function (VNF) placement comprised of (i) a local level prediction module deployed at system nodes; and (ii) a global Reinforcement Learning (RL) module topping the hierarchy, utilising live local predictions and adapting placement to systemwide dynamics. Besides Global, the local level integrates an RL
module that continuously and accurately predicts end-to-end (e2e) service latency after VNF placements, and a node-local CPU load prediction model. HRL’s is designed to stand fully autonomously or to complement and augment existing orchestrators lacking intelligence with a previously unexplored distributed multi-RL approach. Our performance evaluation over an actual 5G testbed implementation and use case shows that HRL can significantly outperform both Open Source Mano and heuristic-based VNF placement while reflecting a more complex trade-off between load and e2e delay, particularly under CPU overloading conditions."
---