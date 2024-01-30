#!/usr/bin/env ruby
# script that accepts one argument and pass it to a regex matching method

print ARGV[0].scan(/School/).join
