# Community Texting Network

## The Problem

Recently, in January 2026, Verizon suffered a system-wide cell phone service outage that lasted the better part of a day. During this time, (non-WiFi-connected) Verizon phones completely lost their ability to call or text. These outages usually last a short time, amounting to little more than an inconvenience for most, but what if it lasted longer, or indefinitely? If this were to happen, our cell phones would become useless as mobile communication devices, and our ability to communicate with each other would be much degraded.

Put simply, our cell phones depend on radio communication networks that may stop working at any time.

## A Solution

One solution to this problem is for us to create our own community-run radio communication network over which our cell phones, and other screened devices, can use for continued communication in the event of a cell and/or Internet service outage. Each Meshtsatic device contains a radio transceiver (transmitter + receiver) that allows it to talk to other Meshtastic devices. By pairing your phone to one of these devices via Bluetooth or WiFi, you're able to send and receive encrypted text messages direcly over the air with other Meshtastic users.

![meshtastic](/uploads/deb0794cb21fadb067d4fb512096856c/meshtastic.gif)

As described on [meshtastic.org](https://meshtastic.org/), Meshtastic is:

> An open source, off-grid, decentralized mesh network built to run on affordable, low-power devices. No cell towers. No internet. Just pure peer-to-peer connectivity.

For those not well-versed in technobabble:

- **open source** : All of the design files and software code you need to manufacture and program the Meshtastic devices is freely available for anyone to read and use.

- **off-grid** : These low-power devices can be run from a solar panel or battery and do not require access to the electrical grid.

- **decentralized** : The network is a result of many devices working together, with each device playing a more or less equal role (see: [Roles](https://meshtastic.org/docs/configuration/radio/device/#roles)), so there's no one "central" device that if turned off would cause the network to stop working. 

- **mesh network** : Each device can act as a relay by retransmitting messages that it receives that are not addressed to the device itself. It's kind of like if you get someone else's piece of mail, e.g. a letter, delivered to your house, you would just put it in your neighbor's mailbox, and they would put it in the next neighbor's mailbox, until it eventually gets to the right address. And because messages are encrypted, even if one of the neighbors opened up the mail to see what's inside, they wouldn't be able to read it.  

- **affordable, low-power devices** : Barebones Meshtastic cicuit boards [start at around $20](https://heltec.org/product-category/lora/meshtastic/).

- **peer-to-peer connectivity** : Any two devices can communicate directly with one another. You don't need a whole mesh network for it to work.

## Other Technologies

In addition to Meshastic, many of the same radio devices can be reprogrammed to function as nodes in the following alternative network types:

### [Meshcore](https://meshcore.co.uk/)

Meshcore is similar to Meshtastic in many ways, but requires dedicated repeater devices that must be maintained as citical network infrastructure, whereas in Meshtastic, almost every device functions as a repeater, allowing the network to dynamically recongiure based on available nodes. The upside to Meshcore is that it's more efficient and reliable than Meshtastic.

From the Seeed [Studio MeshCore or Meshtastic: Which one is better?](https://www.seeedstudio.com/blog/2026/03/23/meshcore-vs-meshtastic/) blog post:

- **Choose Meshtastic** if you need a plug-and-play, collective network for hiking, skiing, or tactical teams where every device is a team player.

- **Choose MeshCore** if you are building a robust, high-capacity urban backbone that requires massive hop counts and dedicated infrastructure without the noise.

### [Reticulum](https://reticulum.network/)

Reticulum differs from Meshtastic / Meshcore in that it's a general networking stack that, beyond just text messages, can basically do anything that you can do over the Internet (e.g. email, images, websites, voice chat).

From [the Reticulum website](https://reticulum.network):

> Reticulum is the cryptography-based networking stack for building local and wide-area networks with readily available hardware. Reticulum can continue to operate even in adverse conditions with very high latency and extremely low bandwidth.

