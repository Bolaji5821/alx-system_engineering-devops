# creating a file in a directory called /tmp
file {'/temp/holberton':
  ensure  =>  'file',
  mode    =>  '0744',
  owner   =>  'www-data',
  content => 'I love Puppet',
}
