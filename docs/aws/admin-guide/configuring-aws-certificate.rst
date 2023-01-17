Setting up HTTPS certificates on AWS
================================

With AWS Certificate Manager (ACM) you can provision and manage SSL/TLS certificates for your AWS based websites and applications. You use ACM to create or import and then manage a certificate.

Pre-requisite
--------

You need to have:

1. AWS account with required access to the resources
2. Register Domain names
3. Load Balancer
4. Route 53

Register Domain names
------------------

A fully qualified domain name (FQDN) is the unique name of an organization or individual on the Internet followed by a top-level domain extension such as .com or .org. If you do not already have a registered domain name, you can register one through Amazon Route 53.

When you want to get a new domain name, such as the example.com part of the URL http://example.com, you can register it with Amazon Route 53.

Reference link : https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html

