![bash](https://blog.desdelinux.net/wp-content/uploads/2019/01/bash-logo.jpg.webp)
___
___

# [0x04]. Bash - Loops, conditions and parsing


## :boom: What is the advantage of using #!/usr/bin/env bash over #!/bin/bash

Running a command through /usr/bin/env has the benefit of looking for whatever the default version of the program is in your current environment.
This way, you don't have to look for it in a specific place on the system, as those paths may be in different locations on different systems. As long as it's in your path, it will find it.


## :boom: How to use while,  until and for loops

In this section you'll find for, while and until loops.

The for loop is a little bit different from other programming languages. Basically, it let's you iterate over a series of 'words' within a string.

The while executes a piece of code if the control expression is true, and only stops when it is false (or a explicit break is found within the executed code.

The until loop is almost equal to the while loop, except that the code is executed while the control expression evaluates to false.

If you suspect that while and until are very similar you are right.

##### For Example:

        #!/bin/bash
        for i in $( ls ); do
            echo item: $i
        done


On the second line, we declare i to be the variable that will take the different values contained in $( ls ).

The third line could be longer if needed, or there could be more lines before the done (4).
'done' (4) indicates that the code that used the value of $i has finished and $i can take a new value.
This script has very little sense, but a more useful way to use the for loop would be to use it to match only certain files on the previous example

##### For Example:

        #!/bin/bash
        for i in `seq 1 10` ;
        do
                echo $i
        done

### While Example:

         #!/bin/bash
         COUNTER=0
         while [  $COUNTER -lt 10 ]; do
             echo The counter is $COUNTER
             let COUNTER=COUNTER+1
         done

### Until Example:

         #!/bin/bash
         COUNTER=20
         until [  $COUNTER -lt 10 ]; do
             echo COUNTER $COUNTER
             let COUNTER-=1
         done

## How to use if,  else,  elif and case condition statements

Bash conditional statements are those which allow us to take some action towards various conditions. These statements implement blocks of code, based on whether the condition specified by the programmer evaluates to true or false. If it evaluates to true, executes a specific block of code otherwise move to the next condition.

There are various types of conditional statements in Bash:

    1. if statement
    2. if-else statement
    3. if..elif..else statement
    4. Nested

The syntax of if, elseif, else is:

    if <test_expression>;  then
        <command-to-execute>
    elif <test_expression>;  then
        <command-to-execute>
    else
        <command-to-execute>
    fi

## How to use the cut command

The cut command in UNIX is a command for cutting out the sections from each line of files and writing the result to standard output. It can be used to cut parts of a line by byte position, character and field. Basically the cut command slices a line and extracts the text. It is necessary to specify option with command otherwise it gives error. If more than one file name is provided then data from each file is not precedes by its file name.

Syntax:
    cut OPTION... [FILE]...


## What are files and other comparison operators, and how to use them

The comparison operators are used in Bash to compare the values. By default, all comparison operators are case-sensitive. These operators help us to find, test, compare, modify, and replace the data and information.

![operators](https://static.javatpoint.com/tutorial/powershell/images/powershell-comparison-operators.png)

___

## How to create SSH keys

#### Public Key authentication - what and why?

The motivation for using public key authentication over simple passwords is security. Public key authentication provides cryptographic strength that even extremely long passwords can not offer. With SSH, public key authentication improves security considerably as it frees the users from remembering complicated passwords (or worse yet, writing them down).
In addition to security public key authentication also offers usability benefits - it allows users to implement single sign-on across the SSH servers they connect to. Public key authentication also allows automated, passwordless login that is a key enabler for the countless secure automation processes that execute within enterprise networks globally.
Public key cryptography revolves around a couple of key concepts. The sections below explain these briefly.
#### Asymmetric Cryptography - Algorithms
As with any encryption scheme, public key authentication is based on an algorithm. There are several well-researched, secure, and trustworthy algorithms out there - the most common being the likes of RSA and DSA. Unlike the commonly known (symmetric or secret-key) encryption algorithms the public key encryption algorithms work with two separate keys. These two keys form a pair that is specific to each user.

#### Key Pair - Public and Private

In the SSH public key authentication use case, it is rather typical that the users create (i.e. provision) the key pair for themselves. SSH implementations include easily usable utilities for this (for more information see ssh-keygen and ssh-copy-id).

Each SSH key pair includes two keys:

##### A public key: 

that is copied to the SSH server(s). Anyone with a copy of the public key can encrypt data which can then only be read by the person who holds the corresponding private key. Once an SSH server receives a public key from a user and considers the key trustworthy, the server marks the key as authorized in its authorized_keys file. Such keys are called authorized keys.

##### A private key: 

that remains (only) with the user. The possession of this key is proof of the user's identity. Only a user in possession of a private key that corresponds to the public key at the server will be able to authenticate successfully. The private keys need to be stored and handled carefully, and no copies of the private key should be distributed. The private keys used for user authentication are called identity keys.

#### Setting Up Public Key Authentication for SSH

The following simple steps are required to set up public key authentication (for SSH):

    1. Key pair is created (typically by the user). This is typically done with ssh-keygen.
    2. Private key stays with the user (and only there), while the public key is sent to the server. Typically with the ssh-copy-id utility.
    3. Server stores the public key (and "marks" it as authorized).
    4. Server will now allow access to anyone who can prove they have the corresponding private key.
