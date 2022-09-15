import argparse
import os

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--canal", help= "canal")
parametros = parser.parse_args()

canal = parametros.canal

os.environ["pubsub_uuid"] = "luiza-pc"

pnconfig = PNConfiguration()

pnconfig.uuid = os.environ["pubsub_uuid"]
os.environ["pubsub_pub"] = "pub-c-0ad73c69-b4a7-4915-8282-2481d3a28883"
os.environ["pubsub_sub"] = "sub-c-50246af4-4f05-48d9-bd18-1017c9c92fb5"

pnconfig.publish_key = os.getenv("pubsub_pub")
pnconfig.subscribe_key = os.getenv("pubsub_sub")

usr = input("Seu nome: ")
print("-"*50)

pubnub = PubNub(pnconfig)

while True:
    msg = input("Fala ae: ")
    envelope = pubnub.publish().channel(canal).message({"msg": msg, "usr": usr}).sync()

    if envelope.status.is_error():
        print("->>>>> DEU PAU")
