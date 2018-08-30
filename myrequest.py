import requests
import re
body = "Change guest_msrs in vcpu data structure from pointer to array, which\r\ncould avoid the dynamic memory allocation.\r\n\r\nv1 -> v2:\r\n * Remove the unnecessary initiguest_msrs[] since vcpu is\r\n   allocated by calloc.\r\n\r\nTracked-On: #861\r\nSigned-off-by: Shiqing Gao <shiqing.gao@intel.com>\r\nAcked-by: Anthony Xu <anthony.xu@intel.com>"


list = re.findall(r'Tracked-On: #(\d+)', body)
print(list)