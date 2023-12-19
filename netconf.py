import xml.dom.minidom
from ncclient import manager

def fetch_interface_config(host, port, username, password, interface_name):
    try:
        with manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
        ) as m:

            netconf_filter = f"""
            <filter>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <interface>
                        <GigabitEthernet>
                            <name>{interface_name}</name>
                        </GigabitEthernet>
                    </interface>
                </native>
            </filter>
            """

            netconf_reply = m.get_config(source="running", filter=netconf_filter)

            pretty_config = xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
            print(f"Configuration for Interface {interface_name}:")
            print(pretty_config)

    except Exception as e:
        print(f"An error occurred (fetch_interface_config): {e}")

if __name__ == "__main__":
    host = "192.168.38.128"
    port = 830
    username = "cisco"
    password = "cisco123!"
    interface_to_fetch = "1"

    fetch_interface_config(host, port, username, password, interface_to_fetch)
