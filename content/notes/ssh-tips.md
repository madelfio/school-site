Title: SSH Tips
Subtitle: Tips for SSH'ing around the lab machines
Date: 2013-02-07 23:47
Author: Marco D. Adelfio
Summary: Tips for SSH'ing around the lab machines.
Category: Notes

The lab machines do not have public IP addresses by default.

    :::console
    user@home-pc:~$ host lab-pc.umiacs.umd.edu
    lab-pc.umiacs.umd.edu has address 192.168.83.91

The 192.168.0.0/16 block is not for public addresses, so this means you
won't be able to directly talk to lab-pc.umiacs.umd.edu from outside of the
UMIACS network.  But openlab.umiacs.umd.edu is publicly accessible.

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

But this is tedious because you have to go through openlab and enter your
password twice.  Remote access to the lab machines would be much more
convenient if you could avoid these two hassles.

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

Now you can ssh to openlab without entering your password (depending on
your OS, you may need to enter the passphrase for your ssh key, but you
should only need to do this once).

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

## Conclusion

Once you follow the steps above, you can ssh into a lab machine with one
command and no ssh passwords.

    :::console
    user@home-pc:~$ ssh lab-pc
    user@lab-pc.umiacs.umd.edu:~$

[1]: https://help.github.com/articles/generating-ssh-keys
