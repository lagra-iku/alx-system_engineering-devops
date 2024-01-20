# fix wordpress site running on LAMP Stack

exec {'add':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
