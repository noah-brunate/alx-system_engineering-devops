# Manifest instals a flask fron pip3 of 2.1.0 version
package { 'flask':
      ensure   => '2.1.0',
      provider => 'pip3',
}
