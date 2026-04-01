# Local Communication Network

## The Problem

Recently, in January 2026, Verizon suffered a system-wide cell phone service outage that lasted the better part of a day. During this time, (non-WiFi-connected) Verizon phones completely lost their ability to call or text. These outages usually last a short time, amounting to little more than an inconvenience for most. But what if it lasted longer, or indefinitely? If this were to happen, our cell phones would become useless as mobile communication devices, and our ability to communicate with each other would be much degraded.

Put simply, the main problem is that our cell phones depend on radio communication networks over which we have no control.

## A Solution

A potential solution to this problem is to create an alternative radio communication network, an increasingly popular technology called Meshtastic allows us to do exactly that. By pairing your phone to one of these devices (Bluetooth or WiFi), you're able to send and receive fully-encryoted text messages direcly over the air with other Meshtastic users.

As described on [meshtastic.org](https://meshtastic.org/), Meshtastic is:

> An open source, off-grid, decentralized mesh network built to run on affordable, low-power devices. No cell towers. No internet. Just pure peer-to-peer connectivity.

For those not well-versed in technobabble:

- "open source" : All of the design files and software code you need to manufacture and program the Meshtastic devices is freely available for anyone to read and use.

- "off-grid" : These low-power devices can be run from a solar panel or battery and do not require access to the electrical grid.

- "decentralized" : The network is a result of many devices working together, with each device playing a more or less equal role (see: [Roles](https://meshtastic.org/docs/configuration/radio/device/#roles)), so there's no one "central" device that if turned off would cause the network to stop working. 

- "mesh network" : it's a relay network in which devices communicate with its neighboring devices to create a larger effective network

- affordable, low-power devices = ...
- peer-to-peer connectivity = ...

<hr>

Beacon has an existing infrastructure of digital communication devices that work together to create a resilient, low-power encrypted text messaging network. These devices primarily use a technology called [Meshtastic](https://meshtastic.org/), which combines [LoRa radios](https://en.wikipedia.org/wiki/LoRa) and custom software to provide seemless interoperation between [compatible devices](https://meshtastic.org/docs/hardware/devices/). While some of these devices include a keyboard and display for use as a standalone text messaging device, most are designed to be controlled over Bluetooth or WiFi via the Mestastic app on a smartphone ([Android](https://play.google.com/store/apps/details?id=com.geeksville.mesh), [iOS](https://apps.apple.com/us/app/meshtastic/id1586432531)), tablet, or [computer](https://client.meshtastic.org/).

