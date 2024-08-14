# A manifest to fix an issue
# in the Apache server by
# correcting a typo in the wordpress settings

exec { 'fix_wordpress':
	command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
	path    => ['/bin']
}
