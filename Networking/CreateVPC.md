# Creation VPC

## 1. VPC

- 1.1 set a range -> VPC CIDR `192.168.0.0/20` Range: `192.168.0.0 - 192.168.15.255` (Total Amount of IPs available in the network) -> **4096**

## 2. Create Subnets -> we create 2 subnets ; 1 Public 128IPs and 1 Private 128IPs

- 2.1 Public Subnet : `192.168.0.0/25` -> 128 IPs ( Range: `192.168.0.0 - 192.168.0.127`)
- 2.2 Private Subnet : `192.168.3.0/25` -> 128 IPs ( Range: `192.168.3.0 - 192.168.3.127`)

## 3. Create Route Tables

- 3.1 Create a Public Route Table -> Associate the Public Subnet with it
- 3.2 Create a Private Route Table -> Associate the Private Subnet with it

## 4. Create Internet Gateway

- 4.1 Attach it to the VPC
- 4.2 Add a new route to the PUBLIC ROUTE TABLE for the IGW

## 5. Create EC2 Instance in Public

- 5.1 Select your VPC in Networking Settings (Click Edit)
- 5.2 Choose your Public Subnet
- 5.3 **IMPORTANT!** Auto Assign IP -> ENABLE

## 6. OPTIONAL: Create a NAT Gateway for Private EC2 Instance

- 6.1 Create a NAT Gateway -> Select the correct VPC
- 6.2 Place it in the PUBLIC Subnet and assign an Elastic IP
- 6.3 Edit the PRIVATE Route Table and add a new Route for the NAT Gateway (`0.0.0.0/0 -> NAT-GATEWAY-ID`)
