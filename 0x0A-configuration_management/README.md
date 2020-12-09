#  0x0A Configuration management
## Puppet - Manifest Files
In Puppet, all the programs which are written using Ruby programming language and saved with an extension of .pp are called manifests. In general terms, all Puppet programs which are built with an intension of creating or managing any target host machine is called a manifest. All the programs written in Puppet follow Puppet coding style.

The core of Puppet is the way resources are declared and how these resources are representing their state. In any manifest, the user can have a collection of different kind of resources which are grouped together using class and definition.

In some cases, Puppet manifest can even have a conditional statement in order to achieve a desired state. However, ultimately it all comes down to make sure that all the resources are defined and used in the right way and the defined manifest when applied after getting converted to a catalog is capable of performing the task for which it was designed.

Manifest File Workflow
Puppet manifest consists of the following components −

Files (these are plain files where Puppet has nothing to do with them, just to pick them up and place them in the target location)

Resources

Templates (these can be used to construct configuration files on the node).

Nodes (all the definition related to a client node is defined here)

Classes

Points to Note
In Puppet, all manifest files use Ruby as their encoding language and get saved with .pp extension.

"Import" statement in many manifest are used for loading files when Puppet starts.

In order to import all files contained in a directory, you can use the import statement in another way like import 'clients/*'. This will import all .pp files inside that directory.
___

![puppet](https://www.tutorialspoint.com/puppet/images/manifest.jpg)