#!/usr/bin/env ruby
# script that acepts one argument and pass it to a regex metching method
print ARGV[0].scan(/School/).join
