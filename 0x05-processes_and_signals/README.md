# Bash - 0x05. Processes and signals
## What is a PID [^1]

    A PID (i.e., process identification number) is an identification number that is automatically
    assigned to each process when it is created on a Unix-like operating system.

A process is an executing (i.e., running) instance of a program. Each process is guaranteed a unique PID, which is always a non-negative integer.

The process init is the only process that will always have the same PID on any session and on any system, and that PID is 1. This is because init is always the first process on the system and is the ancestor of all other processes.

A very large PID does not necessarily mean that there are anywhere near that many processes on a system. This is because such numbers are often a result of the fact that PIDs are not immediately reused, in order to prevent possible errors.

The default maximum value of PIDs is 32, 767. This maximum is important because it is essentially the maximum number of processes that can exist simultaneously on a system. Although this will almost always be sufficient for a small system, large servers may require many more processes. The lower the maximum value, the sooner the values will wrap around, meaning that lower values do not necessarily indicate processes that started to run earlier.

The file pid_max, which was introduced with the Linux 2.5 kernel, specifies the value at which PIDs wrap around (i.e., the value in this file is one greater than the maximum PID). It has a default of 32768, but it can be set to any number up to approximately four million. The maximum number of processes on a system is only limited by the amount of physical memory (i.e.,  RAM) available.
The PIDs for the processes currently on the system can be found by using the ps command or the pstree command (which shows the process names and PIDs in a tree diagram). The top command also shows the PIDs of currently running processes along with other information about them, but it differs in that it continuously updates the information. The pidof command provides the PID of a program whose name is passed to it as an argument (i.e., input).

![ps output](https://www.tecmint.com/wp-content/uploads/2017/09/List-Current-Running-Processes.png)

The PID is needed in order to terminate a frozen or otherwise misbehaving program with the kill command. This command makes it possible to end a program that cannot otherwise be stopped except by rebooting (i.e., restarting) the system, and it is thus an important element in the stability and robustness of Unix-like operating systems.

___

## What is a signal? [^2]

    Signals are software interrupts.

A robust program need to handle signals. This is because signals are a way to deliver asynchronous events to the application.
A user hitting ctrl+c, a process sending a signal to kill another process etc are all such cases where a process needs to do signal handling.

Linux Signals
In Linux, every signal has a name that begins with characters SIG. For example :
A SIGINT signal that is generated when a user presses ctrl+c. This is the way to terminate programs from terminal.
A SIGALRM  is generated when the timer set by alarm function goes off.
A SIGABRT signal is generated when a process calls the abort function.
etc
When the signal occurs, the process has to tell the kernel what to do with it.  There can be three options through which a signal can be disposed :

    1. The signal can be ignored. By ignoring we mean that nothing will be done when signal occurs.
    Most of the signals can be ignored but signals generated by hardware exceptions like divide by
    zero, if ignored can have weird consequences. Also, a couple of signals like SIGKILL and SIGSTOP
    cannot be ignored.
    2. The signal can be caught. When this option is chosen, then the process registers a function
    with kernel. This function is called by kernel when that signal occurs. If the signal is non
    fatal for the process then in that function the process can handle the signal properly or
    otherwise it can chose to terminate gracefully.
    3. Let the default action apply. Every signal has a default action. This could be process
    terminate, ignore etc.


As we already stated that two signals SIGKILL and SIGSTOP cannot be ignored. This is because these two signals provide a way for root user or the kernel to kill or stop any process in any situation . The default action of these signals is to terminate the process. Neither these signals can be caught nor can be ignored.

![signals](https://www.wisdomjobs.com/tutorials/linux-signals-revisited.png)

___

References:

[^1]: [linfo.org](http://www.linfo.org/pid.html)

[^2]: [thegeekstuff.com](https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/)
