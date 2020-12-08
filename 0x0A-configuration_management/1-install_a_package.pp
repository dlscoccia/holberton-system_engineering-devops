# Manifest that installs puppet-lint package
$lint = 'puppet-lint'
package { $lint:
    ensure   => '2.1.1',
    provider => 'gem'
}
