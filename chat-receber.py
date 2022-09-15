import argparse
import os
from datetime import datetime

from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--canal", help= "canal")
parametros = parser.parse_args()

canal = parametros.canal

os.environ["pubsub_uuid"] = "luiza-pc"

pnconfig = PNConfiguration()

os.environ["pubsub_pub"] = "pub-c-0ad73c69-b4a7-4915-8282-2481d3a28883"
os.environ["pubsub_sub"] = "sub-c-50246af4-4f05-48d9-bd18-1017c9c92fb5"

pnconfig.publish_key = os.getenv("pubsub_pub")
pnconfig.subscribe_key = os.getenv("pubsub_sub")

pnconfig.uuid = os.environ["pubsub_uuid"]


pubnub = PubNub(pnconfig)


class RecebeMensagem(SubscribeCallback):
    def presence(self, pubnub, event):
        pass

    def status(self, pubnub, event):
        pass

    def message(self, pubnub, event):
        print("{}: {}\n{}".format(event.message["usr"], event.message["msg"], datetime.now().strftime("%H:%M:%S")))


pubnub.add_listener(RecebeMensagem())
pubnub.subscribe().channels(canal).with_presence().execute()
