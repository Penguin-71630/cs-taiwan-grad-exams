<!-- src: devin -->
(a) Battery/PMIC → low-power ARM SoC; camera, microphone, GPS and controls ↔ SoC bus ↔ RAM, flash, Wi-Fi/Bluetooth, audio output and prism-display controller. Choose low-latency image processing, sufficient frame-buffer RAM, flash for OS/app and minimal cached data, with low weight, heat and power consumption.\
(b) No: Glass camera/client app ↔ encrypted Wi-Fi ↔ authenticated API server ↔ face-recognition service and passenger database; upload a face image, match it on the server, retrieve authorized passenger information, and return a display overlay.
