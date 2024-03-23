# create a manifest that kills a process named killmenow using puppet

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
