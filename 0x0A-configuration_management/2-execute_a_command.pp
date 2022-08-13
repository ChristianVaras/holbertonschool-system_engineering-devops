# Create a manifest that kills a process named killmenow

exec { 'killmenow':
  command  => 'pkill killmenow',
  path     => '/usr/local/bin:/usr/sbin:/bin',
  provider => 'shell',
  user     => 'root',
}