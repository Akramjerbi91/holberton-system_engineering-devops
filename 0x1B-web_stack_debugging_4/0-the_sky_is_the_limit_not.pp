# Make limit 4000
exec { 'fix limit':
  command => 'sed -i 's/15/4000/g' /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}
