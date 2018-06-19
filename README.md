# Arrange IPs!
A simple script to group IP addresses into their range. 

### Eg:
```
    10.0.0.1, 10.10.0.2, 10.0.0.3 becomes 10.0.0.1-10.0.0.3
```
```mermaid
graph LR
A(10.0.0.1) --- D(10.0.0.1-10.0.0.3)
B(10.0.0.2) --- D(10.0.0.1-10.0.0.3)
C(10.0.0.3) --- D(10.0.0.1-10.0.0.3)
```
### Usage
```
    python Arrange.py -i ip.txt
```
