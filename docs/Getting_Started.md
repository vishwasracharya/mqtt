# MQTT  (Message Queuing Telemetry Transport)

Installation Guide (Ubuntu): https://www.vultr.com/docs/install-mosquitto-mqtt-broker-on-ubuntu-20-04-server/

Subscribe & Publisher Command With Authentication:
```bash
mosquitto_sub -u YOUR_USERNAME -P YOUR_PASSWORD -t “home/lights/sitting_room”
```

```bash
mosquitto_pub -u YOUR_USERNAME -P YOUR_PASSWORD -t “home/lights/sitting_room” -m “ON”
```

## MQTT Message Types:
3 types of messages are primarily used:

<strong>CONNECT:</strong> Used for clients to send connection requests to the broker
<strong>PUBLISH:</strong> Used by the client/sender to publish letters to the broker
<strong>SUBSCRIBE:</strong> Used by the client/receiver to receive notifications from the broker

## Characteristics:
- Machine to Machine
- Simple & Lightweight
- Fast Delivery
- Doesn’t require the client & server to communicate at the same time

## Architecture/Comonents:
- Message
- Client
- Server & Broker
- TOPIC

## QoS Levels:
- 0 - at most once (Client publish & NO Acknowledgment by broker)
- 1 - at least once (Client publishes & Acknowledgement is sent back to the sender)
- 2 - exactly once (Both sender and receiver will get one message accordingly)

## Last Will and Testament:
A message is sent when the client’s connection is about to get disconnected. It is a normal message.

## Retained Messages:
The broker stores the last message which is sent and if the client’s topic pattern is similar to the retained message, then the retained message is immediately sent. And Broker stores only ONE message for only ONE Topic.

## Clean / Persistent Sessions:

<strong>Clean Sessions:</strong>

- The client only needs to publish to topics, it doesn’t need to subscribe to any topics.

<strong>Persistent Sessions:</strong> 

- The client must get all the messages from certain topics, even if it is offline.
- The broker needs to store the messages so that if the connection is back online an immediate response can be sent.

## Heartbeats:
MQTT defines a heartbeat interval, and at this interval, the client will send a PINGREQ packet to the server, the server will, in turn, send a PINGRSP, each of these packets is 2 bytes of overhead.

## MQTT over WebSockets:
- Display Live information from the device sensor.
- Receive PUSH notification.

## Scaling MQTT:
1. MQTT Clients Connections
2. Subscriptions and Topics at Scale
3. Testing MQTT Message Throughput
4. Quality of Service Levels
5. Queued Messages
6. Shared Subscriptions
7. Retained Messages
8. Large-scale Client Disconnect Scenarios
9. Infrastructure Outage
10. Prolonged Network Outage
