# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message

exec { 'change_hard_nofile_limit':
  command     => "/bin/sed -i 's/holberton hard nofile 5/holberton hard nofile 50000/' /etc/security/limits.conf",
}

exec { 'change_soft_nofile_limit':
  command     => "/bin/sed -i 's/holberton soft nofile 4/holberton soft nofile 50000/' /etc/security/limits.conf",
}
