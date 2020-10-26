#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - infinite loop
 * Return: 1 on error, 0 on success
 */
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 * main - entry point
 * Return: 1 on error, 0 on success
 */
int main(void)
{
int i = 5;
pid_t child_pid;

while (i--)
{
child_pid = fork();
if (child_pid > 0)
{
printf("Zombie process created, PID: %i\n", child_pid);
}
else
exit(0);
}
infinite_while();

return (0);
}
