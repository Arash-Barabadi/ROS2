# Topic
## A topic is a named bus over which nodes exchange messages.
### 1. Data stream is unidirectional. Some nodes can publish to a topic, and some nodes can subscribe to a topic. However, there is no response from a subscriber to a publisher. The data is only flowing in one direction.
### 2. As mentioned above, a node (either publisher or subscriber) isn't aware of another node's existence. Therefore, publishers and subscribers are anonymous. A publisher only knows it is publishing to a topic, and a subscriber only knows it is subscribing to a topic.
### 3. A topic has a message type. All publishers and subscribers to a topic must use the same message type associated with that topic.
### 4. A node can have many publishers/subscribers for many different topics.
# ___________________


