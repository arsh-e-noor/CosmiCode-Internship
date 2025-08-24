provider "aws" {
    region = "eu-north-1"
}

resource "aws_instance" "my_ec2" {
    ami = "ami-0c4fc5dcabc9df21d"
    instance_type = "t3.micro"
    tags = {
        Name = "MyFirstInstance"
    }
}