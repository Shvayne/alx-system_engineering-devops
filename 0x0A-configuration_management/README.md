# 0x0A Configuration Management

This repository contains examples and exercises related to configuration management using Puppet. Configuration management is an essential practice in DevOps and IT operations that involves managing and automating the configuration of servers

## Introduction

Configuration management allows you to automate the management of your infrastructure, ensuring consistency, efficiency, and reliability. Puppet is a powerful tool used for configuration management, allowing you to define the desired state of your systems using code.

## Setup

To use the examples in this repository, you need to have Puppet installed on your system. You can follow the official [Puppet installation guide](https://puppet.com/docs/puppet/latest/installing_and_upgrading.html) to set it up.

## Puppet Manifest Examples

### Creating a File in /tmp

This example demonstrates how to create a file in the `/tmp` directory with specific permissions, owner, group, and content using a Puppet manifest.

```puppet
file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}

