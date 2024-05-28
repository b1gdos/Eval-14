import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print("Connecting via SSH => show ip interface brief")
#
from netmiko import ConnectHandler
router1 = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.1.2",
    port="22",
    username="admin",
    password="cisco"
    )
router2 = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.1.2",
    port="22",
    username="admin",
    password="cisco"
    )
switch1 = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.1.4",
    port="22",
    username="admin",
    password="cisco"
    )
switch2 = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.1.5",
    port="22",
    username="admin",
    password="cisco"
    )
switch3 = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.1.6",
    port="22",
    username="admin",
    password="cisco"
    )
output=router1.send_command("show ip interface brief")
output2=router2.send_command("show ip interface brief")
output3=switch1.send_command("show ip interface brief")
output4=switch2.send_command("show ip interface brief")
output5=switch3.send_command("show ip interface brief")

print("Router1: " + output)
print("Router2: " + output2)
print("Switch1: " + output3)
print("Switch2: " + output4)
print("Switch3: " + output5)