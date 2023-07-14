#puppet manifest to installl and configure nginx server

package { "nginx":
  ensure => 'installed',
}

file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => server {
	listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html;
        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
	}
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}
	
service { 'nginx':
  ensure => running,
  enable => true
  require => [
	package['nginx'],
	file['/etc/nginx/sites-enabled/default'],
	]
}
