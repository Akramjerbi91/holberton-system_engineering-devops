# Enable the user holberton to login and open files without error.

exec { 'increase-hard-file-limit-for-holberton-user':
  command => '/bin/sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf && /bin/sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
}
