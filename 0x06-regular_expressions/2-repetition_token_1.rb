#!/usr/bin/env ruby
#script that accepts one argument and pass it to a regular expression matching method

print ARGV[0].scan(/hb?t?n/).join
