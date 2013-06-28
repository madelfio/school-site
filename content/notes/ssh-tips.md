Title: SSH Tips
Subtitle: Tips for SSH'ing around the lab machines
Date: 2013-02-07 23:47
Author: Marco D. Adelfio
Summary: Tips for SSH'ing around the lab machines.
Category: Notes

*These are instructions for using ssh to access a machine that doesn't have a
public IP address by going through one that does.  They're written for
machines on the UMIACS network at UMD, but should apply generically.*

<hr />

Say you're on your home computer, which we'll call "home-pc", and want to ssh
to a lab computer, "lab-pc".  You probably can't do this directly because most
of the UMIACS lab machines don't have public IP addresses:

    :::console
    user@home-pc:~$ host lab-pc.umiacs.umd.edu
    lab-pc.umiacs.umd.edu has address 192.168.83.91

The 192.168.0.0/16 block is a private IP block inside the UMIACS network, so
this means you can't directly access lab-pc.umiacs.umd.edu from other
networks. But some hosts on the UMIACS network, like
openlab.umiacs.umd.edu, are publicly accessible:

    :::console
    user@home-pc:~$ host openlab.umiacs.umd.edu
    openlab.umiacs.umd.edu has address 128.8.132.247
    openlab.umiacs.umd.edu has address 128.8.132.248

This means you can go through openlab to get to the lab machines.

    :::console
    user@home-pc:~$ ssh openlab.umiacs.umd.edu
    user@openlab.umiacs.umd.edu's password:
    user@opensub00:~$ ssh lab-pc.umiacs.umd.edu
    user@lab-pc.umiacs.umd.edu's password:
    user@lab-pc:~$

And we're in!  Unfortunately this is tedious because you have to go through
openlab and enter your password twice.  Accessing the lab machines remotely
is much more convenient without these hassles, so let's get rid of them.

## Generate SSH key

To avoid entering a password every time, you can create an ssh key.  There
are many guides on this, like [this one from github][1].

The short version is:

    :::console
    user@home-pc:~$ ssh-keygen -t rsa
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/user/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase): [Type a passphrase]
    Enter same passphrase again: [Type passphrase again]
    user@home-pc:~$ ssh-copy-id user@openlab.umiacs.umd.edu
    user@openlab.umiacs.umd.edu's password:

Now you can ssh to openlab without entering your password (depending on your
OS and system setup, you will need to enter the passphrase for your ssh key,
but you should only need to do this once if you have an ssh agent running).

    :::console
    user@home-pc:~$ ssh openlab.umiacs.umd.edu
    user@openlab.umiacs.umd.edu:~$

## Proxy SSH through openlab

To avoid manually ssh'ing through openlab.umiacs.umd.edu, you can automate
the process with an ssh "ProxyCommand".  Add the following lines to your
~/.ssh/config file on your remote computer (create it if it doesn't exist),
repeated for each host you'd like to be able to ssh to directly.

    Host lab-pc
      Hostname lab-pc.umiacs.umd.edu
      ForwardAgent yes
      ProxyCommand ssh openlab.umiacs.umd.edu nc %h %p

If you have a username (e.g., USERNAME) on the lab-pc and/or the intermediate
machine that's different from your username on your home-pc, you can add the
line `User USERNAME` within this section of your config and update the
ProxyCommand line with `USERNAME@openlab...` to get ssh to use the correct
one.

## End result

Once you generate an ssh key and add the proxy command above, you can ssh into
a lab machine with a single command.

    :::console
    user@home-pc:~$ ssh lab-pc
    user@lab-pc.umiacs.umd.edu:~$

#### Updates

6/20/13 - Reworded some sections for clarity.

[1]: https://help.github.com/articles/generating-ssh-keys
