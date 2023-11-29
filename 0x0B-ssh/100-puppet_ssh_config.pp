# using Puppet to make changes to our configuration file
$file_content = @(CONTENT)
Host *
        PasswordAuthentication no
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/school
        HostName 52.87.220.126
        User ubuntu
CONTENT

file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => $file_content,
  mode    => '0600', 
}
