#configure ab Nginx server to listen on port 80 and perform 301 redirects
include stdlib

package { 'nginx':
  ensure => installed
}

exec { 'allow_HTTP':
  command => '/usr/sbin/ufw allow "Nginx HTTP"',
  require => Package['nginx']
}

file { 'index.html':
  ensure  => file,
  path    => '/var/www/html/index.html',
  content => '<h2>Hello World!</h2>'
}

$redirect_301 = ['    location /redirect_me {',
          '         return 301 http://youtube.com;',
          '    }']

$redirect_301.each |$input| {
  file_line { "add_line_${input}":
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => $input,
    match  => 'server_name _;'
  }
}

exec { 'restart_nginx':
  command => 'usr/sbin/service nginx restart'
}

