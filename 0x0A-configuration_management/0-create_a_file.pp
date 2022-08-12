# create school file
  file { '/tmp/school':
    content => 'I love Puppet', #this text will be inside the file
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
  }

