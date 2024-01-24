# fixing Nginx when under pressure 

exec { 'change':
  command  => 'sudo sed -i "s/15/4096/" /etc/default/nginx',
  provider => shell,
  before   => Exec['restart'],
}

exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
