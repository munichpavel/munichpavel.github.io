---
title: "Towards a tangible data mesh with expat-fatcat"
published: false
---

## Avoiding analytical data downstream from operational data

Identified as antipattern.

### Setup

Follow roughly [Ankitthakur/apache-kafka-installation-on-mac-using-homebrew](https://medium.com/@Ankitthakur/apache-kafka-installation-on-mac-using-homebrew-a367cdefd273).

1. `brew install java` + adding to path
1. `brew install kafka`

#### Producing and consuming messages from the console

Please note that the settings used here are purely for (local) demo purposes. For anything else you should look into proper configuration.

```console
kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 2
```

```console
kafka-topics --list --bootstrap-server localhost:9092
__consumer_offsets
fatcat-users
test-topic
```

In one console run a kafka-console-producer with `kafka-console-producer --broker-list localhost:9092 --topic test-topic` and in another run a kafka-console-consumer with `kafka-console-consumer --bootstrap-server  localhost:9092 --topic test-topic`.

Now you are ready to produce and consume some first messages. For dramatic effect, it is best to do this with your two consoles side-by-side.

Producer:

```console
(base) Pauls-MacBook-Air:expat-fatcat-app pauldev$ kafka-console-producer --broker-list localhost:9092 --topic test-topic
>yoyo
>wassup
```

And in the consumer console:

```console
(base) Pauls-MacBook-Air:expat-fatcat-app pauldev$ kafka-console-consumer --bootstrap-server  localhost:9092 --topic test-topic
yoyo
wassup
```

### Data products for the expat-fatcat-app

```console
kafka-topics --create --topic fatcat-users --bootstrap-server localhost:9092 --replication-factor 1 --partitions 2
```