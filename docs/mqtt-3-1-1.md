## Session present flag
- This flag is used to determine whether the session flag is present or not. 
## Error codes on failed subscriptions

| Error code (Decimal) | Error code (Hexadecimal) | Meaning                                                       |
| -------------------- | ------------------------ | ------------------------------------------------------------- |
| 0                    | 0x0                      | No Error                                                      |
| 1                    | 0x1                      | Connection Refused: Unacceptable protocol version             |
| 10                   | 0xa                      | Timeout waiting for SUBACK                                    |
| 11                   | 0xb                      | Timeout waiting for UNSUBACK                                  |
| 12                   | 0xc                      | Timeout waiting for PINGRESP                                  |
| 13                   | 0xd                      | Malformed Remaining Length                                    |
| 14                   | 0xe                      | Problem with the underlying communication port                |
| 15                   | 0xf                      | Address could not be parsed                                   |
| 16                   | 0x10                     | Malformed received MQTT packet                                |
| 17                   | 0x11                     | Subscription failure                                          |
| 18                   | 0x12                     | Payload decoding failure                                      |
| 19                   | 0x13                     | Failed to compile a Decoder                                   |
| 2                    | 0x2                      | Connection Refused: Identifier rejected                       |
| 20                   | 0x14                     | The received MQTT packet type is not supported on this client |
| 21                   | 0x15                     | Timeout waiting for PUBACK                                    |
| 22                   | 0x16                     | Timeout waiting for PUBREC                                    |
| 23                   | 0x17                     | Timeout waiting for PUBCOMP                                   |
| 3                    | 0x3                      | Connection Refused: Server Unavailable                        |
| 4                    | 0x4                      | Connection Refused: Bad username or password                  |
| 5                    | 0x5                      | Connection Refused: Authorization error                       |
| 6                    | 0x6                      | Connection lost or bad                                        |
| 7                    | 0x7                      | Timeout waiting for Length bytes                              |
| 8                    | 0x8                      | Timeout waiting for Payload                                   |
| 9                    | 0x9                      | Timeout waiting for CONNACK                                   |

## Anonymous MQTT clients
- If we require a temporary client to connect to the broker, we can use the anonymous MQTT client. MQTT broker will assign random client ID to the anonymous client.
<img src="https://github.com/vishwasracharya/mqtt/blob/main/screenshots/mosquitto_implementation.png" alt="Anonymous MQTT clients" />

## Immediate publishes
- An abilty to send a messages without waiting for a CONNACK response from the broker.
- This is better for the burst-mode clients. Those who only care about sending messages.

## No client identifier restrictions
- Previously there was a limit for characters in the client identifier (23 char for CONNECT message). This has been removed in MQTT 3.1.1.
