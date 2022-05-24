---
title: "Towards a tangible data mesh with expat-fatcat"
published: false
---

Avoiding analytical data downstream from operational data, identified as antipattern in data-mesh book.

Notes

* the choice for the [django rest framework]() is not strictly necessary, but rather to have 1.) a convenient front-end without writing html templates, and 2.) built-in serializers support.


## Setup

Follow roughly [Ankitthakur/apache-kafka-installation-on-mac-using-homebrew](https://medium.com/@Ankitthakur/apache-kafka-installation-on-mac-using-homebrew-a367cdefd273).

1. `brew install java` + adding to path
1. `brew install kafka`

### Producing and consuming messages from the console

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

## Data products for the expat-fatcat-app

```console
kafka-topics --create --topic fatcat-conversions --bootstrap-server localhost:9092 --replication-factor 1 --partitions 2
```

```console
kafka-topics --create --topic fatcat-users --bootstrap-server localhost:9092 --replication-factor 1 --partitions 2
```

### First implementation

Note: there are so many suboptimal design choices in this implementation that it doesn't even deserve a commit in my opinion. But it works, and shows that we're going in a constructive direction.

Modify [conversions/views.py](https://github.com/munichpavel/expat-fatcat-app/blob/83c8593feb452d6208178d628a5e796e4d2cabed/conversions/views.py)'s

```python
from kafka import KafkaProducer

class ConversionList(generics.ListCreateAPIView):
    queryset = Conversion.objects.all()
    serializer_class = ConversionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        producer.send('fatcat-conversions', b'some_message_bytes')
        serializer.save(owner=self.request.user)
```

now go to your localhost django rest server conversions endpoint (e.g. [http://127.0.0.1:8000/conversions/](http://127.0.0.1:8000/conversions/) and enter a new conversion.

And rejoice, because your local kafka consumer gets the message

```console
(base) Pauls-MacBook-Air:expat-fatcat-app pauldev$ kafka-console-consumer --bootstrap-server  localhost:9092 --topic fatcat-conversions
some_message_bytes
```
