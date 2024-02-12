## Open Terminal & Type Below Commands

Raspberry Pi Software Configuration
```bash
  sudo pip3 install picamera
  sudo raspi-config
```
```bash
  Interface Option -> Legacy Camera -> Enable -> Yes -> OK -> Finish
  Interface Option -> SPI -> Enable -> Yes -> OK -> Finish
```
Enter Cammand to Reboot
```bash
   sudo reboot
```
Now Again Open Terminal Type 
Enter Cammand to Reboot
```bash
   cd IOT/Camera
```

### Run Python Program
```bash
  cd Camera 
  python picamera.py
```
OR
```bash
  cd Camera
  python3 picamera.py
```
OR
```bash
  cd Camera
  ./picamera.py
```
