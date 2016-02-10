#!/bin/env /opt/anaconda2/bin/python

from __future__ import print_function
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SQLContext, Row

title = "Iteration #3"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " <zk> <topic> </checkpoint/dir>", file=sys.stderr)
        exit(-1)

    zkQuorum, topic, checkpointDirectory = sys.argv[1:]

    sc = SparkContext(appName=title)
    ssc = StreamingContext(sc, 1)
    ssc.checkpoint(checkpointDirectory)

    kafkaStream = KafkaUtils.createStream(ssc, zkQuorum, "iter-consumer", {topic: 1})

    event = kafkaStream.map(lambda x: x[1])
    lines = event.flatMap(lambda line: line.split("\n"))
    fields = lines.map(lambda f: f.split(","))
    callsignfields = fields.map(lambda c: (c[10]))
    notnulls = callsignfields.filter(lambda c: (c != ''))
    callsigns = notnulls.map(lambda c: (c, 1))
    counts = callsigns.reduceByKeyAndWindow(lambda a, b: a+b, lambda a, b: a-b, 600, 10)
    counts.pprint()

    ssc.start()
    ssc.awaitTermination()
