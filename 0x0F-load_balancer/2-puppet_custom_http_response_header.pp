#install Nginx package using puppet
package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => file,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm;

        server_name _;

        location / {
            add_header X-Served-By $::hostname;
            try_files \$uri \$uri/ =404;
        }
    }
  ",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
